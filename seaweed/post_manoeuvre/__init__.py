# This is a generated file. Do not edit. Run:
#     scripts/post-manoeuvre-moments.sage.py -vv --output-folder ../Downloads/post_manoeuvre -N 5 --num-parallel=0
# to recreate, then copy the corresponding "__init__.py" file on top of this one.

from .impl import moment_1000, latex_1000
from .impl import moment_0100, latex_0100
from .impl import moment_0010, latex_0010
from .impl import moment_0001, latex_0001
from .impl import moment_2000, latex_2000
from .impl import moment_1100, latex_1100
from .impl import moment_1010, latex_1010
from .impl import moment_1001, latex_1001
from .impl import moment_0200, latex_0200
from .impl import moment_0110, latex_0110
from .impl import moment_0101, latex_0101
from .impl import moment_0020, latex_0020
from .impl import moment_0011, latex_0011
from .impl import moment_0002, latex_0002
from .impl import moment_3000, latex_3000
from .impl import moment_2100, latex_2100
from .impl import moment_2010, latex_2010
from .impl import moment_2001, latex_2001
from .impl import moment_1200, latex_1200
from .impl import moment_1110, latex_1110
from .impl import moment_1101, latex_1101
from .impl import moment_1020, latex_1020
from .impl import moment_1011, latex_1011
from .impl import moment_1002, latex_1002
from .impl import moment_0300, latex_0300
from .impl import moment_0210, latex_0210
from .impl import moment_0201, latex_0201
from .impl import moment_0120, latex_0120
from .impl import moment_0111, latex_0111
from .impl import moment_0102, latex_0102
from .impl import moment_0030, latex_0030
from .impl import moment_0021, latex_0021
from .impl import moment_0012, latex_0012
from .impl import moment_0003, latex_0003
from .impl import moment_4000, latex_4000
from .impl import moment_3100, latex_3100
from .impl import moment_3010, latex_3010
from .impl import moment_3001, latex_3001
from .impl import moment_2200, latex_2200
from .impl import moment_2110, latex_2110
from .impl import moment_2101, latex_2101
from .impl import moment_2020, latex_2020
from .impl import moment_2011, latex_2011
from .impl import moment_2002, latex_2002
from .impl import moment_1300, latex_1300
from .impl import moment_1210, latex_1210
from .impl import moment_1201, latex_1201
from .impl import moment_1120, latex_1120
from .impl import moment_1111, latex_1111
from .impl import moment_1102, latex_1102
from .impl import moment_1030, latex_1030
from .impl import moment_1021, latex_1021
from .impl import moment_1012, latex_1012
from .impl import moment_1003, latex_1003
from .impl import moment_0400, latex_0400
from .impl import moment_0310, latex_0310
from .impl import moment_0301, latex_0301
from .impl import moment_0220, latex_0220
from .impl import moment_0211, latex_0211
from .impl import moment_0202, latex_0202
from .impl import moment_0130, latex_0130
from .impl import moment_0121, latex_0121
from .impl import moment_0112, latex_0112
from .impl import moment_0103, latex_0103
from .impl import moment_0040, latex_0040
from .impl import moment_0031, latex_0031
from .impl import moment_0022, latex_0022
from .impl import moment_0013, latex_0013
from .impl import moment_0004, latex_0004
from .impl import moment_5000, latex_5000
from .impl import moment_4100, latex_4100
from .impl import moment_4010, latex_4010
from .impl import moment_4001, latex_4001
from .impl import moment_3200, latex_3200
from .impl import moment_3110, latex_3110
from .impl import moment_3101, latex_3101
from .impl import moment_3020, latex_3020
from .impl import moment_3011, latex_3011
from .impl import moment_3002, latex_3002
from .impl import moment_2300, latex_2300
from .impl import moment_2210, latex_2210
from .impl import moment_2201, latex_2201
from .impl import moment_2120, latex_2120
from .impl import moment_2111, latex_2111
from .impl import moment_2102, latex_2102
from .impl import moment_2030, latex_2030
from .impl import moment_2021, latex_2021
from .impl import moment_2012, latex_2012
from .impl import moment_2003, latex_2003
from .impl import moment_1400, latex_1400
from .impl import moment_1310, latex_1310
from .impl import moment_1301, latex_1301
from .impl import moment_1220, latex_1220
from .impl import moment_1211, latex_1211
from .impl import moment_1202, latex_1202
from .impl import moment_1130, latex_1130
from .impl import moment_1121, latex_1121
from .impl import moment_1112, latex_1112
from .impl import moment_1103, latex_1103
from .impl import moment_1040, latex_1040
from .impl import moment_1031, latex_1031
from .impl import moment_1022, latex_1022
from .impl import moment_1013, latex_1013
from .impl import moment_1004, latex_1004
from .impl import moment_0500, latex_0500
from .impl import moment_0410, latex_0410
from .impl import moment_0401, latex_0401
from .impl import moment_0320, latex_0320
from .impl import moment_0311, latex_0311
from .impl import moment_0302, latex_0302
from .impl import moment_0230, latex_0230
from .impl import moment_0221, latex_0221
from .impl import moment_0212, latex_0212
from .impl import moment_0203, latex_0203
from .impl import moment_0140, latex_0140
from .impl import moment_0131, latex_0131
from .impl import moment_0122, latex_0122
from .impl import moment_0113, latex_0113
from .impl import moment_0104, latex_0104
from .impl import moment_0050, latex_0050
from .impl import moment_0041, latex_0041
from .impl import moment_0032, latex_0032
from .impl import moment_0023, latex_0023
from .impl import moment_0014, latex_0014
from .impl import moment_0005, latex_0005


