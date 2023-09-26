from bs4 import BeautifulSoup
import requests
import json


def get_data():
    page = requests.get("https://www.forbes.ru/milliardery/487053-10-bogatejsih-ludej-mira-2023-rejting-forbes")
    soup = BeautifulSoup(page.text, "lxml")
    all_person = soup.find_all('figcaption', class_='EXdHT')
    for person in all_person:
        name = person.find('h2', class_='jYzxi').text
        file_name = name.replace('№', '').replace(' ', '_')

        data = {
            name: {}
        }

        for item in person.find('div', class_='CFaZ3').find('p').find('span').find_all('b'):
            data[name][item.text.strip()] = item.next_sibling.text.strip()

        with open(f'data/{file_name}.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)


get_data()
