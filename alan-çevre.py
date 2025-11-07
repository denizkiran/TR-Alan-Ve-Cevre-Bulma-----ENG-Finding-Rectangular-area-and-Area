def dikdortgen_ciz(genislik, yukseklik):

    w = int(genislik)
    h = int(yukseklik)


    for i in range(h):

        if i == 0 or i == h - 1:

            print('*' * w)

        else:

            if w > 1:
                print('*' + ' ' * (w - 2) + '*')

            else:
                print('*')

def cevre_hesaplama(kenar1, kenar2):

    cevre = 2 * (kenar1 + kenar2)
    print(f"Dikdörtgenin çevresi: {cevre}")
    print("\nDikdörtgeninizin çizimi:")
    dikdortgen_ciz(kenar1, kenar2)

def alan_hesaplama(kenar1, kenar2):

    alan = kenar1 * kenar2
    print(f"Dikdörtgenin alanı: {alan}")
    print("\nDikdörtgeninizin çizimi:")
    dikdortgen_ciz(kenar1, kenar2)

def secim_ekrani(kenar1, kenar2):

    while True:
        print("\n----------Lütfen yapmak istediğiniz işlemi seçiniz----------")
        print("1. Dikdörtgenin çevresini hesaplama")
        print("2. Dikdörtgenin alanını hesaplama")
        print("3. Çıkış")
        secim = input("Yapmak istediğiniz işlemin numarasını giriniz: ")

        if secim == "1":
            cevre_hesaplama(kenar1, kenar2)
        elif secim == "2":
            alan_hesaplama(kenar1, kenar2)
        elif secim == "3":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen 1, 2 veya 3 giriniz.")


try:
    ilkkenar_str = input("Lütfen dikdörtgenin genişliğini giriniz: ")
    ilkkenar = int(ilkkenar_str)
    if ilkkenar <= 0:
        print("Girdiğiniz değer 0'dan büyük olmalıdır.")
        exit()
    print(f"Girdiğiniz genişlik '{ilkkenar}' olarak belirlenmiştir.")

    ikincikenar_str = input("Lütfen dikdörtgenin yüksekliğini giriniz: ")
    ikincikenar = int(ikincikenar_str)
    if ikincikenar <= 0:
        print("Girdiğiniz değer 0'dan büyük olmalıdır.")
        exit()
    print(f"Girdiğiniz yükseklik '{ikincikenar}' olarak belirlenmiştir.")

    secim_ekrani(ilkkenar, ikincikenar)

except ValueError:
    print("Hatalı giriş. Lütfen sayısal bir değer giriniz.")
    exit()
