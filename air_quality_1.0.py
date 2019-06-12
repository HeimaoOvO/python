import requests
from bs4 import BeautifulSoup
import csv
import lxml


def get_cities_quality(city_py):
    """
        获取城市的空气质量AQI
    """
    url = "http://pm25.in/" + city_py
    xdd = requests.get(url, timeout=60)
    soup = BeautifulSoup(xdd.text, "lxml")
    pc_list = soup.find_all("div", {"class": "span1"})

    cities_aqi = []
    for i in range(8):
        pc_content = pc_list[i]
        value = pc_content.find("div", {"class": "value"}).text.strip()
        cities_aqi.append(value)
    return cities_aqi


def get_cities():
    """
        获取所有城市
    """
    url = "http://pm25.in/"
    cities_list = []
    xdd = requests.get(url, timeout=60)
    soup = BeautifulSoup(xdd.text, "lxml")

    cities_div = soup.find_all("div", {"class": "bottom"})[1]
    cities_link_list = cities_div.find_all("a")
    for cities_link in cities_link_list:
        city_name = cities_link.text
        city_py = cities_link['href'][1:]
        cities_list.append((city_name, city_py))
    return cities_list


def main():
    cities_all = get_cities()
    header = ['City', 'AQI', 'PM2.5/1h', 'PM10/h', 'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h']
    with open("cities_aqi.csv", "w", encoding="utf-8", newline="")as f:
        writing = csv.writer(f)
        writing.writerow(header)
        for i, city in enumerate(cities_all):
            if(i + 1) % 5 == 0:
                print("共有{}条记录，目前已处理{}条城市记录。".format(len(cities_all), i+1))
            city_name = city[0]
            city_py = city[1]
            city_aqi = get_cities_quality(city_py)
            row = [city_name] + city_aqi
            writing.writerow(row)

if __name__ == "__main__":
    main()