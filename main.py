import requests
import smtplib

password = "hvlrhpnpzoawbcoe"
my_email = "ilearntostudy@gmail.com"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
API_KEY = "c6ec301ae26e287016b8134bacb09041"

parameters = {
    "lat": 2.046934,
    "lon": 45.318161,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url = OWM_Endpoint, params = parameters)
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = "learnerpython169@gmail.com",
            msg = f"Subject:Rain Alert \n\n Today is raining day, bring your umbrella")
    print("Rain")
