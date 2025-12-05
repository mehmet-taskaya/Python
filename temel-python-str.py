ornek_a = "kasaba"
print(len(ornek_a)) #dize uzunluğunu verir

ornek_a = "kasaba"
print(ornek_a[1:6:2]) #dizeden belirli karakterleri alır

ornek_a = "kasaba"
print(len(ornek_a)) #dize uzunluğunu verir

print('Ali\'nin evi çok sıcak') #kaçış karakteri kullanımı(\ ile ' işaretini yazdırma)

ders1 = "matematik"
ders2 = "fizik"
print("{ikinci_ders} sınavından 90, {ilk_ders} sınavından ise 45 aldı.".format(ilk_ders = ders1, ikinci_ders = ders2)) #format metodu ile dize biçimlendirme

sayi = 90
ondalik_sayi = 4.5
kompleks_sayi = 3 + 4j
mantiksal_deger = True
print(type(sayi), type(ondalik_sayi), type(kompleks_sayi), type(mantiksal_deger))
sayi = str(sayi)
ondalik_sayi = str(ondalik_sayi)
kompleks_sayi = str(kompleks_sayi)
mantiksal_deger = str(mantiksal_deger)
print(type(sayi), type(ondalik_sayi), type(kompleks_sayi), type(mantiksal_deger)) #tür dönüşümü sonrası türler

