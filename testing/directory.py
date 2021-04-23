tempObj = {"age": 12, "name": "python"}
print(tempObj['age'])
tempObj['title'] = "哦嘿哟"
print(tempObj)
print(tempObj.keys())
print(tempObj.values())
print(tempObj.items())

for key, value in tempObj.items():
    print(key, value)
