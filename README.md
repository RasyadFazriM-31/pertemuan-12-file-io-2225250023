# Pertemuan 12 - File I/O dan Error Handling

Nama: Rasyad Fazri Mulyono
NIM: 2225250023
Kelas: 3A

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Format File Input
`data/nilai.txt`, satu record per baris dengan format `NIM,nilai`. Data contoh bersifat fiktif dan sengaja memuat satu baris invalid (`A004,abc`), satu baris kosong, dan satu nilai batas (`A007,60`).

## Cara Menjalankan
Dari root folder proyek:
```
python3 tugas/rekap_nilai_file.py
python3 tugas/test_rekap.py
```
Latihan: `python3 latihan/01_tulis_file.py` dst (jalankan berurutan 01, 02, 03).

## Error yang Ditangani
- `FileNotFoundError` (file input tidak ada): pesan jelas, program tidak crash.
- `ValueError` (nilai bukan angka atau jumlah kolom salah): ditangani **per baris**, record lain tetap diproses.

## Hasil Eksekusi `data/nilai.txt`
```
Baris 4 dilewati (tidak valid): A004,abc
Jumlah data valid: 6
Rata-rata: 79.50
Minimum: 60.00
Maksimum: 92.00
Jumlah lulus: 6
```
Nilai 60 dihitung lulus (`>= 60`).

## Test Case (hasil aktual, `tugas/test_rekap.py`)
| ID | Kondisi | Expected | Actual | Status |
|----|---------|----------|--------|--------|
| TC1 | Semua baris valid | Semua diproses, rata-rata benar | 3 record, 76.67 | PASS |
| TC2 | File tidak ada | Pesan, tidak crash | list kosong | PASS |
| TC3 | `A004,abc` | Dilewati, lainnya diproses | A001, A005 terbaca | PASS |
| TC4 | Baris kosong | Dilewati | 2 record | PASS |
| TC5 | Nilai 60 | Lulus | lulus = 1 (59 tidak) | PASS |
| TC6 | Baris 3 kolom | Dilewati | 1 record | PASS |
| TC7 | Tulis rekap | File output terbentuk | berisi "Rata-rata: 70.00" | PASS |
| TC8 | Data kosong | File output tidak dibuat | tidak dibuat | PASS |

Total 8/8 PASS.

## Refleksi
Error yang ditemukan: nilai `abc` pada baris 4 memicu `ValueError` saat `float()`. Program menangkapnya di dalam loop, mencatat nomor barisnya, lalu melanjutkan sehingga satu baris rusak tidak menggagalkan seluruh file.

## Referensi/Bantuan
Bahan ajar Pertemuan 12, Python 3 Documentation (Reading and Writing Files; Errors and Exceptions). Dibantu Claude untuk menyusun kode dan test; penulis wajib dapat menjelaskan isinya.
