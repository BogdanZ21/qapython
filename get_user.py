import requests

response = requests.get("https://www.klerk.ru/yindex.php/v4/user/view?id=2251495")
print(response.text)