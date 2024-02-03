sozluk = {
    "Esef" : "Olmaması, yapılmaması gereken veya yapılmayan bir şey için duyulan üzüntü",
    "Emin" : "Güvenilir,doğru"
}
print(*sozluk)
kullanici_istek = input("Hangi kelimenin anlamını öğrenmek istiyorsunuz?")
if kullanici_istek in sozluk.keys():
    print("Girdiğiniz Kelimenin anlamı:",sozluk[kullanici_istek])
else:
        print("Bu kelime sözlükte bulunmuyor!")
