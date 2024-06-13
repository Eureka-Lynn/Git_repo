import json

with open ('C:/Users/VBSE/Desktop/dev/1.json','r',encoding='utf-8') as f:
    data = json.load(f)
    for _ in data:
        print(_)