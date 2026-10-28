# Memproses data/nilai.txt baris demi baris.
# Baris kosong dilewati dan baris tidak valid dilaporkan (lihat Tugas 5 untuk versi lengkap).
with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for nomor, baris in enumerate(file, start=1):
        baris = baris.strip()
        if not baris:
            continue
        try:
            nim, teks_nilai = baris.split(",")
            print(nim, float(teks_nilai))
        except ValueError:
            print(f"Baris {nomor} tidak valid: {baris}")
