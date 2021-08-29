class Requester:

    blood_requests = {"person1" : "AB+" , "person2" : "B-" , "person3" : "O+"}

    def __init__(self , name , blood_group):
        self.name = name
        self.blood_group = blood_group

    def check(self):
        if self.blood_group in Donor.blood_list.values():
            print("\nthe blood group is available you can request for it")
        else:
            print("\ncurrently the blood group is not there you will be notified if it is available")


    def request(self):
        print(self.name + " requires  " + self.blood_group + " please inform if anyone is willing to donate blood \n")
        Requester.blood_requests["self.name"] = self.blood_group


class Donor:

        blood_list = {"name1" : "A" , "name2" : "B+" , "name3" : "B-" , "name4" : "o+"}

        def __init__(self , name , bloodgroup , city):
            self.name = name
            self.bloodgroup = bloodgroup
            self.city = city

        def donate(self):
            Donor.blood_list[self.name] = self.bloodgroup




class Admin:

    blood_donating_hospitals  = ["hospital-A" , "hospital-B"]
    blood_donating_camps      = ["camp-1" , "camp-2"]

    def __init__(self , username):
        self.username = username


    def checkdonors(self):
        print("the blood donors are as follows")
        return Donor.blood_list

    def add_blood_donating_hospitals(self , name):

        Admin.blood_donating_hospitals.append(name)
        print("\nhospital " + name + " has been added and current list is :")
        return Admin.blood_donating_hospitals

    def add_blood_donating_camps(self , name2):

        Admin.blood_donating_camps.append(name2)
        print("\ncamp " + name2 + " has been added and current list is : ")

        return Admin.blood_donating_camps

    def check_requests(self):

        print("\nthe blood donation requests are as follows")
        return Requester.blood_requests


    def message(self):
            print("\nwe have sent you this notification since your blood is necessary for a patient so kindly donate your blood\n")







re1 = Requester("name10" , "B+")
re1.check()
re1.request()

do1 = Donor("nam1" , "B+" , "hyderabad")
do1.donate()

do2 = Donor("nam2" , "A-" , "Vijayawada")
do2.donate()

do3 = Donor("nam3" , "O-" , "Amaravati")
do3.donate()

do4 = Donor("nam4" , "AB+" , "Vishakapatnam")
do4.donate()

do5 = Donor("nam5" , "AB-" , "Guntur")
do5.donate()

re2 = Requester("na1" , "AB-")
re2.check()
re2.request()

re3 = Requester("na2" , "O+")
re3.check()
re3.request()


a1 = Admin("name1")
print(a1.checkdonors())
print(a1.check_requests())
print(a1.add_blood_donating_camps("vistaaaa"))
print(a1.add_blood_donating_hospitals("pure health hospital"))
a1.message()







