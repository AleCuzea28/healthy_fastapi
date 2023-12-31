# from fastapi import FastAPI
# from api.users import user_router
# import uvicorn


# app = FastAPI()
# app.include_router(user_router)


# # @app.get("/")
# # async def root():
# #     return {"message": "Hello World"}


# # ---------------------------------- made with dict of dictionaries

# # @app.post("/users")
# # async def create_user(user: User):
# #     username = user.username
# #     user_db[username] = user.dict()
# #     return {"message": f"Succesfully added : {username}"}


# # @app.get("/users")
# # async def get_users(limit: int = 20):
# #     user_list = list(user_db.values())
# #     return user_list[:limit]


# # @app.delete("/users/{username}")
# # async def delete_users(username: str):
# #     user_db.pop(username)
# #     return {"message": f"User {username} deleted successfully"}


# # @app.put("/users/{username}/{email}")
# # async def update_users(username: str, email: str):
# #     user_db[username]["email"] = email
# #     return {"message": f"User {username} updated successfully"}


# # @app.get("/")
# # async def root():
# #     return {"message": "Hello, world!"}


# if __name__ == "__main__":
#     uvicorn.run(
#         app,
#         port=8000,
#         host="0.0.0.0",
#     )


# # uvicorn main:app --reload

# # Create a user with username, email, height, weight
