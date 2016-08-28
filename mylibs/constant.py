# -*- coding: utf-8 -*-

#GP: Generator Polynomial, MP: Message Polynomial
GP_list = {
        7: [0, 87, 229, 146, 149, 238, 102, 21],
        10: [0, 251, 67, 46, 61, 118, 70, 64, 94, 32, 45],
        13: [0, 74, 152, 176, 100, 86, 100, 106, 104, 130, 218, 206, 140, 78],
        15: [0, 8, 183, 61, 91, 202, 37, 51, 58, 58, 237, 140, 124, 5, 99, 105],
        16: [0, 120, 104, 107, 109, 102, 161, 76, 3, 91, 191, 147, 169, 182, 194, 225, 120],
        17: [0, 43, 139, 206, 78, 43, 239, 123, 206, 214, 147, 24, 99, 150, 39, 243, 163, 136],
        18: [0, 215, 234, 158, 94, 184, 97, 118, 170, 79, 187, 152, 148, 252, 179, 5, 98, 96, 153],
        20: [0, 17, 60, 79, 50, 61, 163, 26, 187, 202, 180, 221, 225, 83, 239, 156, 164, 212, 212, 188, 190],
        22: [0, 210, 171, 247, 242, 93, 230, 14, 109, 221, 53, 200, 74, 8, 172, 98, 80, 219, 134, 160, 105, 165, 231],
        23: [0, 229, 121, 135, 48, 211, 117, 251, 126, 159, 180, 169, 152, 192, 226, 228, 218, 111, 117, 232, 87, 96, 227, 21],
        26: [0, 173, 125, 158, 2, 103, 182, 118, 17, 145, 201, 111, 28, 165, 53, 161, 21, 245, 142, 13, 102, 48, 227, 153, 145, 218, 70],
        28: [0, 168, 223, 200, 104, 224, 234, 108, 180, 110, 190, 195, 147, 205, 27, 232, 201, 21, 43, 245, 87, 42, 195, 212, 119, 242, 37, 9, 123],
        30: [0, 41, 173, 145, 152, 216, 31, 179, 182, 50, 48, 110, 86, 239, 96, 222, 125, 42, 173, 226, 193, 224, 130, 156, 37, 251, 216, 238, 40, 192, 180]
        }

        
# Error Correction Codewords per block
# [version1(level1,level2,level3,level4),
#  version2(..,..,..,..),
#   ....]
ecc_num_per_block = [
    (7, 10, 13, 17), (10, 16, 22, 28), (15, 26, 18, 22), (20, 18, 26, 16), (26, 24, 18, 22), (18, 16, 24, 28), (20, 18, 18, 26), (24, 22, 22, 26), (30, 22, 20, 24), (18, 26, 24, 28), (20, 30, 28, 24), (24, 22, 26, 28), (26, 22, 24, 22), (30, 24, 20, 24), (22, 24, 30, 24), (24, 28, 24, 30), (28, 28, 28, 28), (30, 26, 28, 28), (28, 26, 26, 26), (28, 26, 30, 28), (28, 26, 28, 30), (28, 28, 30, 24), (30, 28, 30, 30), (30, 28, 30, 30), (26, 28, 30, 30), (28, 28, 28, 30), (30, 28, 30, 30), (30, 28, 30, 30), (30, 28, 30, 30), (30, 28, 30, 30), (30, 28, 30, 30), (30, 28, 30, 30), (30, 28, 30, 30), (30, 28, 30, 30), (30, 28, 30, 30), (30, 28, 30, 30), (30, 28, 30, 30), (30, 28, 30, 30), (30, 28, 30, 30), (30, 28, 30, 30)
    ]
 
 
