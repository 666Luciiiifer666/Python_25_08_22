from decimal import Decimal, ROUND_FLOOR
import json
import random

current_data_location = 'sys_data.json'
configuration_file_path = 'config.json'


def rounding_after_decimal_point(number):
    number = Decimal(str(number))
    number = number.quantize(Decimal("1.00"), ROUND_FLOOR)
    return float(number)


def current_data_state():
    with open(current_data_location) as file:
        data = json.load(file)
        exchange_rate = data.get('course')
        uah = data.get('UAH')
        usd = data.get('USD')
        delta = data.get('delta')
    return exchange_rate, uah, usd, delta, data


data_of_current_recording = current_data_state()
exchange_rate = data_of_current_recording[0]
uah_available = data_of_current_recording[1]
usd_available = data_of_current_recording[2]
delta = data_of_current_recording[3]
data = data_of_current_recording[4]


def current_data_recording(money_available):
    with open(current_data_location, 'w') as file:
        json.dump(money_available, file)


def rate(exchange_rate):
    print(exchange_rate)


def available(usd_available, uah_available):
    print('USD', usd_available, 'UAH', uah_available)


def buy_xxx(amount, uah_available, usd_available, exchange_rate):
    amount_in_uah = amount * exchange_rate
    if uah_available >= amount_in_uah:
        uah_available -= rounding_after_decimal_point(amount_in_uah)
        usd_available += rounding_after_decimal_point(amount)
        uah_usd_available_update = {"USD": usd_available,
                                    "UAH": uah_available}
        data.update(uah_usd_available_update)
        current_data_recording(data)
    else:
        print('REQUIRED BALANCE UAH ', amount_in_uah, ' AVAILABLE ', uah_available)


def sell_xxx(amount, usd_available, uah_available, exchange_rate):
    amount_in_uah = amount * exchange_rate
    if usd_available >= amount:
        uah_available += rounding_after_decimal_point(amount_in_uah)
        usd_available -= rounding_after_decimal_point(amount)
        uah_usd_available_update = {"USD": usd_available,
                                    "UAH": uah_available}
        data.update(uah_usd_available_update)
        current_data_recording(data)
    else:
        print('REQUIRED BALANCE USD ', amount, ' AVAILABLE ', usd_available)


def buy_all(usd_available, uah_available, exchange_rate):
    value_usd = uah_available / exchange_rate
    uah_usd_available_update = {"USD": usd_available + rounding_after_decimal_point(value_usd),
                                "UAH": uah_available - rounding_after_decimal_point(exchange_rate * value_usd)}
    data.update(uah_usd_available_update)
    current_data_recording(data)


def sell_all(usd_available, uah_available, exchange_rate):
    value_uah = usd_available * exchange_rate
    uah_usd_available_update = {"USD": 0,
                                "UAH": uah_available + rounding_after_decimal_point(value_uah)}
    data.update(uah_usd_available_update)
    current_data_recording(data)


def next_step(exchange_rate, delta):
    new_exchange_rate = rounding_after_decimal_point(random.triangular(exchange_rate - delta,
                                                exchange_rate + delta))
    current_data_update = {"course": new_exchange_rate}
    data.update(current_data_update)
    current_data_recording(data)


def restart():
    with open(configuration_file_path) as file_config:
        data_update = json.load(file_config)
    current_data_recording(data_update)
