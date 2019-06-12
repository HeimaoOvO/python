import pandas as pd
import matplotlib.pyplot as plt
import csv
plt.rcParams["font.sans-serif"] = ["SimHei"]


def main():
    aqi_data = pd.read_csv("cities_aqi.csv")
    print("数据预览：")
    print(aqi_data.head())

    clean_aqi_data = aqi_data[aqi_data["AQI"] > 0]
    aqi_all = clean_aqi_data["AQI"]
    f = open('aqi_city03.txt', 'a')
    f.write('{}\n'.format(aqi_all.values))
    f.close()

    plt.scatter(aqi_all.index, aqi_all.values)
    plt.ylabel("AQI")
    plt.title("AQI散点图分布表")
    plt.grid(b=True, which='major', axis='y', c="pink")
    plt.savefig("all_cities.PNG")
    plt.show()


if __name__ == "__main__":
    main()
