#THIS DOES NOT WORK ANYMORE!!! api got changed completely and there's no way I'm rewriting this. its pretty crappy anyways
#holy fuck i need to add docstrings this looks like shit

import os
from dotenv import load_dotenv
from email.errors import MalformedHeaderDefect
import requests, time, os
from gtts import gTTS

start_time = time.time()
load_dotenv()
LUNAR_CRUSH_API = os.getenv('LUNAR_CRUSH')

main_response = requests.get(f'https://api.lunarcrush.com/v2?data=assets&key={LUNAR_CRUSH_API}symbol=BTC&interval=day&time_series_indicators=open,high,low,close&data_points=50')
main_hourly_response = requests.get(f'https://api.lunarcrush.com/v2?data=assets&key={LUNAR_CRUSH_API}symbol=BTC&interval=hour&time_series_indicators=open,high,low,close&data_points=50')
current_btc_price = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/sell")

data = current_btc_price.json()
final_score = 0

class response:

    daily = main_response.json()
    hour = main_hourly_response.json()
    price = int(float(data["data"]["amount"]))

class daily:

    High = response.daily['data'][0]['high']
    Low = response.daily['data'][0]['low']
    Open = response.daily['data'][0]['open']
    Close = response.daily['data'][0]['close']

class pivots:

    pivot_point = int((daily.High+daily.Low+daily.Close)/3)
    resistance_1 = int((pivot_point*2)-daily.Low)
    resistance_2 = int(pivot_point+(daily.High-daily.Low))
    support_1 = int((pivot_point*2)-daily.High)
    support_2 = int(pivot_point-(daily.High-daily.Low))

p = pivots()

class indicators:

    ma_list = []
    min_max_list = []

    #Structure of "ma" function: print(indicate.ma('open', 'hour', 13))
    #Structure of "bollibands" function: print(bollibands('a'))
    #Structure of "hml_average" function: print(hml_average('a'))
    #Structure of "min_max" function print(print(indicate.min_max(9, 'day', 'min', 'low')))

    def ma(self, price_type: str, day_or_hour: str, period: str):
        ma_data = requests.get(f"https://api.lunarcrush.com/v2?data=assets&key={LUNAR_CRUSH_API}symbol=BTC&interval={day_or_hour}&time_series_indicators=open,high,low,close&data_points={period}")
        ma_data_json = ma_data.json()
        for i in range(0,period+1):
            if i >= period:
                indicate.ma_list.append(response.price)
                moving_avg = int(sum(indicate.ma_list)/len(indicate.ma_list))
                return int(moving_avg)
               
            else:
                indicate.ma_list.append(ma_data_json['data'][0]['timeSeries'][i][price_type])

    def bollibands(self, bolli_choice: str):
        upper = int((indicate.ma(response.hour, 'open', 20)-(daily.Open-response.price)))
        lower = int((indicate.ma(response.hour, 'open', 20)+(daily.Open-response.price)))
        basis = int((indicate.ma(response.hour, 'open', 20)))
        if bolli_choice == 'a':
            return upper
        elif bolli_choice == 'b':
            return lower
        elif bolli_choice == 'c':
            return basis
        elif bolli_choice == 'd':
            return upper, basis, lower

    def min_max(self, period, day_or_hour: str, min_or_max: str, price_type: str):
        min_max_data = requests.get(f"https://api.lunarcrush.com/v2?data=assets&key={LUNAR_CRUSH_API}symbol=BTC&interval={day_or_hour}&time_series_indicators=open,high,low,close&data_points={period}")
        min_max_json = min_max_data.json()
        for i in range(0,period+1):
            if i >= period:
                if min_or_max == 'min':
                    return int(min(indicate.min_max_list))
                else:
                    return int(max(indicate.min_max_list))               
               
            else:
                indicate.min_max_list.append(min_max_json['data'][0]['timeSeries'][i][price_type])

    def adr(self, adr_choice: str, day_or_hour: str):
        daily_top = int(indicate.min_max(9, day_or_hour, 'max', 'high'))
        daily_low = int(indicate.min_max(9, day_or_hour, 'min', 'low'))
        ma_hml = int(indicate.ma('close', day_or_hour, 26))
        super_avg = (daily_top+daily_low)/2
        if adr_choice == 'a':
            return daily_top
        elif adr_choice == 'b':
            return daily_low
        elif adr_choice == 'c':
            return ma_hml
        elif adr_choice == 'd':
            return super_avg
        else:
            return daily_top, daily_low, ma_hml, super_avg
                
    def ichimoku(self, day_or_hour: str):
        conversion_line = (indicate.min_max(9, day_or_hour, 'max', 'high')+indicate.min_max(9, day_or_hour, 'min', 'low'))/2
        base_line = (indicate.min_max(26, day_or_hour, 'max', 'high')+indicate.min_max(26, day_or_hour, 'min', 'low'))/2
        leading_span_a = (conversion_line+base_line)/2
        leading_span_b = (indicate.min_max(52, day_or_hour, 'max', 'high')+indicate.min_max(52, day_or_hour, 'min', 'low'))/2
        return conversion_line, base_line, leading_span_a, leading_span_b

indicate = indicators() 
ma_length_one = 0

#1 is hourly, 2 is daily
#The maximum of final_score is 8
for i in range(1,3):
    if i == 1:
        day_or_hour = 'hour'
    else:
        day_or_hour = 'day' 
    for x in range(1,5): 
        print(ma_length_one)
        if x == 1:
            ma_length_one = 13
        elif x == 2: 
            ma_length_one = 26
        elif x == 3:
            ma_length_one = 100
        elif x ==4: 
            ma_length_one = 200
            print("BOOP")
        if indicate.ma('close', day_or_hour, ma_length_one) >= response.price:
            pass
        else:
            final_score += 1

print(final_score)

print("Process finished --- %s seconds ---" % (time.time() - start_time))



   






