import requests
from datetime import datetime
import pytz

# === 設定區 ===
CITIES = {
    "北部": "Taipei",
    "中部-老大": "Taichung",
    "中部-大哥": "Taichung",
    "南部": "Kaohsiung"
}

TEMPLATES = {
    "北部": "邦哥早安~\n{提醒}",
    "中部-老大": "老大早~\n{提醒}",
    "中部-大哥": "大哥早~\n{提醒}",
    "南部": "哥早安~\n{提醒}"
}

def fetch_fake_weather(city):
    # 此處為示意用，可替換為 OpenWeather API
    if city == "Taipei":
        return "午後局部地區有雷陣雨，出門備傘比較安心。"
    elif city == "Taichung":
        return "中午前後可能會有短暫陣雨，外出記得多留心天氣變化。"
    elif city == "Kaohsiung":
        return "中午附近可能轉雷陣雨，出門建議帶傘，避免臨時狼狽。"
    return "今天天氣普通，記得照顧好自己。"

def build_messages():
    results = []
    for region, city in CITIES.items():
        reminder = fetch_fake_weather(city)
        text = TEMPLATES[region].format(提醒=reminder)
        results.append(text)
    return "\n\n".join(results)

def main():
    tz = pytz.timezone('Asia/Taipei')
    now = datetime.now(tz)
    print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}]")
    print(build_messages())

if __name__ == "__main__":
    main()
