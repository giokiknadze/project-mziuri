# giorgi kiknadze
from bs4 import BeautifulSoup
import requests
import csv

# listi romelic sheicavs csv filies xazebis saxelebs
column_names = ['Entry Number', 'Name', 'Year', 'Game Price', 'Platform', 'Total Votes']

# xsnis main.csv fails to ar arsebobs qmnis
with open('main.csv', 'a', encoding='utf-8', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(column_names)

# qmnis headers romelic mibadzavs web broswings
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }

# gzavnis mititebul saitze motxovnas rom html content amoiros am yvelafristvis beautifulsoups iyenebs.
    site = requests.get('https://steam250.com/top250', headers=headers).text
    soup = BeautifulSoup(site, 'html.parser')
    games = soup.find_all('div', class_="appline")
    c = 1

# poulobs yvela html elements romelic aris class applineshi romelic saitze individualur tamashebs asaxavs.
# aseve yvela tamasidan amoirebs relevantur informacias rogoricaa name, date, price, content tags, platform information.
    for game in games:
        name = game.find('span', class_="title").text.split('. ')[1:]
        name = "{}".format(*name)
        game_date = game.find('span', class_="date").text if game.find('span', class_="date") else ""
        game_price = game.find('span', class_="price").text if game.find('span', class_="price") else "?????"
        game_content = game.find('a', class_="g2 tag").text if game.find('a', class_="g2 tag") else "N/A"
        game_platform = game.find('span', class_="platform")
        mac = game.find('a', class_="mac")
        win = game.find('a', class_="win")
        deck = game.find('a', class_="deck")


