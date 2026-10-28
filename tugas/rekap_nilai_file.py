"""Tugas 5 - Rekap nilai dari file.

Membaca data/nilai.txt (format NIM,nilai), memvalidasi tiap baris,
menghitung ringkasan, lalu menulis data/hasil_rekap.txt.

Jalankan dari root folder proyek:
    python3 tugas/rekap_nilai_file.py
"""

BATAS_LULUS = 60


def baca_data(nama_file):
    """Membaca dan memvalidasi file. Mengembalikan list tuple (nim, nilai).

    - File tidak ada      -> pesan jelas, kembalikan list kosong
    - Baris kosong        -> dilewati
    - Baris tidak valid   -> dilaporkan dan dilewati, baris lain tetap diproses
    """
    data = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()
                if not baris:
                    continue
                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    data.append((nim.strip(), nilai))
                except ValueError:
                    print(f"Baris {nomor} dilewati (tidak valid): {baris}")
    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")
    return data


def hitung_ringkasan(data):
    """Menghitung statistik dari record valid."""
    nilai = [item[1] for item in data]
    return {
        "jumlah": len(nilai),
        "rata_rata": sum(nilai) / len(nilai),
        "minimum": min(nilai),
        "maksimum": max(nilai),
        "lulus": sum(1 for x in nilai if x >= BATAS_LULUS),
    }


def tulis_rekap(nama_file, data):
    """Menulis ringkasan ke file. Tidak menulis apa pun jika data kosong."""
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return False
    r = hitung_ringkasan(data)
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {r['jumlah']}\n")
        file.write(f"Rata-rata: {r['rata_rata']:.2f}\n")
        file.write(f"Minimum: {r['minimum']:.2f}\n")
        file.write(f"Maksimum: {r['maksimum']:.2f}\n")
        file.write(f"Jumlah lulus: {r['lulus']}\n")
    return True


def main(input_file="data/nilai.txt", output_file="data/hasil_rekap.txt"):
    data = baca_data(input_file)
    if tulis_rekap(output_file, data):
        print(f"Rekap ditulis ke {output_file}")


if __name__ == "__main__":
    main()
