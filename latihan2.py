angka_1 = int(input("masukan angka Pertama: "))
operator = input("operator (+ - x :) = ")
angka_2 = int(input("masukan angka Kedua: "))

if operator == "+":
    hasil = angka_1 + angka_2
    print (f"Hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print (f"Hasilnya adalah {hasil}")
elif operator == "x":
    hasil = angka_1 * angka_2
    print (f"Hasilnya adalah {hasil}")
elif operator == ":":
    hasil = angka_1 / angka_2
    print (f"Hasilnya adalah {hasil}")
else:
    print("Masukan dengan benar")