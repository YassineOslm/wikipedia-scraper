import requests
import json
import re
from bs4 import BeautifulSoup

def get_first_paragraph(wikipedia_url, session):
    response = session.get(wikipedia_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        if paragraph.find('b'):
            break
    text = paragraph.get_text()
    patterns = [
        r'\(.*?Écouter.*?\)',
        r'\[.*?\]',
        r'\/.*?\/',
        r'ⓘ',
        r'\(.*?ⓘ.*?\)',
        r'uitspraakⓘ ?',
        r'\([^)]*\)',
        r'\bÉcouter\b'
    ]
    for pattern in patterns:
        text = re.sub(pattern, '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def save(leaders_per_country):
    with open("leaders.json", "w", encoding="utf-8") as f:
        json.dump(leaders_per_country, f, ensure_ascii=False, indent=2)

def get_leaders():
    base = "https://country-leaders.onrender.com/"
    cookie = requests.get(base + "cookie").cookies

    try:
        countries = requests.get(base + "countries", cookies=cookie).json()
    except:
        cookie = requests.get(base + "cookie").cookies
        countries = requests.get(base + "countries", cookies=cookie).json()

    leaders_per_country = {}
    with requests.Session() as session:
        for country in countries:
            try:
                res = requests.get(base + "leaders", cookies=cookie, params={"country": country})
                if res.status_code != 200:
                    raise Exception()
            except:
                cookie = requests.get(base + "cookie").cookies
                res = requests.get(base + "leaders", cookies=cookie, params={"country": country})
            leaders = res.json()
            for leader in leaders:
                leader["first_paragraph"] = get_first_paragraph(leader["wikipedia_url"], session)
            leaders_per_country[country] = leaders
    return leaders_per_country

if __name__ == "__main__":
    leaders_per_country = get_leaders()
    save(leaders_per_country)
