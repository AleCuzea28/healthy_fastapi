from fastapi import APIRouter

import requests

# # # import Image

# from PIL import Image

from fastapi.responses import FileResponse, JSONResponse

cocktail_router = APIRouter(prefix="/cocktail", tags=["cocktail"])


@cocktail_router.get("/{cocktail_name}")
def get_image(cocktail_name: str):
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"

    # image_url = "https://www.thecocktaildb.com/images/media/drink/5noda61589575158.jpg"

    response = requests.get(url, params={"s": cocktail_name})

    try:
        dict = response.json().get("drinks")[0]
    except TypeError:
        return JSONResponse(status_code=404, content={"message": "Cocktail not found"})

    img_url = dict.get("strDrinkThumb")
    data = requests.get(img_url).content
    f = open("img.jpg", "wb")
    f.write(data)
    f.close()
    # img = Image.open('img.jpg')
    return FileResponse("img.jpg")


# # # config_path = "img.jpg"


# # # url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
# # # image_url = "https://www.thecocktaildb.com/images/media/drink/5noda61589575158.jpg"


# @cocktail_router.get("")
# async def show_cocktail():
#     # response = requests.get(url, params={"s": name})
#     # diction = response.json()
#     # data = diction.get()
#     img = Image.open("healthy\\api\\img.jpg")
#     return img.show()