# character capacities
# {level1: [version1(mode1,mode2,mode3,mode4), version2(..,..,..,..), ...],
#   level2: [version1(mode1,mode2,mode3,mode4), version2(..,..,..,..),...],
#   ...}
char_cap = {
        'L': [(41, 25, 17, 10), (77, 47, 32, 20), (127, 77, 53, 32), (187, 114, 78, 48), (255, 154, 106, 65), (322, 195, 134, 82), (370, 224, 154, 95), (461, 279, 192, 118), (552, 335, 230, 141), (652, 395, 271, 167), (772, 468, 321, 198), (883, 535, 367, 226), (1022, 619, 425, 262), (1101, 667, 458, 282), (1250, 758, 520, 320), (1408, 854, 586, 361), (1548, 938, 644, 397), (1725, 1046, 718, 442), (1903, 1153, 792, 488), (2061, 1249, 858, 528), (2232, 1352, 929, 572), (2409, 1460, 1003, 618), (2620, 1588, 1091, 672), (2812, 1704, 1171, 721), (3057, 1853, 1273, 784), (3283, 1990, 1367, 842), (3517, 2132, 1465, 902), (3669, 2223, 1528, 940), (3909, 2369, 1628, 1002), (4158, 2520, 1732, 1066), (4417, 2677, 1840, 1132), (4686, 2840, 1952, 1201), (4965, 3009, 2068, 1273), (5253, 3183, 2188, 1347), (5529, 3351, 2303, 1417), (5836, 3537, 2431, 1496), (6153, 3729, 2563, 1577), (6479, 3927, 2699, 1661), (6743, 4087, 2809, 1729), (7089, 4296, 2953, 1817)],
        'M': [(34, 20, 14, 8), (63, 38, 26, 16), (101, 61, 42, 26), (149, 90, 62, 38), (202, 122, 84, 52), (255, 154, 106, 65), (293, 178, 122, 75), (365, 221, 152, 93), (432, 262, 180, 111), (513, 311, 213, 131), (604, 366, 251, 155), (691, 419, 287, 177), (796, 483, 331, 204), (871, 528, 362, 223), (991, 600, 412, 254), (1082, 656, 450, 277), (1212, 734, 504, 310), (1346, 816, 560, 345), (1500, 909, 624, 384), (1600, 970, 666, 410), (1708, 1035, 711, 438), (1872, 1134, 779, 480), (2059, 1248, 857, 528), (2188, 1326, 911, 561), (2395, 1451, 997, 614), (2544, 1542, 1059, 652), (2701, 1637, 1125, 692), (2857, 1732, 1190, 732), (3035, 1839, 1264, 778), (3289, 1994, 1370, 843), (3486, 2113, 1452, 894), (3693, 2238, 1538, 947), (3909, 2369, 1628, 1002), (4134, 2506, 1722, 1060), (4343, 2632, 1809, 1113), (4588, 2780, 1911, 1176), (4775, 2894, 1989, 1224), (5039, 3054, 2099, 1292), (5313, 3220, 2213, 1362), (5596, 3391, 2331, 1435)],
        'Q': [(27, 16, 11, 7), (48, 29, 20, 12), (77, 47, 32, 20), (111, 67, 46, 28), (144, 87, 60, 37), (178, 108, 74, 45), (207, 125, 86, 53), (259, 157, 108, 66), (312, 189, 130, 80), (364, 221, 151, 93), (427, 259, 177, 109), (489, 296, 203, 125), (580, 352, 241, 149), (621, 376, 258, 159), (703, 426, 292, 180), (775, 470, 322, 198), (876, 531, 364, 224), (948, 574, 394, 243), (1063, 644, 442, 272), (1159, 702, 482, 297), (1224, 742, 509, 314), (1358, 823, 565, 348), (1468, 890, 611, 376), (1588, 963, 661, 407), (1718, 1041, 715, 440), (1804, 1094, 751, 462), (1933, 1172, 805, 496), (2085, 1263, 868, 534), (2181, 1322, 908, 559), (2358, 1429, 982, 604), (2473, 1499, 1030, 634), (2670, 1618, 1112, 684), (2805, 1700, 1168, 719), (2949, 1787, 1228, 756), (3081, 1867, 1283, 790), (3244, 1966, 1351, 832), (3417, 2071, 1423, 876), (3599, 2181, 1499, 923), (3791, 2298, 1579, 972), (3993, 2420, 1663, 1024)],
        'H': [(17, 10, 7, 4), (34, 20, 14, 8), (58, 35, 24, 15), (82, 50, 34, 21), (106, 64, 44, 27), (139, 84, 58, 36), (154, 93, 64, 39), (202, 122, 84, 52), (235, 143, 98, 60), (288, 174, 119, 74), (331, 200, 137, 85), (374, 227, 155, 96), (427, 259, 177, 109), (468, 283, 194, 120), (530, 321, 220, 136), (602, 365, 250, 154), (674, 408, 280, 173), (746, 452, 310, 191), (813, 493, 338, 208), (919, 557, 382, 235), (969, 587, 403, 248), (1056, 640, 439, 270), (1108, 672, 461, 284), (1228, 744, 511, 315), (1286, 779, 535, 330), (1425, 864, 593, 365), (1501, 910, 625, 385), (1581, 958, 658, 405), (1677, 1016, 698, 430), (1782, 1080, 742, 457), (1897, 1150, 790, 486), (2022, 1226, 842, 518), (2157, 1307, 898, 553), (2301, 1394, 958, 590), (2361, 1431, 983, 605), (2524, 1530, 1051, 647), (2625, 1591, 1093, 673), (2735, 1658, 1139, 701), (2927, 1774, 1219, 750), (3057, 1852, 1273, 784)]
        }

        
