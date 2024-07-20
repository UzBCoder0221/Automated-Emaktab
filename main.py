import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

user_agent = UserAgent()

logins = [
    "username",
]

passwords = [
    "password",
]
isParent=False

for i in range(len(logins)):
    random_user_agent = user_agent.random
    with requests.Session() as s:
        s.headers.update({'User-Agent': random_user_agent})
        url = "https://login.emaktab.uz/?ReturnUrl=https%3a%2f%2femaktab.uz%2fuserfeed"
        data = {"login": logins[i], "password": passwords[i]}
        response = s.post(url,allow_redirects=True, data=data)
        soup = BeautifulSoup(response.content, 'html.parser')
        captcha = soup.find_all(class_='captcha')
        isSucceed = "Login successful"
        if captcha:
            isSucceed = "Login unsuccessful: Captcha required"
        print(isSucceed, ":   ",data['login'])

