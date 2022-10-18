import json
import random

current_data_location = 'Currency_Trader\\sys_data.json'
configuration_file_path = 'Currency_Trader\\config.json'


def Current_data_state():
    with open(current_data_location) as file:
        data = json.load(file)
        exchange_rate = data.get('course')
        uah = data.get('UAH')
        usd = data.get('USD')
        delta = data.get('delta')
    return exchange_rate, uah, usd, delta, data


exchange_rate = Current_data_state()[0]
uah_available = Current_data_state()[1]
usd_available = Current_data_state()[2]
delta = Current_data_state()[3]
data = Current_data_state()[4]


def current_data_recording(money_available):
    with open(current_data_location, 'w') as file:
        json.dump(money_available, file)


def rate():
    print(exchange_rate)


def available():
    print('USD', usd_available, 'UAH', uah_available)


def buy_xxx(amount):
    uah_available = Current_data_state()[1]
    usd_available = Current_data_state()[2]
    amount_in_uah = float(amount) * exchange_rate
    if uah_available >= amount_in_uah:
        uah_available -= amount_in_uah
        usd_available += float(amount)
        uah_usd_available_update = {"USD": usd_available,
                                    "UAH": uah_available}
        data.update(uah_usd_available_update)
        current_data_recording(data)
    else:
        print('REQUIRED BALANCE UAH ', amount_in_uah, ' AVAILABLE ', uah_available)


def sell_xxx(amount):
    uah_available = Current_data_state()[1]
    usd_available = Current_data_state()[2]
    amount_in_uah = float(amount) * exchange_rate
    if usd_available >= float(amount):
        uah_available += amount_in_uah
        usd_available -= float(amount)
        uah_usd_available_update = {"USD": usd_available,
                                    "UAH": uah_available}
        data.update(uah_usd_available_update)
        current_data_recording(data)
    else:
        print('REQUIRED BALANCE USD ', amount, ' AVAILABLE ', usd_available)


def buy_all():
    value_usd = int(uah_available / exchange_rate)
    uah_usd_available_update = {"USD": usd_available + value_usd,
                                "UAH": uah_available - exchange_rate * value_usd}
    data.update(uah_usd_available_update)
    current_data_recording(data)


def sell_all():
    value_uah = usd_available * exchange_rate
    uah_usd_available_update = {"USD": 0,
                                "UAH": uah_available + value_uah}
    data.update(uah_usd_available_update)
    current_data_recording(data)


def next_step():
    new_exchange_rate = round(random.triangular(exchange_rate - delta,
                                                exchange_rate + delta), 2)
    current_data_update = {"course": new_exchange_rate}
    data.update(current_data_update)
    current_data_recording(data)


def restart():
    with open(configuration_file_path) as file_config:
        data_update = json.load(file_config)
    current_data_recording(data_update)
