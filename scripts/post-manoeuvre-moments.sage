import argparse
import functools
import os
import sys
import textwrap
from pathlib import Path
from itertools import chain
import multiprocessing
from typing import List
import tempfile

import sage.parallel.multiprocessing_sage as mps


script = Path(__file__).stem

project_root = Path(__file__).parents[1]
sagedir = project_root/'sage'
load_attach_path(str(sagedir))
sage.repl.load.load('pmm.sage', globals())
sage.repl.load.load('utils.sage', globals())


def moment_converter(value: str):
    try:
        order = [int(o) for o in value.split(',')]
        assert len(order) == 4
        for o in order:
            assert o >= 0
    except:
        raise ValueError(f'the input "{value}" is not a string of 4 comma-separated numbers >= 0') from None
    return order


def setup_moments(namespace):
    if namespace.highest_order is None:
        moments = [moment_converter(m) for m in namespace.moments]
    else:
        moments = list(chain.from_iterable([get_Nth_orders(n) for n in range(1, namespace.highest_order + 1)]))
    setattr(namespace, 'moments', moments)


def setup_parser():
    descr = """%(prog)s creates a Python module with expressions for post-manoeuvre moments and
their LaTeX representations.
"""
    epilog = """
Examples:

Generate expressions for all moments up to the order of 3, save to the folder 'pmm':
     %(prog)s -N 3 --output-folder pmm

Do the same using all the CPU cores available:
     %(prog)s -N 3 --output-folder pmm --num-parallel=0

Generate expressions for the 3 specified moments, of the first, second, and third order in
log-range, save to the folder 'bespoke':
    %(prog)s --moment 0,0,0,1 --moment 0,0,0,2 --moment 0,0,0,3 --output-folder bespoke

As of now, do not output sage symbolic variables. Theoretically possible using the save method
     https://homepages.math.uic.edu/~jan/mcs320/mcs320notes/lec09.html
However, to use these Sage exports elsewhere, like in pure Python code, the user would still need a
compatible version of Sagemath in its entirety, which is a major downside. For comparison, the
current export is just a (relatively bulky) piece of Python code with one dependency (numpy).
"""

    parser = argparse.ArgumentParser(description=descr,
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=epilog)

    parser.add_argument('--output-module', '--output-folder',
                        dest='output_folder', type=str, required=True,
                        help="the path to the Python module folder to be written")
    parser.add_argument('--num-parallel', '--run-parallel',
                        dest='num_parallel', type=int, default=None,
                        help='the number of moments to compute in parallel; default: serial, 0 means use all CPU cores')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-n', '-N', '--moment-order', '--highest-order',
                       dest='highest_order', type=int,
                       help='generate moments up to (and including) the highest-order')
    group.add_argument('--moment', '--order',
                       dest='moments', type=str, action='append',
                       help='generate moment of the given order, specified as 4 comma-separated non-negative numbers')
    parser.add_argument('-v', '--verbose',
                        action='count', default=0, dest='verbosity',
                        help='output more details; repeat the option to increase verbosity level')
    return parser


