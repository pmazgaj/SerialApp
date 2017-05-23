"""
Calories intake for men and women
http://www.sfd.pl/Zapotrzebowanie_kaloryczne%2C_sk%C5%82._prod._%C5%BCywno%C5%9Bciowych%2C_BF-t276436.html
NEAT = (kcal)
if endo:
    200 - 400

if ekto:
    700-900

if mezo:
    400-500

"""
import datetime


class EditUser:
    def edit(self, param):
        pass


class AddUser:
    """Handles what is done on add of user"""

    def __init__(self):
        self.list_of_users = []

    user1 = User(age=25, weight=102, height=180, st_avg_len=80, cardiovascular_count=2, cardioascular_avg_len=35,
                 neat=600)
    user2 = User(age=20, weight=60, height=180, st_avg_len=45, cardiovascular_count=0, cardioascular_avg_len=0,
                 neat=900)

    users = [user1, user2]
    trainings = [Training(length=60), Training(length=45), Training(length=80)]
    for user in users:

    for user in users:
        Calculations(user)
        for training in trainings:
            user.set_training(training)
        print(user)
    user1.tdee = 3000

    print(users)


class Training:
    """Describe training"""

    def __init__(self, length: int = 60):
        self.id = id
        self.date_of_training = datetime.datetime.now()
        self.length = length

    def get_training(self):
        return Training(self.length)

    def __repr__(self):
        return 'id: {}\ndate: {}'.format(self.id, self.date_of_training)


class Calculations:
    def __init__(self, user):
        self.id = id
        self.user = user
        self.user.tdee = self.calculate_calories_intake()

    def calculate_calories_intake(self):
        """Calculate calories intake for user"""
        bmr = ((9.99 * self.user.weight) + (6.25 * self.user.height) - (4.92 * self.user.age) + self.user.bmr_extra)

        # 4 - 7 % bmr
        calories_burnt_after_training = 0.07
        epoc = self.user.strength_trainings * calories_burnt_after_training * bmr

        # cardio - light - 5 cal, medium - 35 cal, high - 180 cal after training
        # cardio per minute - 5-10 cal (light - intense)
        calories_in_minute = 5

        cardio = 5 + calories_in_minute * self.user.cardio_count * self.user.cardio_avg_len

        # 7-9 kcal per minute
        calories_per_minute = 9
        tea = epoc + calories_per_minute * self.user.strength_trainings * self.user.st_avg_len + cardio

        self.user.neat += tea / 7 + bmr

        # 6 - 10 % of neat
        term_effect = 0.1
        tef = term_effect * self.user.neat
        tdee = tef + self.user.neat

        return tdee


class User:
    ID = 0

    def __init__(self, gender: str = 'm', age: int = 20, weight: int = 3, height: int = 44, strength_trainings: int = 4,
                 st_avg_len: int = 60, cardiovascular_count: int = 0, cardioascular_avg_len: int = 0, neat: int = 900):
        self.ID += 1
        self.id = self.ID
        self.date_of_creation = datetime.datetime.now()
        self.weight = weight
        self.height = height
        self.age = age
        self.bmr_extra = 5 if gender == 'm' else -161
        self.strength_trainings = strength_trainings
        self.st_avg_len = st_avg_len
        self.cardiovascular_count = cardiovascular_count
        self.cardiovascular_avg_len = cardioascular_avg_len
        self.neat = neat
        self.tdee = None

        self.list_of_trainings = []

    def set_training(self, training):
        self.list_of_trainings.append(training)

    def __str__(self):
        return "id: {} weight: {} height: {} age: {}\nTDEE: {}\ntrainings: {}".format(self.id, self.weight, self.height,
                                                                                      self.age,
                                                                                      self.tdee, self.list_of_trainings)

    def __repr__(self):
        return "id: {} weight: {} height: {} age: {}\nTDEE: {}\ntrainings: {}".format(self.id, self.weight, self.height,
                                                                                      self.age,
                                                                                      self.tdee, self.list_of_trainings)

# user =
# user.calculate_calories_intake()
# print(user.tdee)
# a = calculate_calories_intake(waga=60, wzrost=180, wiek=20, trening_silowy=3, czas_trwania=45, neat=900)
