a = "dizi"
b = "denemesi"
c = "bir"
kelimeler = [a, b, c]
print(" ".join(kelimeler))  

metin = "0123456789"
parca1 = metin[3:7]
print(f"3'ten 7'ye kadar olan sayılar {parca1} şeklinde yazılır")
parca2 = metin[5:]
print(f"5ten sonuna kadar olan sayılar {parca2} şeklinde yazılır")
parca3 = metin[1:9:2]
print(f"1den sonuna kadar ikişer artan sayılar {parca3} şeklinde yazılır")

urunA = 300
urunB = 400
kdv = 0.18
bson = urunB + (urunB * kdv)
ason = urunA + (urunA * kdv)
tercih = input("a ürünü için A, b ürünü için B yazınız: ")
if tercih == "A":
    print("ürün A KDV'li fiyatı:" + str(ason))
elif tercih == "B":
    print("ürün B KDV'li fiyatı:" + str(bson))
else:
    print("geçersiz tercih")


    