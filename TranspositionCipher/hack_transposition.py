import random
import math
import check_eng

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

file_name = input("Enter the name of the file to be decrypted :")
f = open(file_name, 'r')
msg = f.read()
f.close()

#decrypting into file
	
for key in range(1,len(msg)):
	print ('Try '+str(key)+'.....')
	dec = decrypt(msg,key)
	
	if(check_eng.check(dec)):
		print ('Seems to be a hack for key....' + str(key))
		o_file_name = input("Enter the name for the decrypted file :")
		f = open(o_file_name,'w')
		f.write(dec)
		f.close()