import requests
from csv import writer

if __name__ == '__main__':
    page_url = 'https://www.coronatracker.com/analytics/'
    s = requests.Session()
    s.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}

    res = s.get(page_url)
    res.raise_for_status()

    json_url = 'https://api.coronatracker.com/v3/stats/worldometer/topCountry'
    res = s.get(json_url)
    res.raise_for_status()
    data = res.json()

with open('covid_data.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['country', 'totalConfirmed', 'totalDeaths', 'totalRecovered', 'dailyConfirmed', 'dailyDeaths', 'activeCases', 'totalCritical', 'lastUpdated']
    csv_writer.writerow(headers) 
    for i in data:
        csv_writer.writerow([ i['country'], i['totalConfirmed'], i['totalDeaths'], i['totalRecovered'], i['dailyConfirmed'], i['dailyDeaths'], i['activeCases'], i['totalCritical'], i['lastUpdated']])