def process(moments: List[List], output_folder: str, num_parallel: int, verbosity: int):
    def sync(ofile):
        """Ensure the contents is fully written. See:
    https://stackoverflow.com/questions/2333872/how-to-make-file-creation-an-atomic-operation
    http://stackoverflow.com/questions/7433057/is-rename-without-fsync-safe
"""
        ofile.flush()
        os.fsync(ofile.fileno())

    def _wrapper(kls, m, output_folder):
        import textwrap
        import os
        order = ''.join([str(o) for o in m])
        mname = f'moment_{order}'
        mpath = f'{output_folder}/{mname}.py'
        mcsv = ','.join([str(o) for o in m])

        warning_header = f"""# This is a generated file. Do not edit. Run:
#     sage post-manoeuvre-moments.sage --output-folder <some/temp/dir> -v --order {mcsv}
# to recreate, then copy the file '{mname}.py' on top of this one.
"""
        pmm = kls(orders=m)
        code = pmm.moment(what="python")
        latex = textwrap.wrap(repr(pmm.moment(what="latex")), width=120L)

        with open(mpath, 'wt') as ofile:
            print(warning_header, file=ofile)
            print(code, file=ofile)
            print('', file=ofile)
            print(f'def latex_{order}():', file=ofile)
            print('    return r"""', file=ofile)
            for line in latex:
                print(line, file=ofile)
            print('"""', file=ofile)

            # cannot call sync in a subprocess, cannot pickle code objects from closures
            ofile.flush()
            os.fsync(ofile.fileno())

        return mname

    impl = str(Path(output_folder) / 'impl')
    os.makedirs(impl)
    inputs = [((PostManoeuvreMoment, m, impl), {}) for m in moments]
    results = list(mps.parallel_iter(num_parallel, _wrapper, inputs))

    # Simplify and add the stringified form that is repeatedly needed
    results = [(m[0][1], mod) for m, mod in results]
    results = [(m, ''.join([str(o) for o in m]), mod) for m, mod in results]

    def sort_results(item1, item2):
        item1 = item1[0]
        item2 = item2[0]

        if sum(item1) < sum(item2):
            return -1
        elif sum(item1) > sum(item2):
            return 1
        else:
            if item1 < item2:
                return 1
            elif item1 > item2:
                return -1
            else:
                return 0

    results.sort(key=functools.cmp_to_key(sort_results))

    if verbosity > 1:
        print('Modules generated in the parallel loop:', file=sys.stderr)
        for m, _, mod in results:
            print(f'{m}: {mod}', file=sys.stderr)

    def make_warning_header():
        cli = ' '.join(sys.argv)
        comment_prefix = "# "
        return '\n'.join([
            '# This is a generated file. Do not edit. Run:',
            f'#     {textwrap.fill(cli, width=120, subsequent_indent=comment_prefix)}',
            '# to recreate, then copy the corresponding "__init__.py" file on top of this one.',
        ])

    def generate_base_init(fname, header, results):
        init = [header, '']

        for _, order, _ in results:
            init.append(f'from .impl import moment_{order}, latex_{order}')
        init.append('')
        init.append('')

        init.append('orders = [')
        for m, _, _ in results:
            init.append(f'    {m},')
        init.append(']')
        init.append('')

        init.append('_moments = {}')
        init.append('_latexs = {}')
        init.append('')
        for m, order, _ in results:
            init.append(f'_moments[{tuple(m)}] = moment_{order}')
            init.append(f'_latexs[{tuple(m)}] = latex_{order}')
            init.append('')

        init.append('')
        init.append('def moment(orders):')
        init.append('    return _moments[tuple(orders)]')
        init.append('')
        init.append('')
        init.append('def latex(orders):')
        init.append('    return _latexs[tuple(orders)]')

        init.append('')
        init.append('def get_orders_n(n, orders, what):')
        init.append('    orders_n = {}')
        init.append('    for o in orders:')
        init.append('        if sum(o) == n:')
        init.append('            if what == "python":')
        init.append('                orders_n[tuple(o)] = _moments[tuple(o)]')
        init.append('            elif what == "latex":')
        init.append('                orders_n[tuple(o)] = _latexs[tuple(o)]')
        init.append('            else:')
        init.append('                raise ValueError(f"unknown argument {what}, not one of [python, latex]")')
        init.append('    return orders_n')

        with open(fname, 'wt') as ofile:
            for line in init:
                print(line, file=ofile)
            sync(ofile)

    def generate_impl_init(fname, header, results):
        init = [header, '']

        for _, order, _ in results:
            init.append(f'from .moment_{order} import moment_{order}, latex_{order}')

        with open(fname, 'wt') as ofile:
            for line in init:
                print(line, file=ofile)
            sync(ofile)

    header = make_warning_header()
    generate_base_init(f"{output_folder}/__init__.py", header, results)
    generate_impl_init(f"{output_folder}/impl/__init__.py", header, results)


if __name__ == '__main__':
    parser = setup_parser()
    args = parser.parse_args()

    if args.verbosity > 1:
        print(f'{script}: command-line options:', file=sys.stderr)
        for arg in vars(args):
            print('    %s: %s' % (arg, getattr(args, arg)), file=sys.stderr)
        print('', file=sys.stderr)

    ncpus = multiprocessing.cpu_count()
    if args.num_parallel is None:
        args.num_parallel = 1
    if args.num_parallel == 0:
        args.num_parallel = ncpus
    if args.num_parallel > ncpus:
        raise ValueError(f'refuse to run {args.num_parallel} jobs on {ncpus} CPUs')
    if args.verbosity > 1:
        if args.num_parallel > 1:
            print(f'{script}: compute {args.num_parallel} moments in parallel', file=sys.stderr)
        else:
            print(f'{script}: run in serial mode', file=sys.stderr)

    module_name = Path(args.output_folder).name
    if not module_name.isidentifier():
        raise ValueError(f'"{args.output_folder}" is not a valid path name for a Python module')
    if Path(args.output_folder).exists():
        raise ValueError(f'output folder "{args.output_folder}" exists, refuse to overwrite')

    setup_moments(args)
    if args.verbosity > 0:
        print(f'{script}: generate moments for the orders of:', file=sys.stderr)
        for m in sorted(args.moments):
            print(f'    {m}', file=sys.stderr)
        print()

    with tempfile.TemporaryDirectory() as workdir:
        output_folder = Path(workdir) / module_name
        process(args.moments, output_folder, args.num_parallel, args.verbosity)
        os.replace(output_folder, args.output_folder)
