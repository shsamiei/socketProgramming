
import requests

def process(book) :

    MyCategory = book["category"]
    Myname = book['name']
    

    if MyCategory == "math" :
        response = requests.get('http://127.0.0.1:8000/math/')
        my_url = 'http://127.0.0.1:8000/math/'

    if MyCategory == "physic" :
        response = requests.get('http://127.0.0.1:8000/physic/')
        my_url = 'http://127.0.0.1:8000/physic/'

    if MyCategory == "chess" :
        response = requests.get('http://127.0.0.1:8000/chess/')
        my_url = 'http://127.0.0.1:8000/chess/'

    myList = response.json()
    for i in range(len(myList)) :
         if myList[i]['name'] == Myname :
             return "bad query"

    requests.post(my_url, data = book)

    

# better way : 

# import requests

# def process(data):
#     url = "http://127.0.0.1:8000/"
#     url += data["category"]
#     url += "/"
#     response = requests.get(url)
#     books = response.json()
#     for book in books:
#         if book["name"] == data["name"]:
#             return "bad query"
#     requests.post(url, data)
 