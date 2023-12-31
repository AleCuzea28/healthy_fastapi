import requests

query = "fries"
api_url = "https://api.api-ninjas.com/v1/nutrition?query={}".format(query)
response = requests.get(
    api_url, headers={"X-Api-Key": "MQbXLgW3YGa/cFMFC63ipg==diQGQcOQNBLJZ26z"}
)
if response.status_code == requests.codes.ok:
    leng = len(response.text)
    print(response.text[1 : leng - 1])

else:
    print("Error:", response.status_code, response.text)
