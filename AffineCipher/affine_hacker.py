import check_eng, affine_cipher, mathmeth, time

def main_hack():
	fname = input("Enter the name of the file to be decrypted :")
	f = open(fname, 'r')
	txt = f.read()
	f.close()

	affine_hack(txt)

def affine_hack(txt):
	for key in range (len(affine_cipher.SYMBOLS)**2):
		keyA = affine_cipher.getparts(key)[0] #The first item of the tuple returned by getparts() is keyA
		if (mathmeth.gcd(keyA, len(affine_cipher.SYMBOLS)) != 1):
			continue

		print ('Hacking....'+str(key))
		htxt = affine_cipher.decrypt(txt,key)
		if (check_eng.check(htxt)):
			print("Seems to be a possible hack...")
			print (htxt)

			ch = int(input("Do you want to continue searching ?\nPress '1' to Write to file then quit\nPress '2' to continue search\n"))
			if(ch == 1):
				fname = str(time.ctime())
				fname = fname.replace(':','_')
				fname = fname.replace(' ','_')
				f = open(("hack_"+fname+'.txt').strip(':'),'w')
				f.write(htxt)
				break
			if(ch == 2):
				fname = str(time.ctime())
				fname = fname.replace(':','_')
				fname = fname.replace(' ','_')
				f = open(("hack_"+fname+'.txt').strip(':'),'w')
				f.write(htxt)

main_hack()