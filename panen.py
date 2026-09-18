print("=== PROGRAM UTAMA: SISTEM PANEN RAYA ===") 
berat = float(input("Masukkan berat panen (kg): "))
harga_per_kg = float(input("Masukkan harga per kg: Rp"))
total = berat * harga_per_kg
print(f"Total pendapatan: Rp{total}")
