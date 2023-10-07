import random #random metodunu import ederek oluşturduğum listenin içinden rastgele bir isim seçmeyi sağladım

print("Kelime Tahmin Oyunu")

kelimeler = ["ali", "ahmet", "ömer", "abdurrahman", "murat", "semih"] # oluşturduğum liste
secilen_kelime = random.choice(kelimeler)#choice komudu ile listemin içinden random seçim yaptım
tahmin_listesi = [] 
can = 6  # Oyuncunun 6 canı vardır

while can > 0: #bu oyunu döngüye sokarak tahmin için can durumuna göre döngü oluşturdum
    durum = ""
    for harf in secilen_kelime: 
        if harf in tahmin_listesi:
            durum += harf
        else:
            durum += "_"
    
    print("Kelime: " + durum)
    print("Kalan Can: " + str(can))
    
    # Oyuncudan tahmin aldım
    tahmin = input("Bir harf tahmin edin: ").lower() #lower komutu ile büyük harflerin küçük olarak algılanmasını sağladım.
    
    # Tahminin geçerli olup olmadığını  kontrol ettim
    if len(tahmin) != 1 or not tahmin.isalpha():#isalpha komudu ile alfebede olmayan karakterleri kontrol altına aldım.
        print("Geçersiz tahmin. Lütfen tek harf girin.")
        continue
    
    # Tahmin doğru mu? sorusunu kontrol ettim.
    if tahmin in secilen_kelime:
        tahmin_listesi.append(tahmin) #append ekleme komudu listeye eklemek için kullandım.
        if set(tahmin_listesi) == set(secilen_kelime):
            print("Tebrikler! Kelimeyi doğru tahmin ettiniz: " + secilen_kelime)
            break
    else:
        can -= 1
        print("Yanlış tahmin. Kalan can: " + str(can))

# Oyun bittiğinde sonucu  gösterdim.
if can == 0:
    print("Oyunu kaybettiniz. Doğru kelime: " + secilen_kelime)



