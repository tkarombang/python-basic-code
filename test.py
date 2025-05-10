# name = "Azwar"
# print(f"Hello Nama sayya {name}")


# list = ["string", 1, 2.2]
# list[0] = 398
# print(list)



# product = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcamp", "microphone"]
# print(product[0:5:2])

# set = {1,6,3,4,2,7,4,5,8}
# print(set)

# kata = "ini huruf kecil menjadi besar"
# print(kata.upper())

# kata = "INI HURUF BESAR MENJADI KECIL"
# print(kata.lower())

# kata = 'HapusTidakHapusHapusHapusHapus'
# print(kata.startswith("Tidak"))

# kata = 'Awal Akhir'.endswith('Akhir')
# print(kata)

# print(' '.join(['Ingin', 'Menggabungkan', '!']))

# print('Kata Yang Dipecah Menjadi Array'.split())

# print('''ini adalah kalimat
# yang akan panjang yang
# menggunakan baris baru
# dan akan digabungkan
# menjadi array'''.split())

# kata = "kalimat INI akan mengganti kalimat ITU"
# print(kata.replace('INI', 'IMI'))

# kata = 'KATA INI AKAN MENGECEK APAKAH HURUF BESAR ATAU TIDAK'
# print(kata.isupper())

# kata = 'mengecekApakahKataIniMurniSemuaHurufTanpaAdaSpasiAtauAngka'
# print(kata.isalpha())

# kata = 'kataIniApakahTerdapatAngka123'
# print(kata.isalnum())

# print('123'.isdecimal())

# print('        '.isspace())

# print('Terdapat Huruf Kapital Pada Setiap Kata Pertamanya'.istitle())

# dico = 750000
# batas = 500000
# diskon = 0.1
# if dico > batas :
#   total_harga = dico - (dico * diskon)
#   print(total_harga)
  


# x = "Belajar"
# y = "Python"
# result = x < y
# print(result)

# print("Selamat Datang dalam program Python!/n")
# print("Silahkan masukkan data diri anda")
# nama = input("Masukkan Nama Anda: ")
# tahun_lahir = input("Masukkan tahun lahir anda: ")
# umur = 2025 - int(tahun_lahir)

# print(f"Selamat datang {nama} dalam program Python, per 2025 umur anda adalah {umur} Tahun. /n")
# print("Terimakasih Telah menggunakan program Python!")


# x = 1
# y = 2

# x, y = y, x

# print("setelah penukaran: ")
# print("x = ", x)
# print("y = ", y)

# score = 100
# if score == 100:
#   print("nilai anda ", score)
# else:
#   print("nilai anda tidak mencapai ", score)

# x = 100
# if x: print("ini true")


# tinggiBadan = 120
# print("anda boleh naik") if tinggiBadan >= 160 else print("anda tidak boleh")

# lulus = True
# kelulusan = ('anda tidak lulus', 'Selamat anda lulus')[lulus]

# print(kelulusan)

# ***PERULANGAN***
# FOR
# list = [1,2,3,4,5,6,7,8,9]
# for i in list:
#   print(i)

# for i in range(1,10, 2):
#   print(i)

# WHILE
# counter = 1
# while counter <= 5:
#   print(counter)
#   counter += 1

# FOR BERSARANG
# for i in range(1, 3):
#   for j in range(1, 3):
#     print(i, j)

# ****CONTROL PERULANGAN***
# BREAK
# for i in range(2):
#   print("Perulangan luar:", i)
#   for j in range(10):
#     print("perulangan dalam:", j)
#     if j == i:
#       break

# for huruf in 'dico ding':
#   if huruf == ' ':
#     break
#   print('huruf saat in: {}'.format(huruf))

# CONTINUE
# for huruf in 'Dico ding':
#   if huruf == ' ':
#     continue
#   print('huruf saat ini: {}'.format(huruf))

# ELSE SETELAH FOR
# number = [1,2,6,4,5]

# for num in number:
#   if num == 6:
#     print('Angka ditemukan! Program berhenti')
#     break
#   else:
#     print('Angka tidak ditemukan')

# ELSE SETELAH WHILE
# count = 0
# while count < 3:
#   print('0 lebih besar dari 3')
#   count += 1
# else:
#   print('kondisi (3<3 == false)')


# n = 10
# while n > 0:
#   n = n - 1
#   if n == 7:
#     break
#   print(n)
# else:
#   print("loop selesai")

# PASS STATEMENT
# x = 10
# if x > 5:
#   pass
# else:
#   print('Nilai x tidak memenuhi')

# angka = [1,2,3,4]
# pangkat = []
# for n in angka:
#   pangkat.append(n**2)
# print(pangkat)
# LIST COMPREHENSION new_list = [expression for_loop_one_more_conditions]
# angka = [1,2,3,5]
# pangkat = [n**2 for n in angka]
# print(pangkat)



# LOOP QUIZ
# TODO:
# Buatlah sebuah variabel bertipe list bernama "evenNumber" dengan ketentuan:
# - variabel tersebut menampung bilangan genap dari 0 hingga 500 (ingat 0 dan 500 termasuk).

# Tips:
# Anda bisa menggunakan loop dan if atau list comprehension untuk memudahkan.
# """

# evenNumber = []
# for n in range(0, 501):
#   if n % 2 == 0:
#     evenNumber.append(n)
# print(evenNumber)
# evenNumber = [n for n in range(0, 501) if n % 2 == 0]
# print(evenNumber)



# ***ERROR HANDLING & EXCEPTION****
# z = 0 
# try:
#   print(1/z)
# except ZeroDivisionError:
#   print("anda tidak bisa membagi angka dengan nilai nol")
  

# var_dict = {"rata_rata": "1.0"}

# try:
#   # print(f"rata-rata adalah {var_dict['rata_rata']}")

#   # untuk menampilkan except TypeError
#   print(f"rata-rata adalah {var_dict['rata_rata']}")
# except KeyError:
#   print("Key tidak ditemukan")
# except TypeError:
#   print("Anda tidak bisa membagi niai dengan tipe data string")
# else:
#   print("Kode ini dieksekusi jika tidak ada exception")
# finally:
#   print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception")


# ####RAISE EXCEPTION
# var = -1
# if var < 0:
#   raise ValueError("Bilangan negatif tidak diperbolehkan")
# else:
#   for i in range(var):
#     print(i+1)

















































# import pygame
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()
# square_pos = pygame.Rect(200, 500, 50, 50)

# while True:
#     for event in pygame.event.get():  # Perbaikan: loop melalui semua event
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()  # atau raise SystemExit
    
#     screen.fill("black")
#     pygame.draw.rect(screen, "red", square_pos)
#     pygame.display.flip()
#     clock.tick(60)


# import pygame
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()
# square_pos = pygame.Rect(200,500,20,20)
# while True:
#   if pygame.event.get(pygame.QUIT): break
#   keys = pygame.key.get_pressed()
#   if keys[pygame.K_UP]:
#     square_pos.y -= 20
#   if keys[pygame.K_DOWN]:
#     square_pos.y += 20
#   if keys[pygame.K_LEFT]:
#     square_pos.x -= 20
#   if keys[pygame.K_RIGHT]:
#     square_pos.x += 20
#   screen.fill("black")
#   pygame.draw.rect(screen, "red", square_pos)
#   pygame.display.flip()
#   clock.tick(60)