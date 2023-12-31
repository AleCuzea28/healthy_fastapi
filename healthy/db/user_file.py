from domain.user import User
import json
import datetime
import requests
from fastapi.responses import JSONResponse
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from fastapi import Response
from fastapi.responses import FileResponse


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        return super().default(obj)


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


class UserFile:
    # ----------------> task 1
    def create_user_db(self, user: User):
        """Create a new user based on the given fields"""
        with open("healthy//user_db.json") as json_file:
            data = json.load(json_file)

        data.append(user.dict())

        with open("healthy//user_db.json", "w") as json_file:
            json.dump(data, json_file, indent=4, cls=DateEncoder)

        return {"message": "User added"}

    # ----------------> task 2
    def get_user_db(self):
        """Show json users with only username and email"""
        with open("healthy//user_db.json") as json_file:
            data = json.load(json_file)
            extracted_data = [
                {"username": extract["username"], "email": extract["email"]}
                for extract in data
            ]
        return extracted_data

    # ----------------> task 3
    def get_user_custom(self, username: str):
        """Display a single user based on its username (+age)"""
        with open("healthy//user_db.json") as json_file:
            data = json.load(json_file)

        for user in data:
            if user["username"] == username:
                today = datetime.date.today()
                bday_str = user["birthdate"]
                bday_object = datetime.datetime.strptime(bday_str, "%Y-%m-%d").date()
                extracted_data = {
                    "username": username,
                    "email": user["email"],
                    "height": user["height"],
                    "weight": user["weight"],
                    "age": today.year
                    - bday_object.year
                    - ((today.month, today.day) < (bday_object.month, bday_object.day)),
                }

        return extracted_data

    # ----------------> task 4
    def delete_user_db(self, username):
        """"""
        with open("healthy//user_db.json") as json_file:
            data = json.load(json_file)

        for user in data:
            if user["username"] == username:
                data.remove(user)

        with open("healthy//user_db.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        return {"message": "User deleted"}

    # ----------------> task 5
    def update_user(self, user: User):
        """edit a user, all fields are editable except username"""
        with open("healthy//user_db.json") as json_file:
            data = json.load(json_file)

        existing_user = None

        for item in data:
            if item["username"] == user.username:
                existing_user = item
                break

        existing_user["email"] = user.email
        existing_user["height"] = user.height
        existing_user["weight"] = user.weight

        with open("healthy//user_db.json", "w") as json_file:
            json.dump(data, json_file, indent=4, cls=DateEncoder)

        return {"message": "User's data modified"}

    # ----------------> task 6
    def create_user_meal(self, username, mealdate, mealname):
        """Create a new user based on the given fields"""
        with open("healthy//user_meals.json") as json_file:
            data = json.load(json_file)

        api_url = "https://api.api-ninjas.com/v1/nutrition?query={}".format(mealname)
        response = requests.get(
            api_url, headers={"X-Api-Key": "MQbXLgW3YGa/cFMFC63ipg==diQGQcOQNBLJZ26z"}
        )
        if response.status_code == requests.codes.ok:
            # leng = len(response.text) - 1
            meal = json.loads(response.text[1 : len(response.text) - 1])
            new_meal = {
                "username": username,
                "mealdate": mealdate,
                "meal": meal,
            }
            data.append(new_meal)
        else:
            print("Error:", response.status_code, response.text)

        with open("healthy//user_meals.json", "w") as json_file:
            json.dump(data, json_file, indent=4, cls=DateEncoder)

        return new_meal

    # ----------------> task 7
    def get_meal_time(
        self, username: str, start_date: datetime.date, end_date: datetime.date
    ):
        """Display a single user based on its username (+age)"""
        with open("healthy//user_meals.json") as json_file:
            data = json.load(json_file)

        query_meals = []

        for user in data:
            if user["username"] == username:
                mealdate_object = datetime.datetime.strptime(
                    user["mealdate"], "%Y-%d-%m"
                ).date()

                if mealdate_object > start_date and mealdate_object < end_date:
                    query_meals.append(user)

        return query_meals

    # ----------------> task 8
    def delete_meal_today(self, username, mealname):
        with open("healthy//user_meals.json") as json_file:
            data = json.load(json_file)

        for user_meal in data:
            if (
                user_meal["username"] == username
                and user_meal["meal"]["name"] == mealname
            ):
                if user_meal["mealdate"] == datetime.date.today().strftime("%Y-%m-%d"):
                    data.remove(user_meal)
                else:
                    return JSONResponse(
                        status_code=405,
                        content={"message": "You can only delete meals from today!"},
                    )

        with open("healthy//user_meals.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        return {"message": "User meal deleted"}

    # ----------------> task 9
    def modify_meal(self, username, mealname_old, mealname_new, day):
        with open("healthy//user_meals.json") as json_file:
            data = json.load(json_file)

        for user_meal in data:
            if (
                user_meal["username"] == username
                and user_meal["meal"]["name"] == mealname_old
            ):
                day = datetime.date.today().strftime("%Y-%m-%d")
                if user_meal["mealdate"] == day:
                    api_url = "https://api.api-ninjas.com/v1/nutrition?query={}".format(
                        mealname_new
                    )
                    response = requests.get(
                        api_url,
                        headers={
                            "X-Api-Key": "MQbXLgW3YGa/cFMFC63ipg==diQGQcOQNBLJZ26z"
                        },
                    )
                    if response.status_code == requests.codes.ok:
                        # leng = len(response.text) - 1
                        new_meal = json.loads(response.text[1 : len(response.text) - 1])
                        user_meal.update({"meal": new_meal})
                else:
                    return JSONResponse(
                        status_code=405,
                        content={"message": "You can only update meals from today!"},
                    )

        with open("healthy//user_meals.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        return {"message": "User meal modified"}

    # ----------------> task 10
    def get_calories_given_day(self, username: str, day: datetime.date):
        """Display a single user based on its username (+age)"""
        with open("healthy//user_meals.json") as json_file:
            data = json.load(json_file)

        meals_given_day = []

        for user in data:
            if user["username"] == username:
                mealdate_object = datetime.datetime.strptime(
                    user["mealdate"], "%Y-%m-%d"
                ).date()

                if mealdate_object == day:
                    meals_given_day.append(user)

        return meals_given_day

    # ----------------> task 11
    def get_chart(self, username: str, start: datetime.date, end: datetime.date):
        """Display a single user based on its username (+age)"""
        with open("healthy//user_meals.json") as json_file:
            data = json.load(json_file)

        result_dict = {}

        for user in data:
            if user["username"] == username:
                mealdate_object = datetime.datetime.strptime(
                    user["mealdate"], "%Y-%m-%d"
                ).date()

                if mealdate_object > start and mealdate_object < end:
                    for key, value in user["meal"].items():
                        if key in result_dict:
                            result_dict[key] += value
                        else:
                            result_dict[key] = value

        values_list = [value for value in result_dict.values()][1:]

        y = np.array(values_list)
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
