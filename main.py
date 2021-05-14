import requests
from bs4 import BeautifulSoup
import time

LTC_USD = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+ltc&sxsrf=ALeKk02n6uUozE5I64fIXRik0eLfpAaJjQ%3A1621021655036&source=hp&ei=1tOeYO_TPMyNwPAPo7uNyAk&iflsig=AINFCbYAAAAAYJ7h57L6-8aPD7Th4LQKspG8SdctumYv&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+ltc&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEEYQggI6BAgAEEM6AggAOgkIABBDEEYQggI6BAgAEAo6CAgAEBYQChAeOgYIABAWEB5QqBFY7mRgqm9oAHAAeACAAYgBiAGUD5IBBDUuMTOYAQCgAQGqAQdnd3Mtd2l6&sclient=gws-wiz&ved=0ahUKEwjvlq2f-MnwAhXMBhAIHaNdA5kQ4dUDCAc&uact=5'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}

def check_currency():
    full_page = requests.get(LTC_USD, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", { "class": "DFlfde", "class": "SwHCTb", "data-precision": "4" })
    print("1 LTC to USD is =", convert[0].text)
    time.sleep(60) #засыпаем на 60 сек
    check_currency()

check_currency()