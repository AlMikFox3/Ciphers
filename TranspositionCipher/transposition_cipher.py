import random
import math

def encrypt(msg,key):

	#encrypting the message
	cipher_text = [''] * key
	for col in range(key):
		pointer = col
		while pointer < len(msg):
			cipher_text[col] += msg[pointer]
			pointer += key

	return ''.join(cipher_text)
	



def decrypt(msg, key):

	no_of_col = math.ceil(len(msg)/key)
	no_of_row = key
	unused = (no_of_row * no_of_col) - len(msg)

	dec = [''] * no_of_col
	col = 0
	row = 0
	
	for symbol in msg:
		dec[col] = dec[col] + symbol
		col = col + 1

		if(col == no_of_col or (col == no_of_col - 1 and row >= no_of_row - unused)):
			row = row +1
			col = 0

	return ''.join(dec)

mode = input("Enter the mode (encrypt/decrypt) :")

if(mode == 'encrypt'):
	#Getting the file and storing the message
	file_name = input("Enter the name of the file to be encrypted :")
	f = open(file_name, 'r')
	msg = f.read()
	f.close()
	

	# Generating key.txt
	key = random.randint(1,int(len(msg)))
	f = open('key.txt','w')
	f.write(str(key))
	f.close()

	#encrypting into file
	enc = encrypt(msg,key)
	o_file_name = input("Enter the name for the encrypted file :")
	f = open(o_file_name,'w')
	f.write(enc)
	f.close()
	print ("Successfully Encrypted and key.txt has been generated !!")

elif (mode=='decrypt'):
	#Getting the file and storing the message
	file_name = input("Enter the name of the file to be decrypted :")
	f = open(file_name, 'r')
	msg = f.read()
	f.close()

	key = int(input("Enter the Security Key for Decryption :"))

	#decrypting into file
	dec = decrypt(msg,key)
	o_file_name = input("Enter the name for the decrypted file :")
	f = open(o_file_name,'w')
	f.write(dec)
	f.close()

	print("Succesfully Decrypted !!")




