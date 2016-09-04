import time
import random
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt():
	fname = input('Enter the name/path of the file to be encrypted : ')
	f = open(fname, 'r')
	msg = f.read()
	f.close()
	#key = input ('Enter Security Key (character string) for encryption :')
	key = ''
	kl = random.randint(10,17)
	for i in range (0,kl):
		n = random.randint(0,25)
		key+= LETTERS[n]
	keyf = ((str(time.ctime())).replace(' ','_')).replace(':','_')
	f = open('key' + keyf,'w')
	f.write(str(key))
	print ('key_'+keyf+" generated....")
	enc = ''

	keyindex = 0
	for symbol in msg :
		num = LETTERS.find(symbol.upper())
		
		if num != -1 :
			num += LETTERS.find(key[keyindex])
			num = num % len(LETTERS)
			enc += LETTERS[num]
			keyindex += 1
			if (keyindex == len(key)):
				keyindex = 0
		else :
			enc += symbol
	keyf = ((str(time.ctime())).replace(' ','_')).replace(':','_')
	f = open('enc' + keyf,'w')
	f.write(str(enc))
	f.close()
	print ('ENCRYPTION SUCCESSFUL ! enc_'+keyf+" generated....")




def decrypt():
	fname = input('Enter the name/path of the file to be decrypted : ')
	f = open(fname, 'r')
	msg = f.read()
	f.close()
	key = input ('Enter Security Key (character string) for decryption :')
	enc = ''

	keyindex = 0
	for symbol in msg :
		num = LETTERS.find(symbol.upper())
		
		if num != -1 :
			num -= LETTERS.find(key[keyindex])
			num = num % len(LETTERS)
			enc += LETTERS[num]
			keyindex += 1
			if (keyindex == len(key)):
				keyindex = 0
		else :
			enc += symbol
	keyf = ((str(time.ctime())).replace(' ','_')).replace(':','_')
	f = open('dec' + keyf,'w')
	f.write(str(enc))
	f.close()
	print ('DECRYPTION SUCCESSFUL ! dec_'+keyf+" generated....")




mode = input ('E/D ?   - ')
if(mode == 'E' or mode == 'e'):
	encrypt()
elif (mode == 'D' or mode == 'd'):
	decrypt()