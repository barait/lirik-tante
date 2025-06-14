import time
import sys

def ketik(teks, kecepatan):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(kecepatan)
    print()

lirik_dengan_pengaturan = [
    ("Tanteeeee",0.08,1.3),
    ("sudah terbiasa terjadi tante", 0.08, 1.0),
    ("Teman datang ketika lagi butuh saja", 0.08, 1.6),
    ("Coba kalo lagi susah", 0.08, 1.2),
    ("Mereka semua menghilaaaaaangg...", 0.07, 4.0)
]

print("🎧 Memutar lagu: Sudah Terbiasa Terjadi Tante 🎧\n")
for baris, kecepatan_ketik, jeda_baris in lirik_dengan_pengaturan:
    ketik(baris, kecepatan_ketik)
    time.sleep(jeda_baris)

print("\nTerima kasih Tante.")
