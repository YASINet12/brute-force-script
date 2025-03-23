import zipfile
import itertools
import string

def brute_force_zip(zip_filename, max_length=4):
    chars = string.ascii_lowercase  
    zip_file = zipfile.ZipFile(zip_filename)

    for length in range(1, max_length + 1):
        for password in itertools.product(chars, repeat=length):
            password = ''.join(password)
            try:
                zip_file.extractall(pwd=password.encode())
                print(f"[✔] Mot de passe trouvé: {password}")
                return
            except:
                print(f"[X] Essai: {password}")
    
    print("[!] Aucun mot de passe trouvé.")

brute_force_zip("protected.zip", max_length=3)