# [
# version1[level1,level2,level3,level4], 
# version2[..,..,..,..],
# ...
#   ]
required_bytes = [
        [19, 16, 13, 9], [34, 28, 22, 16], [55, 44, 34, 26], [80, 64, 48, 36], [108, 86, 62, 46], [136, 108, 76, 60], [156, 124, 88, 66], [194, 154, 110, 86], [232, 182, 132, 100], [274, 216, 154, 122], [324, 254, 180, 140], [370, 290, 206, 158], [428, 334, 244, 180], [461, 365, 261, 197], [523, 415, 295, 223], [589, 453, 325, 253], [647, 507, 367, 283], [721, 563, 397, 313], [795, 627, 445, 341], [861, 669, 485, 385], [932, 714, 512, 406], [1006, 782, 568, 442], [1094, 860, 614, 464], [1174, 914, 664, 514], [1276, 1000, 718, 538], [1370, 1062, 754, 596], [1468, 1128, 808, 628], [1531, 1193, 871, 661], [1631, 1267, 911, 701], [1735, 1373, 985, 745], [1843, 1455, 1033, 793], [1955, 1541, 1115, 845], [2071, 1631, 1171, 901], [2191, 1725, 1231, 961], [2306, 1812, 1286, 986], [2434, 1914, 1354, 1054], [2566, 1992, 1426, 1096], [2702, 2102, 1502, 1142], [2812, 2216, 1582, 1222], [2956, 2334, 1666, 1276]
        ]

        
