print("=== Program Penghitung Hasil Panen ===")
target = float(input("Masukkan target panen bulan ini (kg): ")) # Fitur buatan Dzikri
berat = float(input("Masukkan berat panen (kg): "))
harga_per_kg = float(input("Masukkan harga per kg: Rp"))

total = berat * harga_per_kg
diskon = 0
if total > 1000000:
    diskon = total * 0.10
total_bersih = total - diskon

print(f"\n--- HASIL ---")
print(f"Target terpenuhi: {'Ya' if berat >= target else 'Belum'}") # Fitur buatan Dzikri
print(f"Total pendapatan kotor: Rp{total}")
print(f"Potongan diskon: Rp{diskon}")
print(f"Total pendapatan bersih: Rp{total_bersih}")
