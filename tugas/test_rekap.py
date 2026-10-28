"""Test case wajib Tugas 5. Jalankan dari root: python3 tugas/test_rekap.py"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(__file__))
from rekap_nilai_file import baca_data, tulis_rekap, hitung_ringkasan  # noqa: E402


def tulis(path, isi):
    with open(path, "w", encoding="utf-8") as f:
        f.write(isi)


hasil = []


def cek(id_tc, kasus, kondisi):
    print(f"{id_tc} | {kasus:<38} | {'PASS' if kondisi else 'FAIL'}")
    hasil.append(kondisi)


with tempfile.TemporaryDirectory() as tmp:
    # Normal
    p = os.path.join(tmp, "normal.txt")
    tulis(p, "A001,85\nA002,75\nA003,70\n")
    d = baca_data(p)
    cek("TC1", "Normal: 3 record, rata-rata 76.67",
        len(d) == 3 and abs(hitung_ringkasan(d)["rata_rata"] - 230 / 3) < 1e-9)

    # File hilang
    d = baca_data(os.path.join(tmp, "tidak_ada.txt"))
    cek("TC2", "File hilang: tidak crash, list kosong", d == [])

    # Nilai invalid
    p = os.path.join(tmp, "invalid.txt")
    tulis(p, "A001,85\nA004,abc\nA005,74\n")
    d = baca_data(p)
    cek("TC3", "Nilai invalid: record lain tetap diproses",
        [x[0] for x in d] == ["A001", "A005"])

    # Baris kosong
    p = os.path.join(tmp, "kosong.txt")
    tulis(p, "A001,85\n\n\nA002,75\n")
    cek("TC4", "Baris kosong dilewati", len(baca_data(p)) == 2)

    # Batas lulus
    p = os.path.join(tmp, "batas.txt")
    tulis(p, "A001,60\nA002,59\n")
    cek("TC5", "Nilai 60 dihitung lulus (59 tidak)",
        hitung_ringkasan(baca_data(p))["lulus"] == 1)

    # Format kolom salah (tiga kolom)
    p = os.path.join(tmp, "kolom.txt")
    tulis(p, "A001,85,extra\nA002,70\n")
    cek("TC6", "Baris 3 kolom dilewati", len(baca_data(p)) == 1)

    # Output file
    out = os.path.join(tmp, "rekap.txt")
    ok = tulis_rekap(out, baca_data(p))
    with open(out, encoding="utf-8") as f:
        isi = f.read()
    cek("TC7", "File output dibuat dan berisi rata-rata",
        ok and "Rata-rata: 70.00" in isi)

    # Data kosong tidak menulis file
    out2 = os.path.join(tmp, "rekap_kosong.txt")
    cek("TC8", "Data kosong: file output tidak dibuat",
        tulis_rekap(out2, []) is False and not os.path.exists(out2))

print(f"\nLulus {sum(hasil)}/{len(hasil)}")
raise SystemExit(0 if all(hasil) else 1)
