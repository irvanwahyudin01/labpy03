modal=100000000
bulan = 0
total_laba=0

while bulan < 8 :
    bulan += 1
    if bulan == 1 or bulan == 2 :
        laba=0
    elif bulan == 3 or bulan == 4 :
        laba= modal*0.01
    elif bulan == 5 or bulan == 6 :
        laba= modal*0.05
    elif bulan == 8 :
        laba= modal*0.03
    print("Laba bulan ke-",bulan,"sebesar : ",laba)
    total_laba+=laba
print("Total laba adalah : ",total_laba)
    