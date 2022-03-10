
import requests

def process(url):
    try :
       response = requests.get(url)
       myJson_file = response.json()
       if len(myJson_file) == 0 :
           return "I can't recognize file"
       nameHolder = myJson_file[0]['category']
       counter = 0 
       for i in range(len(myJson_file)) :
           if myJson_file[i]['category'] == nameHolder :
                counter += 1
        
       if counter == len(myJson_file) :
           return nameHolder
       else : 
           return "I can't recognize file"

    except:
       return "Bad Query"
    


pass

process('https://mysafeinfo.com/api/data?list=englishmonarchs&format=json')
