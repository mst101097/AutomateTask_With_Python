import requests
api_key ='e1c19e5b340ccaf3c8cd5274f7322327'
#api.openweathermap.org/data/2.5/forecast?q={cityname}&appid={API key}
def wetherForcast(cityname,units='matric', api_key= api_key ):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={cityname}&appid={api_key}&units={units}"
    r = requests.get(url)
    content =r.json()
    with open('data.txt','a') as file:
        for dicty in content['list']:
            file.write(f"{dicty['dt_txt']},{dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")
wetherForcast(cityname='Washington')

