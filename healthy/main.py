from fastapi import FastAPI
from api.users import user_router

from api.cocktail import cocktail_router
from api.finance import finance_router
import uvicorn

app = FastAPI()
app.include_router(user_router)
app.include_router(cocktail_router)
app.include_router(finance_router)

if __name__ == "__main__":
    uvicorn.run(
        app,
        port=8080,
        host="0.0.0.0",
    )
