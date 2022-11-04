import	hashlib
import csv
from collections import OrderedDict
def hash_password_hack(input_file_name, output_file_name):
	HashDict=OrderedDict()
	user_pass=OrderedDict()
	output=OrderedDict()
	for everynum in range(1000,10000):
	 	HashDict[hashlib.sha256((str(everynum)).encode('utf-8')).hexdigest()]=everynum
	with open(input_file_name) as read:
		reader=csv.reader(read)
		for row in reader:
			user_pass[row[1]]=row[0]
			#hash dict 9asdsdfsdcxv : 1001
			#user_pass 9sdfsdfsdfsdf :mina
	for i in user_pass:
		if i in HashDict:
			# exp>> mina :1001
	 		output[user_pass[i]]=HashDict[i]
	with open(output_file_name,'w',newline='') as save:
		writer=csv.writer(save)
		writer.writerows(output.items())
		
hash_password_hack('input.csv','output.csv')