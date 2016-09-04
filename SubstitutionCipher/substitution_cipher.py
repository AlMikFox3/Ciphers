import time, random
greek = 'αβγδεζηθικλμνξοπρστυφχψω'
x = '!@#$%^&*()_+{|}"<>?/`~\;-='
SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'
def main():
	mode = input("Enter the mode (E/D) : ")
	if (mode == 'E' or mode =='e'):
		fname = input("Enter the name of the file to be encrypted : ")
		f = open(fname, 'r')
		txt = f.read()
		f.close()
		key = getkey()
		fname = ('key_'+str(time.ctime()).replace(' ','_')).replace(':','_')
		f = open(fname+'.txt','w')
		f.write(str(key))
		print ('KEY : ' + fname + ' generated..' )
		encrypt(txt,key)


	elif (mode == 'D' or mode == 'd'):
		fname = input("Enter the name of the file to be decrypted : ")
		f = open(fname, 'r')
		txt = f.read()
		f.close()
		
		keyf = input("Enter the key file : ")
		f = open(keyf, 'r')
		key = f.read()
		f.close()
		decrypt(txt,key)

def getkey():
	keylist = list(SYMBOLS)
	random.shuffle(keylist)
	key = ''.join(keylist)
	return key

def encrypt(txt, key):
	ciphertext = ''
	for symbol in txt:
		s = symbol.lower()
		if s in key:
			q = key.find(s)
			ciphertext += x[q]

		
			

		else:
			ciphertext += symbol

	print (ciphertext)
	fname = ('enc_'+str(time.ctime()).replace(' ','_')).replace(':','_')
	f = open(fname+'.txt','w')
	f.write(ciphertext)
	f.close()
	print ('Successfully Encrypted  : ' + fname + ' generated..' )




def decrypt(txt, key):
	plaintext = ''
	#print(txt + '\n\n\n' +key)
	for symbol in txt:
		if symbol in x:
			q = x.find(symbol)
			plaintext += key[q]

		else:
			plaintext += symbol

	print(plaintext)
	fname = ('dec_'+str(time.ctime()).replace(' ','_')).replace(':','_')
	f = open(fname+'.txt','w')
	f.write(plaintext)
	f.close()
	print ('Successfully Decrypted  : ' + fname + ' generated..' )

main()


