import random
mode = input('Enter the mode (encryption/decryption)')
letters = 'abcdefghijklmnopqrstuvwxyz'
LETTERS = letters.upper()
numbers = '0123456789'
enc = ''
dec = ''

if mode == 'encrypt':
	file_name = input("Enter the name of the file to be encrypted :")
	f = open(file_name,'r')
	m = f.read()
	f.close()
	key = random.randint(1,25)
	nkey = random.randint(1,9)
	f1 = open('key.txt','w')
	k = str(key) + ' ' + str(nkey)
	f1.write(str(k))
	f1.close()

elif mode == 'decrypt':
	key = int(input("Enter Secret Key 1 for decryption"))
	nkey = int(input("Enter Secret Key 2 for decryption"))
	f = open('encrypted.txt', 'r')
	m = f.read()
	f.close()
	

for symbol in m:
	if symbol in letters:
		n = letters.find(symbol)
		if mode == 'encrypt':
			n = n + key
		elif mode == 'decrypt':
			n = n - key

		if n > 25 :
			n = n-25
		elif n < 0 :
			n = n+25

		if mode == 'encrypt':
			enc = enc + letters[n]
		else :
			dec = dec + letters[n]

	elif symbol in LETTERS:
		n = LETTERS.find(symbol)
		if mode == 'encrypt':
			
			n = n + key
			
		elif mode == 'decrypt':
			
			n = n - key

		if n > 25 :
			n = n-25
		elif n < 0 :
			n = n+25

		if mode == 'encrypt':
			enc = enc + LETTERS[n]
		else :
			dec = dec + LETTERS[n]
	
	elif symbol in numbers:
		n = numbers.find(symbol)
		if mode == 'encrypt':
			
			n = n + nkey
			
		elif mode == 'decrypt':
			
			n = n - nkey

		if n > 9 :
			n = n-9
		elif n < 0 :
			n = n+9

		if mode == 'encrypt':
			enc = enc + numbers[n]
		else :
			dec = dec + numbers[n]
			
	else :
		if mode == 'encrypt':
			enc = enc + symbol
		else :
			dec = dec + symbol

if mode == 'encrypt':
	f = open('encrypted.txt','w')
	f.write(enc)
	f.close()
	print ('Successfully Encrypted and key.txt generated')
	

elif mode == 'decrypt':
	f = open('decrypted.txt','w')
	f.write(dec)
	f.close()
	print('Successfully decrypted')
	