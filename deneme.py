sekiller = ["ucgen", "kare", "dikdortgen", "daire"]
harfler = ["a", "b", "c", "d", "e"]
print(f"şekiller listesi: {sekiller}")
print(f"harfler listesi: {harfler}")
sekiller.append("yamuk")
harfler.remove("c")
print(f"Güncellenmiş şekiller listesi: {sekiller}")
print(f"Güncellenmiş harfler listesi: {harfler}")
sekiller_yedek = sekiller.copy()
sekiller_yedek.sort()
print(f" şekiller listesi: {sekiller}")
print(f"Sıralanmış şekiller yedek listesi: {sekiller_yedek}")