print("=== Program Penghitung Hasil Panen ===")
berat = float(input("Masukkan berat panen (kg): "))
harga_per_kg = float(input("Masukkan harga per kg: Rp"))

total = berat * harga_per_kg

# Fitur Diskon: Diskon 10% jika total pendapatan kotor di atas Rp 1.000.000
diskon = 0
if total > 1000000:
    diskon = total * 0.10
    
total_bersih = total - diskon

print(f"Total pendapatan kotor: Rp{total}")
print(f"Potongan diskon: Rp{diskon}")
print(f"Total pendapatan bersih: Rp{total_bersih}")
