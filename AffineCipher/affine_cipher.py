import sys, mathmeth, random
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""" 

def main():
	mode = input("Enter the mode (E/D) : ")
	if (mode == 'E' or mode =='e'):
		fname = input("Enter the name of the file to be encrypted : ")
		f = open(fname, 'r')
		txt = f.read()
		f.close()
		key = getkey()
		f = open('key.txt','w')
		f.write(str(key))
		encrypt(txt,key)


	elif (mode == 'D' or mode == 'd'):
		fname = input("Enter the name of the file to be decrypted : ")
		f = open(fname, 'r')
		txt = f.read()
		f.close()
		key = int(input("Enter the decryption key: "))
		decrypt(txt,key)

def getkey():
	while True:
		keyA = random.randint(2,len(SYMBOLS))
		keyB = random.randint(2,len(SYMBOLS))
		if (mathmeth.gcd(keyA,len(SYMBOLS)) == 1):
			return (keyA * len(SYMBOLS) + keyB)

def getparts(key):
	keyA = key // len(SYMBOLS)
	keyB = key % len(SYMBOLS)
	return (keyA, keyB)

def encrypt(txt, key):
	keyA, keyB = getparts(key)
	ciphertext = ''
	for symbol in txt:
		if symbol in SYMBOLS:
			symindex = SYMBOLS.find(symbol)
			ciphertext += SYMBOLS[((keyA * symindex + keyB)%len(SYMBOLS))]
		else :
			ciphertext += symbol

	fname = input("Enter the name for the encrypted file :")
	f = open(fname,'w')
	f.write(ciphertext)

def decrypt(txt,key):
	keyA, keyB = getparts(key)
	print(str(keyA) + " " + str(keyB))
	plaintext = ''
	for symbol in txt:
		if symbol in SYMBOLS:
			symindex = SYMBOLS.find(symbol)
			plaintext += SYMBOLS[((symindex - keyB) * mathmeth.findModInverse(keyA, len(SYMBOLS)))%len(SYMBOLS)]
		else:
			plaintext += symbol

	fname = input("Enter the name for the decrypted file :")
	f = open(fname,'w')
	f.write(plaintext)


main()