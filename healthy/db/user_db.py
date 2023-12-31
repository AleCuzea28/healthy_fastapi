from domain.user import User
from fastapi.responses import FileResponse
from collections import namedtuple

import sqlite3
import requests
import json
import datetime
import matplotlib.pyplot as plt
import numpy as np


def customMealDecoder(mealDict):
    return namedtuple("X", mealDict.keys())(*mealDict.values())


DATABASE_NAME = "users.db"
TABLE_NAME = "user"
MEALS_TABLE = "meals"


class UserDb:
    def sql_connection(self):
        con = sqlite3.connect(DATABASE_NAME, check_same_thread=False)
        return con

    def sql_cursor(self):
        cur = self.sql_connection().cursor()
        return cur

    def create_table_user(self):
        conn = self.sql_connection()
        curs = conn.cursor()

        try:
            curs.execute(
                f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (username text PRIMARY KEY, email text NOT NULL UNIQUE, height float, weight float, birthdate date);"
            )
            conn.close()
        except:
            pass

    # ----------------> task 1
    def create_user_db(self, user: User):
        conn = self.sql_connection()
        curs = conn.cursor()

        user_data = (
            user.username,
            user.email,
            user.height,
            user.weight,
            user.birthdate,
        )

        curs.execute(
            f"INSERT INTO {TABLE_NAME}(username, email, height, weight, birthdate) VALUES(?, ?, ?, ?, ?)",
            user_data,
        )
        conn.commit()
        conn.close()
        return {"message": f"Successfully added {user.username}"}

    # ----------------> task 2
    def get_user_db(self):
        conn = self.sql_connection()
        curs = conn.cursor()

        data_from_db = curs.execute(f"SELECT username, email from {TABLE_NAME}")
        result = data_from_db.fetchall()
        conn.close()
        # users_dict = [User(*tuple_values).__dict__ for tuple_values in result]
        return result

    # ----------------> task 3
    def get_user_custom(self, username: str):
        """Display a single user based on its username (+age)"""
        conn = self.sql_connection()
        curs = conn.cursor()
        data_from_db = curs.execute(
            f"SELECT *, strftime('%Y', 'now') - strftime('%Y', birthdate) - (strftime('%m-%d', 'now') < strftime('%m-%d', birthdate)) AS age FROM {TABLE_NAME} WHERE username=?",
            (username,),
        )
        conn.commit()
        result = data_from_db.fetchall()
        conn.close()
        return result

    # ----------------> task 4
    def delete_user_db(self, username):
        conn = self.sql_connection()
        curs = conn.cursor()

        curs.execute(f"DELETE FROM {TABLE_NAME} WHERE username=?", (username,))
        conn.commit()
        conn.close()
        return {"message": f"Successfully deleted {username}"}

    # ----------------> task 5
    def update_user(self, user: User):
        conn = self.sql_connection()
        curs = conn.cursor()

        curs.execute(
            f"UPDATE {TABLE_NAME} SET email=?,height=?,weight=? WHERE username=?",
            (
                user.email,
                user.height,
                user.weight,
                user.username,
            ),
        )
        conn.commit()

        return {"message": "Data is modified"}

    # ----------------> task 6
    def create_user_meal(self, username, datemeal, mealname):
        conn = self.sql_connection()
        curs = conn.cursor()

        api_url = "https://api.api-ninjas.com/v1/nutrition?query={}".format(mealname)
        response = requests.get(
            api_url, headers={"X-Api-Key": "MQbXLgW3YGa/cFMFC63ipg==diQGQcOQNBLJZ26z"}
        )

        if response.status_code == requests.codes.ok:
            meal = json.loads(
                response.text[1 : len(response.text) - 1], object_hook=customMealDecoder
            )
            meal_data = (
                username,
                datemeal,
                mealname,
                meal.calories,
                meal.serving_size_g,
                meal.fat_total_g,
                meal.fat_saturated_g,
                meal.protein_g,
                meal.sodium_mg,
                meal.potassium_mg,
                meal.cholesterol_mg,
                meal.carbohydrates_total_g,
                meal.fiber_g,
                meal.sugar_g,
            )
            data = "(username, mealdate, name,calories,serving_size_g,fat_total_g,fat_saturated_g,protein_g,sodium_mg,potassium_mg,cholesterol_mg,carbohydrates_total_g,fiber_g,sugar_g)"
            data_from_db = curs.execute(
                f"INSERT INTO {MEALS_TABLE}{data} VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                meal_data,
            )
            conn.commit()
            result = data_from_db.fetchall()
            conn.close()
            return result
        else:
            print("Error:", response.status_code, response.text)

    # ----------------> task 7
    def get_meal_time(self, username, startdate, enddate):
        conn = self.sql_connection()
        curs = conn.cursor()

        data_from_db = curs.execute(
            f"SELECT * from {MEALS_TABLE} WHERE username=? and DATE(mealdate) BETWEEN ? AND ?",
            (username, startdate, enddate),
        )
        result = data_from_db.fetchall()
        conn.close()

        return result

    # ----------------> task 8
    def delete_meal_today(self, username, mealname):
        conn = self.sql_connection()
        curs = conn.cursor()

        current_date = datetime.datetime.now().date().strftime("%Y-%m-%d")

        data_from_db = curs.execute(
            f"DELETE FROM {MEALS_TABLE} WHERE username=? and name=? and date(mealdate) = date(?)",
            (
                username,
                mealname,
                current_date,
            ),
        )
        conn.commit()
        result = data_from_db.fetchall()
        conn.close()
        return current_date, username, mealname, result

    # ----------------> task 9
    def modify_meal(self, username, mealname_old, mealname_new, day):
        conn = self.sql_connection()
        curs = conn.cursor()

        current_date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        yesterday = (
            datetime.datetime.now().date() - datetime.timedelta(days=1)
        ).strftime("%Y-%m-%d")

        api_url = "https://api.api-ninjas.com/v1/nutrition?query={}".format(
            mealname_new
        )
        response = requests.get(
            api_url, headers={"X-Api-Key": "MQbXLgW3YGa/cFMFC63ipg==diQGQcOQNBLJZ26z"}
        )

        if response.status_code == requests.codes.ok:
            meal = json.loads(
                response.text[1 : len(response.text) - 1], object_hook=customMealDecoder
            )

            data = "(username, mealdate, name,calories,serving_size_g,fat_total_g,fat_saturated_g,protein_g,sodium_mg,potassium_mg,cholesterol_mg,carbohydrates_total_g,fiber_g,sugar_g)"
            data_from_db = curs.execute(
                f"UPDATE {MEALS_TABLE} SET name=?,calories=?,serving_size_g=?,fat_total_g=?,fat_saturated_g=?,protein_g=?,sodium_mg=?,potassium_mg=?,cholesterol_mg=?,carbohydrates_total_g=?,fiber_g=?,sugar_g=? WHERE username=? and name=? and date(mealdate) = date(?)",
                (
                    mealname_new,
                    meal.calories,
                    meal.serving_size_g,
                    meal.fat_total_g,
                    meal.fat_saturated_g,
                    meal.protein_g,
                    meal.sodium_mg,
                    meal.potassium_mg,
                    meal.cholesterol_mg,
                    meal.carbohydrates_total_g,
                    meal.fiber_g,
                    meal.sugar_g,
                    username,
                    mealname_old,
                    current_date,
                ),
            )
            conn.commit()
            result = data_from_db.fetchall()
            conn.close()
            return result
        else:
            print("Error:", response.status_code, response.text)

        conn.commit()
        result = data_from_db.fetchall()
        conn.close()
        return current_date, username, result
        return

    # ----------------> task 10
    def get_calories_given_day(self, username, day):
        conn = self.sql_connection()
        curs = conn.cursor()

        data_from_db = curs.execute(
            f"SELECT SUM(calories), SUM(serving_size_g), SUM(fat_total_g), SUM(fat_saturated_g), SUM(protein_g), SUM(sodium_mg), SUM(potassium_mg), SUM(cholesterol_mg), SUM(carbohydrates_total_g), SUM(fiber_g), SUM(sugar_g) from {MEALS_TABLE} WHERE username=? and date(mealdate) = date(?) ",
            (
                username,
                day,
            ),
        )
        result = data_from_db.fetchall()
        conn.close()

        return result

    # ----------------> task 11
    def get_chart(self, username, start, end):
        conn = self.sql_connection()
        curs = conn.cursor()

        data_from_db = curs.execute(
            f"SELECT SUM(calories), SUM(serving_size_g), SUM(fat_total_g), SUM(fat_saturated_g), SUM(protein_g), SUM(sodium_mg), SUM(potassium_mg), SUM(cholesterol_mg), SUM(carbohydrates_total_g), SUM(fiber_g), SUM(sugar_g) from {MEALS_TABLE} WHERE username=? and DATE(mealdate) BETWEEN ? AND ? ",
            (
                username,
                start,
                end,
            ),
        )
        result = data_from_db.fetchall()
        conn.close()

        y = np.array(result)
        mylabels = [
            "calories",
            "serving_size_g",
            "fat_total_g",
            "fat_saturated_g",
            "protein_g",
            "sodium_mg",
            "potassium_mg",
            "cholesterol_mg",
            "carbohydrates_total_g",
            "fiber_g",
            "sugar_g",
        ]
        y_flattened = y.flatten()
        plt.pie(y_flattened, labels=mylabels)
        plt.axis("equal")
        chart_filename = "pie_chart.png"
        plt.savefig(chart_filename)

        return FileResponse("pie_chart.png")


# con = sqlite3.connect(DATABASE_NAME, check_same_thread=False)
# cur = con.cursor()

# # cur.execute(
# #     f"CREATE TABLE IF NOT EXISTS {MEALS_TABLE} (username, mealdate, name,calories,serving_size_g,fat_total_g,fat_saturated_g,protein_g,sodium_mg,potassium_mg,cholesterol_mg,carbohydrates_total_g,fiber_g,sugar_g);"
# # )

# cur.execute(
#     f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (username, email, height,weight,birthdate);"
# )

# res = cur.execute(f"PRAGMA table_info({MEALS_TABLE})")
# print(res.fetchone())
# con.close()
