# Aplikasi Input Data Siswa


import os
import sys

class Mahasiswa:
	nim = ''
	nama = ''

pilih = 0
dataSiswa = []

def menu() :
	os.system('cls')
	print("Menu Aplikasi Data Siswa")
	print(30*"-")
	print("1. Input Data Siswa")
	print("2. Tampilkan Data siswa")
	print("3. Update Data Siswa")
	print("4. Hapus Data siswa")
	print("5. Author")
	print("6. keluar Aplikasi")
	pilih = int(input("Masukkan pilihan anda : "))
    	if pilih == 1 :
        	pilih1()
        	menu()
    	elif pilih == 2:
        	tampil()
        	input("kembali menu utama")
        	menu()
    	elif pilih == 3:
