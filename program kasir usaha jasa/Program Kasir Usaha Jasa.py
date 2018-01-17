import os 
def awal():
	os.system('cls')
	print ("PROGRAM MENGHITUNG JUMLAH PEMBAYARAN PADA USAHA JASA")
	print (67*"-")
	print ("Masukkan pilihan pembayaran: ")
	print ("1. Sablon Baju")
	print ("2. Printing Sticker size kecil")
	print ("3. Printing Banner Size A")
	print ("4. Printing Banner Size B")
	print ("5. Printing Banner Size C")
	print ("6. Exit")
	print (67*"-")
def kasir():
	jawab = "y"	
	harga = 0
	banyak = 0
	while (jawab =="y"):
		awal()
		kode = input("Masukkan kode produk : ")
		if kode=="1":
			os.system('cls')
			print ("Sablon Baju Rp.20,000")
			harga+=20000
		elif kode=="2":
			os.system('cls')
			print ("Printing Sticker size kecil Rp.15,000")
			harga+=15000
		elif kode=="3":
			os.system('cls')
			print ("Printing Banner Size A Rp.15,000")
			harga+=15000
		elif kode=="4":
			os.system('cls')
			print ("Printing Banner Size B Rp.25,000")
			harga+=25000
		elif kode=="5":
			os.system('cls')
			print ("Printing Banner Size C Rp.40,000")
			harga+=40000
		jawab = input("Apakah anda masih ingin memasukkan jasa ? (y/n)")
	os.system('cls')
	print ("Total biaya yang harus dibayar adalah : "+"Rp."+str(harga))
	bayar = input ("Masukkan jumlah pembayaran : ")
	total = int(bayar)-int(harga)
	os.system('cls')
	print ("Total kembalian adalah : "+"Rp."+str(total))
	finish=input()

print ("-"*23)
print ("Program Kasir Usaha Percetakan")
print ("-"*23)
username = input("Username : ")
password = input("Password : ")
if username == "sisfo17" and password == "mantap":
	awal()
	kasir()
else:
	os.system('cls')
	print ("LOGIN ERROR")
	print ("PROGRAM CRASH")
