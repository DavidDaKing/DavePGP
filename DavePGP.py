from pathlib import Path
import sys 
import time
import os
import gnupg


"""
    ** Developer **
    David Bower

    *** PURPOSE ***
    This tool is supposed to enage in secure communication --> Strictly 4 My H.O.M.I.E.Z
        - encrpyt and sign documents with PGP in python 

    *** MODIFICATION HISTORY *** 
    Initial Implementation - DAB 01/26/2026 

"""

# PASS IN USERS STORED GNUPG HOME 

path = input("Please enter the path to your .gnupg file \n" \
"EX: /home/$USER/.gnupg \n")



# Generate Keys

def generate_key():
    # home file 
    # PLEASE CHANGE PARAMETERS

    gpg=gnupg.GPG(gnupghome=path)

    gpg.encoding = 'utf-8'

    # I will never store real credentials.
    input_data = gpg.gen_key_input(
        name_email = 'alice@fakemail.com',
        passphrase = 'testphrase',
        key_type = 'RSA',
        key_length = 1024
    )

    key = gpg.gen_key(input_data)

    print(key)

# Encrypt with our public key

# Decrypt with private key 

# Import keys from other users 

# Sign a document 

# Verify a signature


def davehat_banner():
    banner = r"""
██████╗  █████╗ ██╗   ██╗███████╗██╗  ██╗ █████╗ ████████╗
██╔══██╗██╔══██╗██║   ██║██╔════╝██║  ██║██╔══██╗╚══██╔══╝
██║  ██║███████║██║   ██║█████╗  ███████║███████║   ██║   
██║  ██║██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██║██╔══██║   ██║   
██████╔╝██║  ██║ ╚████╔╝ ███████╗██║  ██║██║  ██║   ██║   
╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   

    DaveHat PGP Engine
    """
    print(banner)





def main():
    davehat_banner()

    ## TAKE IN USER INPUIT 
    if len(sys.argv) == 1:
        print("Useage:\n")
        print("python3 DavePGP.py <command>")
        # Commands associated with python PGP libraries 
        print("\nCommands:")
        print(" key-gen  :  Generates your own keys!")
        sys.exit(0)
        

    cmd = sys.argv[1]

    if cmd == "banner":
        davehat_banner()
    elif cmd == "key-gen":
        generate_key()
    else: 
        print(f"[!] Command '{cmd}' Unknown.")




if __name__ == "__main__":
    main()