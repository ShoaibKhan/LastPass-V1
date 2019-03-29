import hashlib
import binascii
import re

lower_alpha = "abcdefghijklmnopqrstuvwxyz"
upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num_alpha = "0123456789"
spec_alpha = "!@#$%^&*()-_"

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


def generate_password(website, user_name, master_password, length, lower_state, upper_state, nums_state, special_char_state):

    #Section below determines the characters used in the password
    alphabet = ""
    if lower_state == 1:
        alphabet += lower_alpha
        low_met = 0
    else:
        low_met = 1
    if upper_state == 1:
        alphabet += upper_alpha
        upp_met = 0
    else:
        upp_met = 1
    if nums_state == 1:
        alphabet += num_alpha
        num_met = 0
    else:
        num_met = 1
    if special_char_state == 1:
        alphabet += spec_alpha
        spec_met = 0
    else:
        spec_met = 1

    #Section below actually creates the password    
    salted = generate_salt(website, user_name)
    peppered = generate_pepper(website, master_password)
    middle = length
    ver_one = key_stretch_one(salted, master_password)
    ver_two = key_stretch_two(peppered, ver_one, length)
    ver_two = ver_two[:middle]
    ver_two = Decimal_to_hexdecimal(ver_two)
    ver_three = decimal_to_alphabet(ver_two, length, alphabet)

    #Section below makes sure each password_requirement is met
    if low_met == 0 and not(re.search('[a-z]', ver_three)):
        print("lower entered")
        ver_three = ver_three[:-1] + lower_alpha[int(length)%27]
    low_met = 1
    if upp_met == 0 and not(re.search('[A-Z]', ver_three)):
        ver_three = ver_three[:-2] + upper_alpha[int(length)%27] + ver_three[-1:]
        print("upper entered")
    upp_met = 1
    if num_met == 0 and not(re.search('[0-9]', ver_three)):
        ver_three = ver_three[:-3] + num_alpha[int(length)%10] + ver_three[-2:]
        print("nums entered")
    num_met = 1
    if spec_met == 0 and not(re.search('[!@#$%^&*()\-_]', ver_three)):
        ver_three = ver_three[:-4] + spec_alpha[int(length)%12] + ver_three[-3:]
        print("spec entered")
    spec_met = 1
            
    return ver_three


def Decimal_to_hexdecimal(Dec):
    return int(Dec, 16)
