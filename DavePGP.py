from pathlib import Path
import sys 
import time
import os
import gnupg
import argparse
import subprocess
import textwrap


"""
    ** Developer **
    David Bower

    *** PURPOSE ***
    This tool is supposed to enage in secure communication
        - encrpyt and sign documents with PGP in python 

    *** MODIFICATION HISTORY *** 
    Initial Implementation - DAB 01/26/2026 

"""

# TEST 
APP_HOME = Path.home() / ".gnupg"
GNUPG_HOME = APP_HOME / "gnupg"



# PASS IN USERS STORED GNUPG HOME 

#path = input("Please enter the path to your .gnupg file \n" \
#"EX: /home/$USER/.gnupg \n")


# List current Keys (public, secret)

def list_pub_key(_):
    p = run_gpg(["--list-keys"], check=False)
    if p.returncode != 0 and "No public key" in p.stderr:
        print("[i] No keys yet.")
        return
    print(p.stdout.strip() or p.stderr.strip())

def list_sec_key(_):
    p = run_gpg(["--list-secret-keys"], check=False)
    if p.returncode != 0 and "No secret key" in p.stderr:
        print("[i] No secret keys yet.")
        return
    print(p.stdout.strip() or p.stderr.strip())

# Generate Keys
    # - Generate key directory
    # - Generate the key ring 

def generate_dir():
    # home file 
    # PLEASE CHANGE PARAMETERS

    GNUPG_HOME.mkdir(parents=True, exist_ok=True)
    try:
        os.chmod(GNUPG_HOME, 0o700)
    except PermissionError:
        pass

    print(f"[+] Initialized app keyring at: {GNUPG_HOME}")

def generate_ring(args):
    params = textwrap.dedent(f"""
            %echo generating key
            Key-Type: RSA
            Key-Length: 3072
            Subkey-Type: RSA
            Subkey-Length: 3072
            Name-Real: {args.name}
            Expire-Date: {args.expire}
            Passphrase: {args.passphrase}
            %commit
            %echo done
         """)
    
    p = run_gpg(["--pinentry-mode", "loopback", "--gen-key"], input_text=params)
    print("[+] Key generated.")

    list_sec_key(args)

# Encrypt with our public key

# Decrypt with private key 

# Import keys from other users 

# Sign a document 

# Verify a signature


# Run the gpg command as a subprocess 
def run_gpg(args, input_text=None, check=True):

    env = os.environ.copy()
    env["GNUPGHOME"] = str(GNUPG_HOME)

    GNUPG_HOME.mkdir(parents=True, exist_ok=True)
    try:
        os.chmod(GNUPG_HOME, 0o700)
    except PermissionError:
        pass
    
    cmd = ["gpg", "--batch", "--yes"] + args
    p = subprocess.run(cmd, input=input_text, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)

    if check and p.returncode != 0:
        raise RuntimeError(f"gpg failed: {p.stderr.strip()}")
    
    return p


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


# Parse the user command 

def build_parser():
    parser = argparse.ArgumentParser(prog="dave-pgp", description="This is my command line interface for PGP encryption and decryption")

    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="Initialize app keyring directory")
    p_init.set_defaults(func=generate_dir())

    p_list = sub.add_parse("list", help="List public keys in app ring")
    p_list.set_defaults(func=list_pub_key())

    p_listsec = sub.add_parse("list-secret", help="List secret keys in app ring")
    p_listsec.set_defaults(func=list_sec_key())

    



    return parser


def main():
    davehat_banner()


    # USE THE PARSER 
    parser = build_parser()

    args = parser.parse_args()

    try:
        args.func(args)
    except Exception as e:
        print(f"[!] Error: {e}", file=sys.stderr)
        sys.exit(1)




if __name__ == "__main__":
    main()