orders = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [2, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 2, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 2, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 2],
    [3, 0, 0, 0],
    [2, 1, 0, 0],
    [2, 0, 1, 0],
    [2, 0, 0, 1],
    [1, 2, 0, 0],
    [1, 1, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 2, 0],
    [1, 0, 1, 1],
    [1, 0, 0, 2],
    [0, 3, 0, 0],
    [0, 2, 1, 0],
    [0, 2, 0, 1],
    [0, 1, 2, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 2],
    [0, 0, 3, 0],
    [0, 0, 2, 1],
    [0, 0, 1, 2],
    [0, 0, 0, 3],
    [4, 0, 0, 0],
    [3, 1, 0, 0],
    [3, 0, 1, 0],
    [3, 0, 0, 1],
    [2, 2, 0, 0],
    [2, 1, 1, 0],
    [2, 1, 0, 1],
    [2, 0, 2, 0],
    [2, 0, 1, 1],
    [2, 0, 0, 2],
    [1, 3, 0, 0],
    [1, 2, 1, 0],
    [1, 2, 0, 1],
    [1, 1, 2, 0],
    [1, 1, 1, 1],
    [1, 1, 0, 2],
    [1, 0, 3, 0],
    [1, 0, 2, 1],
    [1, 0, 1, 2],
    [1, 0, 0, 3],
    [0, 4, 0, 0],
    [0, 3, 1, 0],
    [0, 3, 0, 1],
    [0, 2, 2, 0],
    [0, 2, 1, 1],
    [0, 2, 0, 2],
    [0, 1, 3, 0],
    [0, 1, 2, 1],
    [0, 1, 1, 2],
    [0, 1, 0, 3],
    [0, 0, 4, 0],
    [0, 0, 3, 1],
    [0, 0, 2, 2],
    [0, 0, 1, 3],
    [0, 0, 0, 4],
    [5, 0, 0, 0],
    [4, 1, 0, 0],
    [4, 0, 1, 0],
    [4, 0, 0, 1],
    [3, 2, 0, 0],
    [3, 1, 1, 0],
    [3, 1, 0, 1],
    [3, 0, 2, 0],
    [3, 0, 1, 1],
    [3, 0, 0, 2],
    [2, 3, 0, 0],
    [2, 2, 1, 0],
    [2, 2, 0, 1],
    [2, 1, 2, 0],
    [2, 1, 1, 1],
    [2, 1, 0, 2],
    [2, 0, 3, 0],
    [2, 0, 2, 1],
    [2, 0, 1, 2],
    [2, 0, 0, 3],
    [1, 4, 0, 0],
    [1, 3, 1, 0],
    [1, 3, 0, 1],
    [1, 2, 2, 0],
    [1, 2, 1, 1],
    [1, 2, 0, 2],
    [1, 1, 3, 0],
    [1, 1, 2, 1],
    [1, 1, 1, 2],
    [1, 1, 0, 3],
    [1, 0, 4, 0],
    [1, 0, 3, 1],
    [1, 0, 2, 2],
    [1, 0, 1, 3],
    [1, 0, 0, 4],
    [0, 5, 0, 0],
    [0, 4, 1, 0],
    [0, 4, 0, 1],
    [0, 3, 2, 0],
    [0, 3, 1, 1],
    [0, 3, 0, 2],
    [0, 2, 3, 0],
    [0, 2, 2, 1],
    [0, 2, 1, 2],
    [0, 2, 0, 3],
    [0, 1, 4, 0],
    [0, 1, 3, 1],
    [0, 1, 2, 2],
    [0, 1, 1, 3],
    [0, 1, 0, 4],
    [0, 0, 5, 0],
    [0, 0, 4, 1],
    [0, 0, 3, 2],
    [0, 0, 2, 3],
    [0, 0, 1, 4],
    [0, 0, 0, 5],
]

