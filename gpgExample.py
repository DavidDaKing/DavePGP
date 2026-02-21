"""
Docstring for gpgExample :: 

    - Going through a youtube video tutorial before returning to my attempted implementation. 
        - https://www.youtube.com/watch?v=9NiPwvLCDpM

"""

import gnupg
import os


# Creating a gnupg directory in the user's home file. 
gpg = gnupg.GPG(gnupghome='/home/bob/.gnupg')
gpg.encoding = 'utf-8'

# Generating the user key - Normally done through command line 
input_data = gpg.gen_key_input(
    name_email = 'bob@davehat.com',
    passphrase = 'KeepMeSecret',
    key_type = 'RSA',
    key_length = 1024
)

key = gpg.gen_key(input_data)

print(key)
