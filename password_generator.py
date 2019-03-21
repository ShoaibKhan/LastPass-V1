import hashlib
import binascii


def generate_salt(website, user_name):
    return website + user_name


def generate_pepper(website, master_password):
    return website + master_password


def key_stretch_one(salt, master_password):
    return decode_utf(hashlib.pbkdf2_hmac("sha256", encode_utf(master_password), encode_utf(salt), 1299, 32))


def key_stretch_two(pepper, ver_one, length):
    return decode_utf(binascii.hexlify(hashlib.pbkdf2_hmac("sha256", encode_utf(ver_one), encode_utf(pepper), 1299, length)))


def decimal_to_alphabet(ver_two, length, alphabet):
    num_elements = len(alphabet)
    chars = []
    while len(chars) < length:
        ver_two, index = divmod(ver_two, num_elements)
        chars.append(alphabet[index])
    ver_two = ''.join(chars)
    return ver_two


def encode_utf(txt):
    return txt.encode("utf-8")


def decode_utf(txt):
    return txt.decode("utf-8", 'ignore')


def generate_password(website, user_name, master_password, length, alphabet):
    salted = generate_salt(website, user_name)
    peppered = generate_pepper(website, master_password)
    middle = length
    ver_one = key_stretch_one(salted, master_password)
    ver_two = key_stretch_two(peppered, ver_one, length)
    ver_two = ver_two[:middle]
    ver_two = Decimal_to_hexdecimal(ver_two)
    ver_three = decimal_to_alphabet(ver_two, length, alphabet)
    return ver_three


def Decimal_to_hexdecimal(Dec):
    return int(Dec, 16)
