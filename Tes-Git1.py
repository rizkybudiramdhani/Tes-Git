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