_moments = {}
_latexs = {}

_moments[(1, 0, 0, 0)] = moment_1000
_latexs[(1, 0, 0, 0)] = latex_1000

_moments[(0, 1, 0, 0)] = moment_0100
_latexs[(0, 1, 0, 0)] = latex_0100

_moments[(0, 0, 1, 0)] = moment_0010
_latexs[(0, 0, 1, 0)] = latex_0010

_moments[(0, 0, 0, 1)] = moment_0001
_latexs[(0, 0, 0, 1)] = latex_0001

_moments[(2, 0, 0, 0)] = moment_2000
_latexs[(2, 0, 0, 0)] = latex_2000

_moments[(1, 1, 0, 0)] = moment_1100
_latexs[(1, 1, 0, 0)] = latex_1100

_moments[(1, 0, 1, 0)] = moment_1010
_latexs[(1, 0, 1, 0)] = latex_1010

_moments[(1, 0, 0, 1)] = moment_1001
_latexs[(1, 0, 0, 1)] = latex_1001

_moments[(0, 2, 0, 0)] = moment_0200
_latexs[(0, 2, 0, 0)] = latex_0200

_moments[(0, 1, 1, 0)] = moment_0110
_latexs[(0, 1, 1, 0)] = latex_0110

_moments[(0, 1, 0, 1)] = moment_0101
_latexs[(0, 1, 0, 1)] = latex_0101

_moments[(0, 0, 2, 0)] = moment_0020
_latexs[(0, 0, 2, 0)] = latex_0020

_moments[(0, 0, 1, 1)] = moment_0011
_latexs[(0, 0, 1, 1)] = latex_0011

_moments[(0, 0, 0, 2)] = moment_0002
_latexs[(0, 0, 0, 2)] = latex_0002

_moments[(3, 0, 0, 0)] = moment_3000
_latexs[(3, 0, 0, 0)] = latex_3000

_moments[(2, 1, 0, 0)] = moment_2100
_latexs[(2, 1, 0, 0)] = latex_2100

_moments[(2, 0, 1, 0)] = moment_2010
_latexs[(2, 0, 1, 0)] = latex_2010

_moments[(2, 0, 0, 1)] = moment_2001
_latexs[(2, 0, 0, 1)] = latex_2001

_moments[(1, 2, 0, 0)] = moment_1200
_latexs[(1, 2, 0, 0)] = latex_1200

_moments[(1, 1, 1, 0)] = moment_1110
_latexs[(1, 1, 1, 0)] = latex_1110

_moments[(1, 1, 0, 1)] = moment_1101
_latexs[(1, 1, 0, 1)] = latex_1101

_moments[(1, 0, 2, 0)] = moment_1020
_latexs[(1, 0, 2, 0)] = latex_1020

_moments[(1, 0, 1, 1)] = moment_1011
_latexs[(1, 0, 1, 1)] = latex_1011

_moments[(1, 0, 0, 2)] = moment_1002
_latexs[(1, 0, 0, 2)] = latex_1002

_moments[(0, 3, 0, 0)] = moment_0300
_latexs[(0, 3, 0, 0)] = latex_0300

_moments[(0, 2, 1, 0)] = moment_0210
_latexs[(0, 2, 1, 0)] = latex_0210

_moments[(0, 2, 0, 1)] = moment_0201
_latexs[(0, 2, 0, 1)] = latex_0201

_moments[(0, 1, 2, 0)] = moment_0120
_latexs[(0, 1, 2, 0)] = latex_0120

_moments[(0, 1, 1, 1)] = moment_0111
_latexs[(0, 1, 1, 1)] = latex_0111

_moments[(0, 1, 0, 2)] = moment_0102
_latexs[(0, 1, 0, 2)] = latex_0102

_moments[(0, 0, 3, 0)] = moment_0030
_latexs[(0, 0, 3, 0)] = latex_0030

_moments[(0, 0, 2, 1)] = moment_0021
_latexs[(0, 0, 2, 1)] = latex_0021

_moments[(0, 0, 1, 2)] = moment_0012
_latexs[(0, 0, 1, 2)] = latex_0012

_moments[(0, 0, 0, 3)] = moment_0003
_latexs[(0, 0, 0, 3)] = latex_0003

_moments[(4, 0, 0, 0)] = moment_4000
_latexs[(4, 0, 0, 0)] = latex_4000

_moments[(3, 1, 0, 0)] = moment_3100
_latexs[(3, 1, 0, 0)] = latex_3100

_moments[(3, 0, 1, 0)] = moment_3010
_latexs[(3, 0, 1, 0)] = latex_3010

_moments[(3, 0, 0, 1)] = moment_3001
_latexs[(3, 0, 0, 1)] = latex_3001

_moments[(2, 2, 0, 0)] = moment_2200
_latexs[(2, 2, 0, 0)] = latex_2200

_moments[(2, 1, 1, 0)] = moment_2110
_latexs[(2, 1, 1, 0)] = latex_2110

_moments[(2, 1, 0, 1)] = moment_2101
_latexs[(2, 1, 0, 1)] = latex_2101

_moments[(2, 0, 2, 0)] = moment_2020
_latexs[(2, 0, 2, 0)] = latex_2020

_moments[(2, 0, 1, 1)] = moment_2011
_latexs[(2, 0, 1, 1)] = latex_2011

_moments[(2, 0, 0, 2)] = moment_2002
_latexs[(2, 0, 0, 2)] = latex_2002

_moments[(1, 3, 0, 0)] = moment_1300
_latexs[(1, 3, 0, 0)] = latex_1300

_moments[(1, 2, 1, 0)] = moment_1210
_latexs[(1, 2, 1, 0)] = latex_1210

_moments[(1, 2, 0, 1)] = moment_1201
_latexs[(1, 2, 0, 1)] = latex_1201

_moments[(1, 1, 2, 0)] = moment_1120
_latexs[(1, 1, 2, 0)] = latex_1120

_moments[(1, 1, 1, 1)] = moment_1111
_latexs[(1, 1, 1, 1)] = latex_1111

_moments[(1, 1, 0, 2)] = moment_1102
_latexs[(1, 1, 0, 2)] = latex_1102

_moments[(1, 0, 3, 0)] = moment_1030
_latexs[(1, 0, 3, 0)] = latex_1030

_moments[(1, 0, 2, 1)] = moment_1021
_latexs[(1, 0, 2, 1)] = latex_1021

_moments[(1, 0, 1, 2)] = moment_1012
_latexs[(1, 0, 1, 2)] = latex_1012

_moments[(1, 0, 0, 3)] = moment_1003
_latexs[(1, 0, 0, 3)] = latex_1003

_moments[(0, 4, 0, 0)] = moment_0400
_latexs[(0, 4, 0, 0)] = latex_0400

_moments[(0, 3, 1, 0)] = moment_0310
_latexs[(0, 3, 1, 0)] = latex_0310

_moments[(0, 3, 0, 1)] = moment_0301
_latexs[(0, 3, 0, 1)] = latex_0301

_moments[(0, 2, 2, 0)] = moment_0220
_latexs[(0, 2, 2, 0)] = latex_0220

_moments[(0, 2, 1, 1)] = moment_0211
_latexs[(0, 2, 1, 1)] = latex_0211

_moments[(0, 2, 0, 2)] = moment_0202
_latexs[(0, 2, 0, 2)] = latex_0202

