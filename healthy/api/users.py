from fastapi import APIRouter
from domain.user import User
from domain.user_repo import UserRepository
from db.user_db import UserDb
from db.user_file import UserFile
import logging
import datetime
import json


logging.basicConfig(
    filename="finance.log",
    level=logging.DEBUG,
    format="%(asctime)s _ %(levelname)s _ %(name)s _ %(message)s",
)


def logging_info():
    logging.info("Mesajjjjj")


config_path = "config.json"

user_router = APIRouter(prefix="/users", tags=["user"])


def read_persistence_file():
    user_obj = UserFile()
    return user_obj
    # with open(config_path) as json_file:
    #     data = json.load(json_file)
    #     if data.get("persistence_type") == "sql":
    #         user_obj = UserDb()
    #     elif data.get("persistence_type") == "json":
    #         user_obj = UserFile()
    # return user_obj


user_return = read_persistence_file()

user_obj = UserRepository(user_return)


# ----------------> task 1
@user_router.post("/task1")
async def create_user_with_fields(user: User):
    return user_obj.create_user(user)


# ----------------> task 2
@user_router.get("/task2")
async def get_users_with_username_and_email():
    logging_info()
    return user_obj.get_user()


# ----------------> task 3
@user_router.get("/task3")
async def get_users_custom(username: str):
    return user_obj.get_user_custom(username)


# ----------------> task 4
@user_router.delete("/task4")
async def delete_user_based_on_username(username: str):
    return user_obj.delete_user(username)


# ----------------> task 5
@user_router.put("/task5")
async def update_user_data_except_username(user: User):
    return user_obj.update_user(user)


# ----------------> task 6
@user_router.post("/task6")
async def create_user_meal_to_a_users_profile(
    username: str, mealdate: datetime.date, mealname: str
):
    return user_obj.create_user_meal(username, mealdate, mealname)


# ----------------> task 7
@user_router.get("/task7")
async def get_meals_on_a_period_of_time(
    username: str, startdate: datetime.date, enddate: datetime.date
):
    return user_obj.get_meal_time(username, startdate, enddate)


# ----------------> task 8
@user_router.delete("/task8")
async def delete_meal_from_today(username: str, mealname: str):
    return user_obj.delete_meal_today(username, mealname)


# ----------------> task 9
@user_router.patch("/task9")
async def edit_a_meal_from_the_same_day(
    username: str, mealname_old: str, mealname_new: str, day: datetime.date
):
    return user_obj.modify_meal(username, mealname_old, mealname_new, day)


# ----------------> task 10
@user_router.get("/task10")
async def get_total_calories_from_a_given_day(username: str, day: datetime.date):
    return user_obj.get_calories_given_day(username, day)


# ----------------> task 11
@user_router.get("/task11")
async def show_chart_based_on_user_meal_values(
    username: str, start: datetime.date, end: datetime.date
):
    return user_obj.get_chart(username, start, end)
