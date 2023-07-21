import json


class Account_Note:
    def __init__(self):
        self.note = {}

    def main_menu(self):
        print("\tPassword Manager")
        try:
            option = int(
                input(
                    'press 1 => save site note\npress 2 => show note\npress 3 => update\npress 4 => exit\nEnter option number:'))

            if option == 1:
                self.save_note()
            elif option == 2:
                self.view()
            elif option == 3:
                self.update_note()
            elif option == 4:
                print('bye')
                exit(1)
            else:
                self.main_menu()
        except Exception as err:
            print('Option wrong, read again!')

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

    def save_note(self):
        email_check = 1
        site = ''
        email = ''
        while email_check == 1:
            print("\tAdding Note")
            site = input('Enter save for site:')
            email = input('Enter save for email: ')
            check = self.email_validate(email)
            print("check", check)
            if check == 1:
                email_check = 0
            else:
                print("Invalid email, try again!")
        password = input('Enter save for password: ')
        save_note: dict = {}
        id_ = len(save_note)
        save_note.update({id_: {"site": site, "email": email, "password": password}})
        print("Adding Note Successfully, see note for press 2")
        self.file_write_note(save_note)

    def file_write_note(self, note):
        with open("note.txt", "a") as f:
            for i in range(len(note)):
                f.writelines(note[i]["site"] + " " + note[i]["email"] + " " + note[i]["password"] + " " + "\n")

    def file_read_note(self):
        with open("note.txt", "r") as f:
            read = f.readlines()
        for i in range(len(read)):
            note: list = read[i].split(" ")
            id_ = len(self.note)
            self.note.update({id_: {"site": note[0], "email": note[1], "password": note[2]}})

    def view(self):
        self.note.clear()
        self.file_read_note()
        for i in range(len(self.note)):
            print(f'id:{i}', self.note[i])

    def update_note(self):
        update_note = {}
        self.view()
        try:
            id = int(input('press id number for update:'))
            if id < len(self.note):
                for i in range(len(self.note)):
                    update_note = self.note[id]
                    break
            else:
                print('Invalid id number, try again!')
                self.update_note()
            self.final_update(update_note, id)
        except Exception as err:
            print('enter id number, try again!')
            self.update_note()

    def final_update(self, update_note, id):
        print("Update Note")
        print(update_note)
        option = input('press 1 => site, press 2 => email, press 3 => password\nEnter option for update:')
        if option == '1':
            print('Site:', update_note['site'])
            site = input('Update site:')
            self.note.update({id: {'site': site, 'email': update_note['email'], 'password': update_note['password']}})
            print('Update successfully')
            print(self.note[id])

        elif option == '2':
            print('Email:', update_note['email'])
            email = input('Update email:')
            self.note.update({id: {'site': update_note['site'], 'email': email, 'password': update_note['password']}})
            print('Update successfully')
            print(self.note[id])
        elif option == '3':
            print('Password:', update_note['password'])
            password = input('Update password:')
            self.note.update({id: {'site': update_note['site'], 'email': update_note['email'], 'password': password}})
            print('Update successfully')
            print(self.note[id])
        else:
            print('wrong option number')
            self.final_update(update_note, id)

        with open("note.txt", "w") as f:
            for i in range(len(self.note)):
                f.writelines(
                    self.note[i]["site"] + " " + self.note[i]["email"] + " " + self.note[i]["password"] + " " + "\n")


if __name__ == '__main__':
    obj = Account_Note()
    # obj.file_read_note()
    while True:
        obj.main_menu()
