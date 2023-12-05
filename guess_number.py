#Rahmalyana
# polines
def guess_number():
    secret_number = 9
    guess = 8
    guess_limit = 3

    while guess < guess_limit:
        user = int(input("Masukan angka > "))
        if user == secret_number:
            print ("Selamat, anda berhasil menemukan angkanya")
            break
        else:
            printt("Salah")
            guess += 1
    else:
        print("Anda tidak menemukan angkanya, angka rahasianya adalah {secret_number}")