_moments[(0, 1, 3, 0)] = moment_0130
_latexs[(0, 1, 3, 0)] = latex_0130

_moments[(0, 1, 2, 1)] = moment_0121
_latexs[(0, 1, 2, 1)] = latex_0121

_moments[(0, 1, 1, 2)] = moment_0112
_latexs[(0, 1, 1, 2)] = latex_0112

_moments[(0, 1, 0, 3)] = moment_0103
_latexs[(0, 1, 0, 3)] = latex_0103

_moments[(0, 0, 4, 0)] = moment_0040
_latexs[(0, 0, 4, 0)] = latex_0040

_moments[(0, 0, 3, 1)] = moment_0031
_latexs[(0, 0, 3, 1)] = latex_0031

_moments[(0, 0, 2, 2)] = moment_0022
_latexs[(0, 0, 2, 2)] = latex_0022

_moments[(0, 0, 1, 3)] = moment_0013
_latexs[(0, 0, 1, 3)] = latex_0013

_moments[(0, 0, 0, 4)] = moment_0004
_latexs[(0, 0, 0, 4)] = latex_0004

_moments[(5, 0, 0, 0)] = moment_5000
_latexs[(5, 0, 0, 0)] = latex_5000

_moments[(4, 1, 0, 0)] = moment_4100
_latexs[(4, 1, 0, 0)] = latex_4100

_moments[(4, 0, 1, 0)] = moment_4010
_latexs[(4, 0, 1, 0)] = latex_4010

_moments[(4, 0, 0, 1)] = moment_4001
_latexs[(4, 0, 0, 1)] = latex_4001

_moments[(3, 2, 0, 0)] = moment_3200
_latexs[(3, 2, 0, 0)] = latex_3200

_moments[(3, 1, 1, 0)] = moment_3110
_latexs[(3, 1, 1, 0)] = latex_3110

_moments[(3, 1, 0, 1)] = moment_3101
_latexs[(3, 1, 0, 1)] = latex_3101

_moments[(3, 0, 2, 0)] = moment_3020
_latexs[(3, 0, 2, 0)] = latex_3020

_moments[(3, 0, 1, 1)] = moment_3011
_latexs[(3, 0, 1, 1)] = latex_3011

_moments[(3, 0, 0, 2)] = moment_3002
_latexs[(3, 0, 0, 2)] = latex_3002

_moments[(2, 3, 0, 0)] = moment_2300
_latexs[(2, 3, 0, 0)] = latex_2300

_moments[(2, 2, 1, 0)] = moment_2210
_latexs[(2, 2, 1, 0)] = latex_2210

_moments[(2, 2, 0, 1)] = moment_2201
_latexs[(2, 2, 0, 1)] = latex_2201

_moments[(2, 1, 2, 0)] = moment_2120
_latexs[(2, 1, 2, 0)] = latex_2120

_moments[(2, 1, 1, 1)] = moment_2111
_latexs[(2, 1, 1, 1)] = latex_2111

_moments[(2, 1, 0, 2)] = moment_2102
_latexs[(2, 1, 0, 2)] = latex_2102

_moments[(2, 0, 3, 0)] = moment_2030
_latexs[(2, 0, 3, 0)] = latex_2030

_moments[(2, 0, 2, 1)] = moment_2021
_latexs[(2, 0, 2, 1)] = latex_2021

_moments[(2, 0, 1, 2)] = moment_2012
_latexs[(2, 0, 1, 2)] = latex_2012

_moments[(2, 0, 0, 3)] = moment_2003
_latexs[(2, 0, 0, 3)] = latex_2003

_moments[(1, 4, 0, 0)] = moment_1400
_latexs[(1, 4, 0, 0)] = latex_1400

_moments[(1, 3, 1, 0)] = moment_1310
_latexs[(1, 3, 1, 0)] = latex_1310

_moments[(1, 3, 0, 1)] = moment_1301
_latexs[(1, 3, 0, 1)] = latex_1301

_moments[(1, 2, 2, 0)] = moment_1220
_latexs[(1, 2, 2, 0)] = latex_1220

_moments[(1, 2, 1, 1)] = moment_1211
_latexs[(1, 2, 1, 1)] = latex_1211

_moments[(1, 2, 0, 2)] = moment_1202
_latexs[(1, 2, 0, 2)] = latex_1202

