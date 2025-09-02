# Input User
a = float(input("Masukkan angka: ")) # angka pertama
o = input("Masukkan operator: ") # operator
b = float(input("Masukkan angka: ")) # angka kedua

# algoritma
if o == '+':
    c = a + b
elif o == '-':
    c = a - b
elif o == '*':
    c == a * b
elif o == '/':
    if b != 0:
        c = a / b
    else:
        print("Tidak dapat dibagi dengan 0")
        exit()
else:
    print("Operator anda tidak valid!")
    exit()

print(f"Hasilnya adalah {c:.0f}" if c.is_integer() else (f"Hasilnya adalah {c}"))