import math

ang = 0
sen = 0
msin = 0
maior = 0

while ang <= 90 and ang >= 0:
    sen = abs((4 * ang (180 - ang)) / (40500 -ang (180 - ang)))
    msin = math.sin(ang)

    if sen - msin > maior:
        maior = sen - msin

    ang += 1

