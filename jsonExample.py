import json
import requests


s = requests.get("http://dev.hyvesolutions.org/hyve-mock-service/asset");
print('json return result data type is %s',type(json))
for item in s.json():
    print(type(item))
    print("key of first level json data is "+item.keys())
    print("key of second level json data is "+item['items'][0])
    for part in item['items']:
        print(part['partNo'])
pass

