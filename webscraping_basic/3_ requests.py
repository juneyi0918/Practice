import requests



res = requests.get("http://google.com")
res.raise_for_status()

# print("status code: ", res.status_code )  # 200 is normal

# if res.status_code == requests.codes.ok:
#     print("Noraml")
# else:
#     print("Problem occurred. [Error Code ", res.status_code, "]" )

print(len(res.text)) 

with open("mygoogle.html", "w", encoding = "utf8") as f:
    f.write(res.text)