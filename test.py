import requests

response = requests.get('http://quera.ir')

# status code : 

# print(response.status_code)

# text ==>> its return html code of that site : 

# print(response.text)

# request : determine the type of requests as preparedRequests

# print(response.request)

# json() : return json file if its exsits 

# print(response.json())

# url : return the url of site that you entered 

# print(response.url)

# encodeing : determine the type of encoding way 

# print(response.encoding)

#headers : keep significent information as dict 

print(response.headers)