_moments[(1, 1, 3, 0)] = moment_1130
_latexs[(1, 1, 3, 0)] = latex_1130

_moments[(1, 1, 2, 1)] = moment_1121
_latexs[(1, 1, 2, 1)] = latex_1121

_moments[(1, 1, 1, 2)] = moment_1112
_latexs[(1, 1, 1, 2)] = latex_1112

_moments[(1, 1, 0, 3)] = moment_1103
_latexs[(1, 1, 0, 3)] = latex_1103

_moments[(1, 0, 4, 0)] = moment_1040
_latexs[(1, 0, 4, 0)] = latex_1040

_moments[(1, 0, 3, 1)] = moment_1031
_latexs[(1, 0, 3, 1)] = latex_1031

_moments[(1, 0, 2, 2)] = moment_1022
_latexs[(1, 0, 2, 2)] = latex_1022

_moments[(1, 0, 1, 3)] = moment_1013
_latexs[(1, 0, 1, 3)] = latex_1013

_moments[(1, 0, 0, 4)] = moment_1004
_latexs[(1, 0, 0, 4)] = latex_1004

_moments[(0, 5, 0, 0)] = moment_0500
_latexs[(0, 5, 0, 0)] = latex_0500

_moments[(0, 4, 1, 0)] = moment_0410
_latexs[(0, 4, 1, 0)] = latex_0410

_moments[(0, 4, 0, 1)] = moment_0401
_latexs[(0, 4, 0, 1)] = latex_0401

_moments[(0, 3, 2, 0)] = moment_0320
_latexs[(0, 3, 2, 0)] = latex_0320

_moments[(0, 3, 1, 1)] = moment_0311
_latexs[(0, 3, 1, 1)] = latex_0311

_moments[(0, 3, 0, 2)] = moment_0302
_latexs[(0, 3, 0, 2)] = latex_0302

_moments[(0, 2, 3, 0)] = moment_0230
_latexs[(0, 2, 3, 0)] = latex_0230

_moments[(0, 2, 2, 1)] = moment_0221
_latexs[(0, 2, 2, 1)] = latex_0221

_moments[(0, 2, 1, 2)] = moment_0212
_latexs[(0, 2, 1, 2)] = latex_0212

_moments[(0, 2, 0, 3)] = moment_0203
_latexs[(0, 2, 0, 3)] = latex_0203

_moments[(0, 1, 4, 0)] = moment_0140
_latexs[(0, 1, 4, 0)] = latex_0140

_moments[(0, 1, 3, 1)] = moment_0131
_latexs[(0, 1, 3, 1)] = latex_0131

_moments[(0, 1, 2, 2)] = moment_0122
_latexs[(0, 1, 2, 2)] = latex_0122

_moments[(0, 1, 1, 3)] = moment_0113
_latexs[(0, 1, 1, 3)] = latex_0113

_moments[(0, 1, 0, 4)] = moment_0104
_latexs[(0, 1, 0, 4)] = latex_0104

_moments[(0, 0, 5, 0)] = moment_0050
_latexs[(0, 0, 5, 0)] = latex_0050

_moments[(0, 0, 4, 1)] = moment_0041
_latexs[(0, 0, 4, 1)] = latex_0041

_moments[(0, 0, 3, 2)] = moment_0032
_latexs[(0, 0, 3, 2)] = latex_0032

_moments[(0, 0, 2, 3)] = moment_0023
_latexs[(0, 0, 2, 3)] = latex_0023

_moments[(0, 0, 1, 4)] = moment_0014
_latexs[(0, 0, 1, 4)] = latex_0014

_moments[(0, 0, 0, 5)] = moment_0005
_latexs[(0, 0, 0, 5)] = latex_0005


def moment(orders):
    return _moments[tuple(orders)]


def latex(orders):
    return _latexs[tuple(orders)]

def get_orders_n(n, orders, what):
    orders_n = {}
    for o in orders:
        if sum(o) == n:
            if what == "python":
                orders_n[tuple(o)] = _moments[tuple(o)]
            elif what == "latex":
                orders_n[tuple(o)] = _latexs[tuple(o)]
            else:
                raise ValueError(f"unknown argument {what}, not one of [python, latex]")
    return orders_n
