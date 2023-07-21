import json
from encrypt_tcp import Encrypted_Decrypted
import socket


class Client:
    def __init__(self):
        self.port = 'localhost'
        self.host = 1232
        self.sms = Encrypted_Decrypted()

    def connect_server(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.port, self.host))
        return client

    def input_checking(self):
        print("\tEmail sent and receive")
        user_option = input('press login => Sing In Form\npress reg => Registration Form\nEnter some data:')
        if user_option == "reg":
            self.user_register()
        elif user_option == "login":
            self.user_login()
        else:
            print("Invalid option")

    def check_email(self, email):
        sms = "check_email" + " " + email
        rev_from_server = self.sentEncrypt_and_recvDecrypt(sms)
        if rev_from_server == "email_exist":
            return 0
        elif rev_from_server == "no_email":
            return 1

    def sentEncrypt_and_recvDecrypt(self, sms):
        key = '@$key-random'
        client = self.connect_server()
        sms_encrypt = self.sms.start_encrypted(sms, key)
        client.send(bytes(sms_encrypt, 'utf-8'))
        from_server = client.recv(4096).decode('utf-8')
        sms_decrypt = self.sms.start_decrypted(from_server)
        return sms_decrypt

    def email_validate(self, email):
        flag = 1
        num = 0
        i = email[0]
        if 47 < ord(i) < 58:  # cannot start 0,1,...,9
            flag = -1
        # print("f ch check: ", flag)

        if len(email) > 1:
            for i in range(len(email)):
                if email[i] == "@":
                    num = i

        email_name = email[0:num]  # email_name
        email_form = email[num:]  # @gmail.com
        if flag != -1:
            for i in email_name:
                if (31 < ord(i) < 48) or (57 < ord(i) < 65) or (90 < ord(i) < 97) or (122 < ord(i) < 128):
                    flag = -1
                    break

        domain_form = ["@facebook.com", "@ncc.com", "@mail.ru", "@yahoo.com", "@outlook.com", "@apple.com", "@zoho.com",
                       "@gmail.com"]
        email_check = -1
        for i in range(len(domain_form)):
            if domain_form[i] == email_form:
                email_check = 1
                break

        if flag == 1 and email_check == 1:
            return 1  # valid email
        else:
            return 0  # invalid email

    def user_register(self):
        flag = 1
        print("\tRegistration Form")
        while flag:
            email = input('Enter your email: ')
            email_valid = self.email_validate(email)
            if email_valid:
                print("email is valid")
                check_email = self.check_email(email)
                if check_email == 1:
                    flag = 0
                    name = input('Enter your name: ')
                    password = input('Enter your password: ')
                    send_server = 'reg' + ' ' + name + ' ' + email + ' ' + password
                    rev_from_server = self.sentEncrypt_and_recvDecrypt(send_server)
                    if rev_from_server == "success":
                        print("Registration successfully!")
                        self.user_login()
                    else:
                        print("Registration fail!, try again!")
                        self.user_register()
                else:
                    print("email already register!")
            else:
                print("email is invalid!")

    def user_login(self):
        print("\tLogin From")
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        send_server = 'login' + ' ' + email + ' ' + password
        rev_from_server = self.sentEncrypt_and_recvDecrypt(send_server)
        if rev_from_server == "authorize":
            print("Login successfully!")
            self.profile()
        elif rev_from_server == "fail":
            print("Login fail")
            self.input_checking()

    def profile(self):
        print("\tUser Profile")
        option = input("press 1 => send mail\npress 2 => show all mail\npress 3 => main_option\nEnter some data: ")

        if option == "1":
            self.send_mail()
        elif option == "2":
            self.show_mail()
        elif option == "3":
            self.input_checking()
        else:
            print("Invalid Option")
            self.profile()

    def send_mail(self):
        print("\tSent mail")
        email = input("to: ")
        txt = input("Subject: ")

        sms = 'mail' + ' ' + email + ' ' + txt
        rev_from_server = self.sentEncrypt_and_recvDecrypt(sms)
        if rev_from_server == "success":
            print("mail sent success!")
            while True:
                option = input("press 1 for sent again:\n2 for main_option\n3 for exit\nEnter some data: ")
                if option == '1':
                    self.send_mail()
                elif option == '2':
                    self.input_checking()
                elif option == '3':
                    exit(1)
                else:
                    print("Invalid option")
        elif rev_from_server == "fail":
            print("email is not found!")
            while True:
                option = input("press 1 for sent again:\n2 for main_option\n3 for exit\nEnter some data: ")
                if option == '1':
                    self.send_mail()
                elif option == '2':
                    self.input_checking()
                elif option == '3':
                    exit(1)
                else:
                    print("Invalid option")

    def show_mail(self):
        print("\tReceive mail")
        sms = 'show_mail'
        rev_from_server = self.sentEncrypt_and_recvDecrypt(sms)
        mail: dict = json.loads(rev_from_server)

        if len(mail) == 0:
            print("no mail")
            self.profile()
        else:
            for i in mail:
                for j in mail[i]:
                    print(f"from: {i}\n     inbox:{j}")
            while True:
                option = input("press 1 => send mail\npress 2 => main_option\nEnter some data: ")

                if option == "1":
                    self.send_mail()
                elif option == "2":
                    self.input_checking()
                else:
                    print("Invalid Option")


if __name__ == '__main__':
    cl = Client()
    while True:
        cl.input_checking()
