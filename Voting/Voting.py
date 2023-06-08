class Voting:
    def __init__(self):
        self.db: dict = {}
        self.voter: dict = {}  # store voter.txt vote list
        self.id = 0
        self.user_id = 0
        self.vote_id = -1

        self.players = {0: {"name": "Haland", "v_mark": 0, "voter": []},
                        1: {"name": "Neymar", "v_mark": 0, "voter": []},
                        2: {"name": "Mbappe", "v_mark": 0, "voter": []},
                        3: {"name": "Ronaldo", "v_mark": 0, "voter": []},
                        4: {"name": "Messi", "v_mark": 0, "voter": []}
                        }

    def main_selector(self):
        option = 0
        try:
            option = int(input("~Press 1 to Register: \n~Press 2 to Login: \n~Press 3 to Exit: "))
        except Exception as err:
            print("Pls insert only Integer eg:1,2,3")
            self.main_selector()

        if option == 1:
            self.registration()
        elif option == 2:
            self.login()
        elif option == 3:
            exit(1)
        else:
            print("Invalid Option")
            self.main_selector()

    def registration(self):
        print(self.db)
        global phone
        input_check = -1
        pass_check = False
        phone_check = False
        try:
            print("Registration Form")
            while input_check == -1:
                name = input("~Enter your name: ")
                if name == self.user_input_check(name):
                    print("name is exit!")
                else:
                    input_check = 1
            while input_check == 1:
                email = input("~Enter your email: ")
                if email == self.user_input_check(email):
                    print("email is exit!")
                else:
                    input_check = -1

            address = input("~Enter your address: ")

            while phone_check is False:
                try:
                    phone = int(input("~Enter your phone number: "))
                    phone_check = True
                except Exception as err:
                    print("Plz fill number!")

            while pass_check is False:
                pass1 = input("Enter your password: ")
                pass2 = input("Retype your password again: ")

                if pass1 != pass2:
                    print("your password incorrect")
                else:
                    self.id = len(self.db)
                    user_data = {
                        self.id: {'name': name, 'email': email, 'address': address, 'phone': phone, 'password': pass1}}
                    self.db.update(user_data)
                    self.upload_data()
                    pass_check = True


        except Exception as err:
            print(err)
            self.registration()
        print("Registration success")

        r_option = False
        while r_option is False:
            try:
                user_option = int(input("~Press 1 to Login: \n~Press 2 Main Option: \n~Press3 to Exit: "))
                if user_option == 1:
                    self.login()
                    break
                elif user_option == 2:
                    self.main_selector()
                    break
                elif user_option == 3:
                    exit(1)
                else:
                    print("Pls read again for option!")

            except Exception as err:
                print("Invalid Input!", err)

    def user_input_check(self, key):
        for i in range(len(self.db)):
            if key == self.db[i]["email"]:
                return key
            elif key == self.db[i]["name"]:
                return key

    def login(self):
        print("--Login Form--")

        email = input("~Enter your email: ")
        password = input("~Enter your password: ")
        length = len(self.db)
        for i in range(length):
            if self.db[i]['email'] == email and self.db[i]['password'] == password:
                self.user_id = i
                if self.user_id != -1:
                    print("Login Success!")
                    self.user_profile(self.user_id)
                else:
                    print("Login Fail!")
                    self.login()

    def user_profile(self, id):
        vote_check = False
        print("Welcome", self.db[id]['name'])

        print("--Voter for players--")
        for i in range(len(self.players)):
            print(f"Id: {i}, Name: {self.players[i]['name']}, Current Vote Mark: {len(self.players[i]['voter'])}, Voter: {self.players[i]['voter']}")

        while vote_check is False:
            try:
                vote_id = int(input("Press 5 Main Option: \n Input id for vote player: "))
                if vote_id == 5:
                    self.main_selector()
                vote_check = True
                voter = self.players[vote_id]['voter']
                voter.append(self.db[self.user_id]['name'])
                print(f"{self.db[self.user_id]['name']} is voted {self.players[vote_id]['name']}")

            except Exception as err:
                print(err)

        while True:
            try:
                self.upload_vote()
                vote_option = int(input("Press 1 to Vote Again!\nPress 2 to get Main Option!\nPress 3 to Force Quit:"))

                if vote_option == 1:
                    self.user_profile(self.user_id)
                    break
                elif vote_option == 2:
                    self.main_selector()
                    break
                elif vote_option == 3:
                    exit(1)
                else:
                    print("Invalid option after vote!")
            except Exception as err:
                print(err)
        print(self.players[self.vote_id]['voter'])

    def file_create(self):
        with open("user_list", 'a') as dbfile:
            pass
        with open("voter", 'a') as dbfile:
            pass

    def upload_data(self):
        with open("user_list", "w") as file:
            for i in range(len(self.db)):
                name = self.db[i]['name']
                email = self.db[i]['email']
                address = self.db[i]['address']
                phone = self.db[i]['phone']
                password = self.db[i]['password']

                data = name + ' ' + email + ' ' + address + ' ' + str(phone) + ' ' + password + ' ' + '\n'
                file.write(data)

    def loading_data(self):
        with open("user_list", "r") as file:
            data = file.readlines()
            for a in data:
                res = a.split(" ")
                id = len(self.db)
                upload_data = {
                    id: {'name': res[0], 'email': res[1], 'address': res[2], 'phone': res[3], 'password': res[4]}}
                self.db.update(upload_data)

            # print(self.db)

    def upload_vote(self):
        with open("voter", "w") as file:
            for a in range(len(self.players)):
                res: list = self.players[a]['voter']
                for voter in res:
                    file.write(voter)
                    file.write(' ')
                file.write('\n')

    def loading_vote(self):
        with open("voter", "r") as file:
            data: list = file.readlines()

            for i in range(len(self.players)):
                if 0 < len(data):
                    voter = data[i]
                    ls: list = voter.split(' ')
                    self.players[i]['voter'] += ls[0:len(ls)-1]


if __name__ == '__main__':
    vote = Voting()
    vote.file_create()
    vote.loading_data()
    vote.loading_vote()
    vote.main_selector()
