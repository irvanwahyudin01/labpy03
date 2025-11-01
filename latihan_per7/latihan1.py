import random

print("Program menentukan acak kurang 0.5")
bil = int(input("Masukan nilai N : "))

batas = 0

while batas < bil :
    acak = random.random()
    if acak < 0.5 :
        batas += 1
        print("Nilai : ",acak)