# [
# version1[
#       level1(num_of_group_1_blocks, DC_per_group_1_block, num_of_group_2_blocks, DC_per_group_2_block),
#       level2(..,..,..,..),
#       level3(..,..,..,..),
#       level4(..,..,..,..)
#       ], 
# version2[level1(..), level2(..), level3(..), level4(..)],
# ...
#   ]
grouping_list = [
    [(1, 19, 0, 0), (1, 16, 0, 0), (1, 13, 0, 0), (1, 9, 0, 0)], [(1, 34, 0, 0), (1, 28, 0, 0), (1, 22, 0, 0), (1, 16, 0, 0)], [(1, 55, 0, 0), (1, 44, 0, 0), (2, 17, 0, 0), (2, 13, 0, 0)], [(1, 80, 0, 0), (2, 32, 0, 0), (2, 24, 0, 0), (4, 9, 0, 0)], [(1, 108, 0, 0), (2, 43, 0, 0), (2, 15, 2, 16), (2, 11, 2, 12)], [(2, 68, 0, 0), (4, 27, 0, 0), (4, 19, 0, 0), (4, 15, 0, 0)], [(2, 78, 0, 0), (4, 31, 0, 0), (2, 14, 4, 15), (4, 13, 1, 14)], [(2, 97, 0, 0), (2, 38, 2, 39), (4, 18, 2, 19), (4, 14, 2, 15)], [(2, 116, 0, 0), (3, 36, 2, 37), (4, 16, 4, 17), (4, 12, 4, 13)], [(2, 68, 2, 69), (4, 43, 1, 44), (6, 19, 2, 20), (6, 15, 2, 16)], [(4, 81, 0, 0), (1, 50, 4, 51), (4, 22, 4, 23), (3, 12, 8, 13)], [(2, 92, 2, 93), (6, 36, 2, 37), (4, 20, 6, 21), (7, 14, 4, 15)], [(4, 107, 0, 0), (8, 37, 1, 38), (8, 20, 4, 21), (12, 11, 4, 12)], [(3, 115, 1, 116), (4, 40, 5, 41), (11, 16, 5, 17), (11, 12, 5, 13)], [(5, 87, 1, 88), (5, 41, 5, 42), (5, 24, 7, 25), (11, 12, 7, 13)], [(5, 98, 1, 99), (7, 45, 3, 46), (15, 19, 2, 20), (3, 15, 13, 16)], [(1, 107, 5, 108), (10, 46, 1, 47), (1, 22, 15, 23), (2, 14, 17, 15)], [(5, 120, 1, 121), (9, 43, 4, 44), (17, 22, 1, 23), (2, 14, 19, 15)], [(3, 113, 4, 114), (3, 44, 11, 45), (17, 21, 4, 22), (9, 13, 16, 14)], [(3, 107, 5, 108), (3, 41, 13, 42), (15, 24, 5, 25), (15, 15, 10, 16)], [(4, 116, 4, 117), (17, 42, 0, 0), (17, 22, 6, 23), (19, 16, 6, 17)], [(2, 111, 7, 112), (17, 46, 0, 0), (7, 24, 16, 25), (34, 13, 0, 0)], [(4, 121, 5, 122), (4, 47, 14, 48), (11, 24, 14, 25), (16, 15, 14, 16)], [(6, 117, 4, 118), (6, 45, 14, 46), (11, 24, 16, 25), (30, 16, 2, 17)], [(8, 106, 4, 107), (8, 47, 13, 48), (7, 24, 22, 25), (22, 15, 13, 16)], [(10, 114, 2, 115), (19, 46, 4, 47), (28, 22, 6, 23), (33, 16, 4, 17)], [(8, 122, 4, 123), (22, 45, 3, 46), (8, 23, 26, 24), (12, 15, 28, 16)], [(3, 117, 10, 118), (3, 45, 23, 46), (4, 24, 31, 25), (11, 15, 31, 16)], [(7, 116, 7, 117), (21, 45, 7, 46), (1, 23, 37, 24), (19, 15, 26, 16)], [(5, 115, 10, 116), (19, 47, 10, 48), (15, 24, 25, 25), (23, 15, 25, 16)], [(13, 115, 3, 116), (2, 46, 29, 47), (42, 24, 1, 25), (23, 15, 28, 16)], [(17, 115, 0, 0), (10, 46, 23, 47), (10, 24, 35, 25), (19, 15, 35, 16)], [(17, 115, 1, 116), (14, 46, 21, 47), (29, 24, 19, 25), (11, 15, 46, 16)], [(13, 115, 6, 116), (14, 46, 23, 47), (44, 24, 7, 25), (59, 16, 1, 17)], [(12, 121, 7, 122), (12, 47, 26, 48), (39, 24, 14, 25), (22, 15, 41, 16)], [(6, 121, 14, 122), (6, 47, 34, 48), (46, 24, 10, 25), (2, 15, 64, 16)], [(17, 122, 4, 123), (29, 46, 14, 47), (49, 24, 10, 25), (24, 15, 46, 16)], [(4, 122, 18, 123), (13, 46, 32, 47), (48, 24, 14, 25), (42, 15, 32, 16)], [(20, 117, 4, 118), (40, 47, 7, 48), (43, 24, 22, 25), (10, 15, 67, 16)], [(19, 118, 6, 119), (18, 47, 31, 48), (34, 24, 34, 25), (20, 15, 61, 16)]
    ]
        
mode_indicator = {'numeric': '0001', 'alphanumeric': '0010', 'byte': '0100', 'kanji': '1000'}

num_list = '0123456789'
alphanum_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:'

mindex = {'numeric':0, 'alphanumeric':1, 'byte':2, 'kanji':3}
lindex = {'L':0, 'M':1, 'Q':2, 'H':3}

required_remainder_bits = (0,7,7,7,7,7,0,0,0,0,0,0,0,3,3,3,3,3,3,3,4,4,4,4,4,4,4,3,3,3,3,3,3,3,0,0,0,0,0,0)