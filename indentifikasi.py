import re
import base64

def id_md5(text):
    return re.match(r"^[0-9a-fA-F]{32}$", text) is not None

def id_base32(text):
    return re.match(r"^[A-Z2-7]{8,}$", text) is not None

def id_base64(text):
    try:
        decoded_bytes = base64.b64decode(text, validate=True)
        return True
    except:
        return False

def identify_enkripsi(text):
    if id_md5(text):
        return "MD5"
    elif id_base32(text):
        return "Base32"
    elif id_base64(text):
        return "Base64"
    else:
        return "Tipe enkripsi tidak dikenali."

if __name__ == "__main__":
    enkripsi = identify_enkripsi(input("input enkripsi: "))
    print(f"Tipe Enkripsi: {enkripsi}")


