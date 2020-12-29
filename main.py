import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://flightplanning.navcanada.ca/cgi-bin/Fore-obs/metar.cgi')
soup = BeautifulSoup(page.content, 'html.parser')
metarAndTaf = soup.find(style="text-indent:-1.5em;margin-left:1.5em")
# print(week)

items = metarAndTaf.find_all(class_='tombstone-container')
# print(items[1])

print(items[1].find(class_='period-name').get_text())
print(items[1].find(class_='short-desc').get_text())
print(items[1].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]

print(period_names)
print(short_descriptions)

weather_stuff = pd.DataFrame(
    {
        'period': period_names,
        'short_descriptions': short_descriptions,
    })

print(weather_stuff)

