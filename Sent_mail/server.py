import json
import socket
import pymongo
from encrypt_tcp import Encrypted_Decrypted

# connection to db
conn = pymongo.MongoClient("localhost", 27017)
database = conn["encrypted_mail"]
user = database['user']


class Server:
    def __init__(self):
        self.host = 'localhost'
        self.port = 1232
        self.sms = Encrypted_Decrypted()
        self.login_email = ''

    def run_server(self):
        connect_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect_server.bind((self.host, self.port))
        connect_server.listen()
        print(f'*** Running server at host: {self.host}, port: {self.port} *** ')
        while True:
            self.client_runner(connect_server)

    def client_runner(self, connect_server):
        client, address = connect_server.accept()
        print(f"Connection from client {address[0]} , {address[1]}")

        with client as sok:
            from_client: list = sok.recv(4096).decode('utf-8')
            from_client: str = self.sms.start_decrypted(from_client).split(" ")
            print(from_client)
            if from_client[0] == "reg":
                self.create(from_client, sok)
            elif from_client[0] == "login":
                self.authentication(from_client, sok)
            elif from_client[0] == "mail":
                self.store_mail(from_client, sok)
            elif from_client[0] == "show_mail":
                self.view_mail(sok)
            elif from_client[0] == "check_email":
                self.check_email_db(from_client[1], sok)

    def create(self, sms, sock):
        user_data = {"name": sms[1], "email": sms[2], "password": sms[3], "mail": {sms[2]: {}}}
        user.insert_one(user_data)
        sms = self.sms.start_encrypted("success", 'random_key')
        sock.send(bytes(sms, 'utf-8'))

    def authentication(self, sms, sock):
        check = -1
        email = sms[1]
        password = sms[2]
        for i in user.find({}, {"email": 1, "password": 1}):
            if i["email"] == email and i["password"] == password:
                check = 1
                self.login_email = email
                break
        if check == 1:
            sms = self.sms.start_encrypted("authorize", 'random_key')
            sock.send(bytes(sms, "utf-8"))
        else:
            sms = self.sms.start_encrypted("fail", 'random_key')
            sock.send(bytes(sms, "utf-8"))

    def store_mail(self, sms, sock):
        email = sms[1]
        txt: list = sms[2:]
        txt_str = ''
        for i in txt:
            if len(txt) > 1:
                txt_str += i + ' '
            else:
                txt_str = i
        dict_email = {email: {}}
        flag = -1
        old_query = {}
        for i in user.find({}, {"mail": 1}):
            if i["mail"].keys() == dict_email.keys():
                old_query.update(i["mail"])
                break

        new_query = {}
        for i in user.find({}, {"mail": 1}):
            if i["mail"].keys() == dict_email.keys():
                new_query.update(i["mail"][email])
                break

        for key in new_query:
            if key == self.login_email:
                flag = 1  #
        print("db in",old_query)
        print("up for",new_query)
        print("flag", flag)
        if flag == 1:
            new_query[self.login_email].append(txt_str)
            a = {"mail": old_query}
            b = {"$set": {"mail": {email: new_query}}}
            print(a)
            print(b)
            user.update_one(a, b)
            sent_client = self.sms.start_encrypted("success", 'hack_key')
            sock.send(bytes(sent_client, 'utf-8'))
        else:
            new_query.update({self.login_email: [txt_str]})
            user.update_one({"mail": old_query}, {"$set": {"mail": {email: new_query}}})
            sent_client = self.sms.start_encrypted("success", 'hack_key')
            sock.send(bytes(sent_client, 'utf-8'))

    def view_mail(self, sock):
        print("login mail", self.login_email)
        for i in user.find({"email": self.login_email}):
            data_str = json.dumps(i["mail"][self.login_email])
            sms = self.sms.start_encrypted(data_str, 'random_key')
            sock.send(bytes(sms, 'utf-8'))

    def check_email_db(self, email, sock):
        check = -1
        for i in user.find({}, {"email": 1}):
            if i["email"] == email:
                check = 1
        if check == 1:
            sms = "email_exist"
            sms = self.sms.start_encrypted(sms, 'random_key')
            sock.send(bytes(sms, 'utf-8'))
        else:
            sms = "no_email"
            sms = self.sms.start_encrypted(sms, 'random_key')
            sock.send(bytes(sms, 'utf-8'))


if __name__ == '__main__':
    server = Server()
    server.run_server()
