import random


# triple encrypted txt changing
class Encrypted_Decrypted:
    def __init__(self):
        self.encrypt_sms = ''
        self.random_key = random.randint(1, 1500)

    def start_encrypted(self, txt, key):
        encry_key = 0
        for i in key:
            encry_key += ord(i)  # string ch to ord
        encry_key_hex = hex(encry_key)  # int to hex

        first_encrypt = 0
        sms = ''
        for i in txt:
            first_encrypt = ord(i) ^ encry_key
            second_encrypt = first_encrypt ^ self.random_key
            final_encrypt = second_encrypt ^ self.random_key
            final_encrypt = hex(final_encrypt)  # change hex
            sms += final_encrypt + "#"
        encrypt_sms = sms + encry_key_hex + "#" + hex(self.random_key)
        # print(self.encrypt_sms)
        return encrypt_sms

    def start_decrypted(self, sms):
        encrypt_sms = sms.split("#")
        key = encrypt_sms[-2:]
        user_key = int(key[0], 16)
        random_key = int(key[1], 16)
        sms_decrypt = ''
        for i in range(len(encrypt_sms) - 2):
            first_decrypt = int(encrypt_sms[i], 16) ^ random_key
            second_decrypt = first_decrypt ^ random_key
            final_decrypt = second_decrypt ^ user_key
            sms_decrypt += chr(final_decrypt)  # change int to txt
        return sms_decrypt


# if __name__ == '__main__':
#     encrypted = Encrypted()
#     encrypted.start_encrypted("Never Give up", "ncc")
#     encrypted.start_decrypted(encrypted.encrypt_sms)
    # print(encrypted.encrypt_sms)
