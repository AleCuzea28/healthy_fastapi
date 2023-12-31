import requests
from PIL import Image

# from wand.image import Image
# from wand.display import display

url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"

# image_url = "https://www.thecocktaildb.com/images/media/drink/5noda61589575158.jpg"

response = requests.get(url, params={"s": "margarita"})

# data = requests.get(image_url).content

# f = open("img.jpg", "wb")
# f.write(data)
# f.close()


# def show_image():
#     img = Image.open("img.jpg")
#     img.show()
#     return img


# show_image()

# print(response)
data = response.json()
# print(data)

first_drink = data.get("drinks")[0]
second_drink = data.get("drinks")[1]

print("----------------------------------------------------")
print(first_drink.get("strDrinkThumb"))  # imagine drink
print("----------------------------------------------------")
print(second_drink.get("strDrinkThumb"))
print("----------------------------------------------------")

# print("----------------------------------------------------")
# print(data.get("explanation"))
# print("----------------------------------------------------")
# print(data.get("url"))
