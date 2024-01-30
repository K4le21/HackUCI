import json
import urllib.request
   
# Opening JSON file
f = open('houses.json')
   
# returns JSON object as 
# a dictionary
data = json.load(f)
final = {}
   
# Iterating through the json
# list
for i in data:
    if i['imageURL'][-4:] == '.jpg' and i['add'] not in final:
        final[i['add']] = i['imageURL']
   
# Closing file
f.close()


for key, item in final.items():
    try:
        urllib.request.urlretrieve(item, key + '.jpg')
        print(item + ", " + key)
    except FileNotFoundError:
        print ("File failed to download.")
    except urllib.error.HTTPError:
        print ("File failed to download.")


print("Done Download!")