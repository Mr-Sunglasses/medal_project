import time

from bs4 import BeautifulSoup
import requests

print("Enter the Country Name which you want to search the Meadals of")
country_name_search = input('>: ')
print(f'Searching out {country_name_search}')

def find_medals():
    html_text = requests.get('https://www.mykhel.com/olympics-medal-table/').text

    soup = BeautifulSoup(html_text,'lxml')

    countries = soup.find_all('tr',class_='med')
    for country in countries:

        no = country.find('td').text
        county_name = country.find('td',class_="country-title country-expand").span.text.replace('arrow_drop_down','').replace(' ','')
        gold_sudo = country.find_all('td')[2]
        gold_real = ''
        for i in gold_sudo:
            gold_real = str(i)

        silver_sudo  = country.find_all('td')[3]
        silver_real = ''
        for j in silver_sudo:
            silver_real = str(j)

        bronze_sudo = country.find_all('td')[4]
        bronze_real = ''
        for k in bronze_sudo:
            bronze_real = str(k)

        total = int(gold_real)+int(silver_real)+int(bronze_real)

        if country_name_search.upper() == county_name.upper():
            print(f'''
            Position : {no.strip()}
            Country : {county_name.strip()}
            Gold Medals : {gold_real.strip()}
            Silver Meadals : {silver_real.strip()}
            Bronze Medals : {bronze_real.strip()}
            Total Medals : {total}
            ''')

            print("------------------------------------------------")


if __name__ == '__main__':
    while True:
        find_medals()
        time_wait = 10
        print(f'Waiting {time_wait} Minutes to update the result.......')
        time.sleep(time_wait*600)













