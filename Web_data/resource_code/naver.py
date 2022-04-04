import pandas as pd
import requests
# from urllib.request.Request
from bs4 import BeautifulSoup

# 4개 데이터 수집
url="https://finance.naver.com/marketindex/"
response = requests.get(url)
# requests.get(), requests.post()
# response.content
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify)

exchange_data = []
baseUrl = " https://finance.naver.com"
exchangeList = soup.select("#exchangeList > li")

for item in exchangeList:
    data = {
        "title" : item.select_one(".h_lst").text,
        "exchange" : item.select_one(".value").text,
        "updown" : item.select_one(".head_info.point_dn > .blind").text,
        "link" : baseUrl + item.select_one("a").get("href")
    }
    exchange_data.append(data)
df = pd.DataFrame(exchange_data)
df.to_excel("Web_data/resource_code/naverfinance.xlsx", encoding="utf-8")