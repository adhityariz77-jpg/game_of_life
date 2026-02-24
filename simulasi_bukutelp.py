# DEDUPLIKASI
def deduplikasi(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# INTERSECTION DUA ARRAY
def intersection(list1, list2):
    set2 = set(list2)
    return [item for item in list1 if item in set2]

# ANAGRAM CHECK (PAKAI DICT)
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    count = {}

    for char in str1:
        count[char] = count.get(char, 0) + 1

    for char in str2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True

# FIRST RECURRING CHARACTER
def first_recurring_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

# PROGRAM KONTAK
contacts = []  # format: (nama, nomor)

def tambah_kontak():
    nama = input("Masukkan nama: ")
    nomor = input("Masukkan nomor: ")
    contacts.append((nama, nomor))
    print("Kontak berhasil ditambahkan.\n")


def cari_kontak():
    nama = input("Masukkan nama yang dicari: ")
    ditemukan = False
    for kontak in contacts:
        if kontak[0].lower() == nama.lower():
            print(f"Ditemukan: Nama: {kontak[0]}, Nomor: {kontak[1]}")
            ditemukan = True
    if not ditemukan:
        print("Kontak tidak ditemukan.")
    print()


def tampilkan_semua():
    if not contacts:
        print("Belum ada kontak.\n")
        return

    print("Daftar Kontak:")
    for i, kontak in enumerate(contacts, start=1):
        print(f"{i}. {kontak[0]} - {kontak[1]}")
    print()

# MENU UTAMA
def menu():
    while True:
        print("===== MENU =====")
        print("1. Tambah Kontak")
        print("2. Cari Kontak")
        print("3. Tampilkan Semua Kontak")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_kontak()
        elif pilihan == "2":
            cari_kontak()
        elif pilihan == "3":
            tampilkan_semua()
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.\n")

# JALANKAN PROGRAM
if __name__ == "__main__":
    menu()