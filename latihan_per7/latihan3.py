saldo=100000

print("Saldo anda sisa : ",saldo)
print("1. Tarik uang")
print("2. keluar")
pilih=int(input("pilih menu (1/2) : "))

while pilih==1 :
	if saldo!=0  :
		tarik=int(input("Masukan jumlah penarikan : "))
		if tarik <= saldo :
			saldo -= tarik
			print("Penarikan anda berhasil")
			print("Saldo anda sisa : ",saldo)
			print("1. Tarik uang")
			print("2. keluar")
			pilih=int(input("pilih menu (1/2) : "))
		else :
			print("saldo anda tidak cukup")
			print("Saldo anda sisa : ",saldo)
			print("1. Tarik uang")
			print("2. keluar")
			pilih=int(input("pilih menu (1/2) : "))
	
	else : 
		print("saldo anda tidak cukup")
		print("Saldo anda sisa : ",saldo)
		print("1. Tarik uang")
		print("2. keluar")
		pilih=int(input("pilih menu (1/2) : "))
	if pilih ==2 :
		print("Terimakasih telah menggunakan ATM")