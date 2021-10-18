import random

def hely(babu):
    if 0 < babu <= 8:
        if babu % 8 == 0:
            a_oszlop_1.append(babu)
            sor_1.append(babu)
        elif babu % 7 == 0:
            b_oszlop_2.append(babu)
            sor_1.append(babu)
        elif babu % 6 == 0:
            c_oszlop_3.append(babu)
            sor_1.append(babu)
        elif babu % 5 == 0:
            d_oszlop_4.append(babu)
            sor_1.append(babu)
        elif babu % 4 == 0:
            e_oszlop_5.append(babu)
            sor_1.append(babu)
        elif babu % 3 == 0:
            f_oszlop_6.append(babu)
            sor_1.append(babu)
        elif babu % 2 == 0:
            g_oszlop_7.append(babu)
            sor_1.append(babu)
        else:
            h_oszlop_8.append(babu)
            sor_1.append(babu)
        osszes_babu.remove(babu)
    if 8 < babu <= 16:
        if babu % 8 == 0:
            a_oszlop_1.append(babu)
            sor_2.append(babu)
        elif babu % 7 == 0:
            b_oszlop_2.append(babu)
            sor_2.append(babu)
        elif babu % 6 == 0:
            c_oszlop_3.append(babu)
            sor_2.append(babu)
        elif babu % 5 == 0:
            d_oszlop_4.append(babu)
            sor_2.append(babu)
        elif babu % 4 == 0:
            e_oszlop_5.append(babu)
            sor_2.append(babu)
        elif babu % 3 == 0:
            f_oszlop_6.append(babu)
            sor_2.append(babu)
        elif babu % 2 == 0:
            g_oszlop_7.append(babu)
            sor_2.append(babu)
        else:
            h_oszlop_8.append(babu)
            sor_2.append(babu)
        osszes_babu.remove(babu)
    if 16 < babu <= 24:
        if babu % 8 == 0:
            a_oszlop_1.append(babu)
            sor_1.append(babu)
        elif babu % 7 == 0:
            b_oszlop_2.append(babu)
            sor_1.append(babu)
        elif babu % 6 == 0:
            c_oszlop_3.append(babu)
            sor_1.append(babu)
        elif babu % 5 == 0:
            d_oszlop_4.append(babu)
            sor_1.append(babu)
        elif babu % 4 == 0:
            e_oszlop_5.append(babu)
            sor_1.append(babu)
        elif babu % 3 == 0:
            f_oszlop_6.append(babu)
            sor_1.append(babu)
        elif babu % 2 == 0:
            g_oszlop_7.append(babu)
            sor_1.append(babu)
        else:
            h_oszlop_8.append(babu)
            sor_1.append(babu)
        osszes_babu.remove(babu)
    if 24 < babu <= 32:
        d_oszlop_4.append(babu)
        osszes_babu.remove(babu)
    if 32 < babu <= 40:
        e_oszlop_5.append(babu)
        osszes_babu.remove(babu)
    if 40 < babu <= 48:
        f_oszlop_6.append(babu)
        osszes_babu.remove(babu)
    if 48 < babu <= 56:
        g_oszlop_7.append(babu)
        osszes_babu.remove(babu)
    if 56 < babu <= 64:
        h_oszlop_8.append(babu)
        osszes_babu.remove(babu)



osszes_babu = []
hasznalt_babu = []
babu = 0
for babu in range(64): # összes hely
    osszes_babu.append(babu)

while len(hasznalt_babu) == 16: #16 választás random
    babu = random.choice(osszes_babu)
    osszes_babu.remove(babu)
    hasznalt_babu.append(babu)
sor_1 = []
sor_2 = []
sor_3 = []
sor_4 = []
sor_5 = []
sor_6 = []
sor_7 = []
sor_8 = []
sorok = [sor_1, sor_2, sor_3, sor_4, sor_5, sor_6, sor_7, sor_8]

a_oszlop_1 = [sorok]
b_oszlop_2 = [sorok]
c_oszlop_3 = [sorok]
d_oszlop_4 = [sorok]
e_oszlop_5 = [sorok]
f_oszlop_6 = [sorok]
g_oszlop_7 = [sorok]
h_oszlop_8 = [sorok]

for babu in hasznalt_babu:
    hely(babu)