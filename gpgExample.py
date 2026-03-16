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

# directory for message in plaintext
path = 'textfiles/message'

cryptedPath = 'textfiles/message.encrypted'

dirPath = 'textfiles'

messagePath = 'textfiles/plaintext_alice'

# Generating the user key - Normally done through command line 
# I dont want to keep over writing encryption keys if I don't have to.. 

## THIS PARTICULAR SET OF CODE GENERATES THE KEYS 
'''
input_data = gpg.gen_key_input(
    name_email = 'bob@davehat.com',
    passphrase = 'KeepMeSecret', # Not a real password... 
    key_type = 'RSA',
    key_length = 1024
)

key = gpg.gen_key(input_data)

print(key)

# export public key
public_key = gpg.export_keys(str(key))

with open('bob_pub_key.asc', 'w') as f:
    f.write(public_key)
'''



## THIS PARTICULAR SET OF CODE ENCRYPTS A SELECTED FILE 

## Can be used to send encryption to a recipient. 
    # Since recipient has been set to bob, 
    # Only he can decrypt that message w/ his private key. 
    # Does not ensure authenticity&Integrity 
'''
with open(path, 'rb') as f:
    status = gpg.encrypt_file(f, recipients = ['bob@davehat.com'], output=path + ".encrypted")

print(status.ok)
print(status.stderr)
'''

## THIS CODE DECRYPTS A FILE WITH A PRIVATE PASS PHRASE 
'''
with open(cryptedPath, 'rb') as f:
    status = gpg.decrypt_file(f, passphrase= 'KeepMeSecret', output = path + '.decrypted')

print(status.ok)
print(status.stderr)
'''

## ENCRYPT MULTIPLE FILES AT ONCE -- example of a ransomware attack. 
'''
for f in os.listdir(dirPath):
    with open(dirPath+"/" + f, 'rb') as efile:
        status = gpg.encrypt_file(efile, recipients= 'bob@davehat.com', output = dirPath+"/"+ f)

print(status.stderr)
'''


## IMPORT ANOTHER KEY INTO A KEY CHAIN 
'''
key_data = open('bob_pub_key.asc').read()
import_result = gpg.import_keys(key_data)

gpg.trust_keys(import_result.fingerprints, 'TRUST_ULTIMATE') # Set the trust level of the key 

mykeys = gpg.list_keys()

print(mykeys)
'''

# Encrypt then sign --> Alice 
'''
stream = open(messagePath, 'rb')

fp = gpg.list_keys(True).fingerprints[0]

edata = gpg.encrypt_file(stream, recipients='bob@davehat.com', sign=fp,passphrase='KeepMeSecret', output=messagePath + ".pgp")

'''

# Decrypt then verify --> Bob
'''
stream = open(messagePath+'.pgp', 'rb')

decrypted_data = gpg.decrypt_file(stream, passphrase='KeepMeSecret', output=messagePath + '.verified')

print(decrypted_data.status)
print(decrypted_data.valid)
'''