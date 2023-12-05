import random

# Davlatlar va ularning poytahtlari
davlatlar_poytahtlari = {
    'Oʻzbekiston': 'Toshkent',
    'Qozogʻiston': 'Nursulton',
    'Rossiya': 'Moskva',
    'AQSh': 'Washington',
    'Turkiya': 'Ankara',
    'Yaponiya': 'Tokio',
    'Xitoy': 'Pekin',
    'Fransiya': 'Parij',
    'Germaniya': 'Berlin',
    'Hindiston': 'Yeni-Delhi',
}

def davlat_tanlash():
    """Davlat tanlash uchun funksiya"""
    return random.choice(list(davlatlar_poytahtlari.keys()))

def oyun_boshlash():
    """O'yinni boshlash uchun funksiya"""
    togri_javoblar = 0
    togri_davlat = davlat_tanlash()

    print("Davlatni toping! (Chiqish uchun 'exit' ni kiriting)")

    while True:
        foydalanuvchi_tanlagan_poytaht = input(f"{togri_davlat}ning poytahti qaysi? ").strip()

        if foydalanuvchi_tanlagan_poytaht.lower() == 'exit':
            print(f"O'yin tugadi. Siz {togri_javoblar} marta to'g'ri javob berdingiz.")
            break

        if foydalanuvchi_tanlagan_poytaht.capitalize() == davlatlar_poytahtlari[togri_davlat]:
            print("To'g'ri!")
            togri_javoblar += 1
            togri_davlat = davlat_tanlash()
        else:
            print(f"Noto'g'ri. To'g'ri javob: {davlatlar_poytahtlari[togri_davlat]}")

if __name__ == "__main__":
    oyun_boshlash()



