import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]


def main():
    aqi_data = pd.read_csv("cities_aqi.csv")
    print("数据预览：")
    print(aqi_data.head())

    # 数据清洗
    clean_aqi_data = aqi_data[aqi_data["AQI"] > 0]
    top30_cities = (clean_aqi_data.sort_values(by=["AQI"]).head(30))
    worst30_cities = (clean_aqi_data.sort_values(by=["AQI"]).tail(30))
    top30_cities.plot(kind="bar", x="City", y="AQI", title="空气质量最好的30个城市", figsize=(20, 20), edgecolor="pink")
    worst30_cities.plot(kind="bar", x="City", y="AQI", title="空气质量最差的30个城市", figsize=(20, 20))
    plt.savefig("top30_cities.png")
    plt.savefig("worst30_cities.png")
    plt.show()


if __name__ == "__main__":
    main()
