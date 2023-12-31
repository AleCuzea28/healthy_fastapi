from domain.user import User
import datetime


class UserRepository:
    def __init__(self, object):
        self.__persistence = object

    # ----------------> task 1
    def create_user(self, user: User):
        return self.__persistence.create_user_db(user)

    # ----------------> task 2
    def get_user(self):
        return self.__persistence.get_user_db()

    # ----------------> task 3
    def get_user_custom(self, username: str):
        return self.__persistence.get_user_custom(username)

    # ----------------> task 4
    def delete_user(self, username: str):
        return self.__persistence.delete_user_db(username)

    # ----------------> task 5
    def update_user(self, user: User):
        return self.__persistence.update_user(user)

    # ----------------> task 6
    def create_user_meal(self, username: str, datemeal: datetime.date, mealname: str):
        return self.__persistence.create_user_meal(username, datemeal, mealname)

    # ----------------> task 7
    def get_meal_time(
        self, username: str, start_date: datetime.date, end_date: datetime.date
    ):
        return self.__persistence.get_meal_time(username, start_date, end_date)

    # ----------------> task 8
    def delete_meal_today(self, username: str, mealname: str):
        return self.__persistence.delete_meal_today(username, mealname)

    # ----------------> task 9
    def modify_meal(
        self, username: str, mealname_old: str, mealname_new: str, day: datetime.date
    ):
        return self.__persistence.modify_meal(username, mealname_old, mealname_new, day)

    # ----------------> task 10
    def get_calories_given_day(self, username: str, day: datetime.date):
        return self.__persistence.get_calories_given_day(username, day)

    # ----------------> task 11
    def get_chart(self, username: str, start: datetime.date, end: datetime.date):
        return self.__persistence.get_chart(username, start, end)


# define a User object with private fields
# # accessed with property decorators
# # user repo receives in constructor an object which know how to save the users in a file or db
# in db folder create 2 classes, one for file, one for db
# create a condig.json in which we tell what type if persistence we have
