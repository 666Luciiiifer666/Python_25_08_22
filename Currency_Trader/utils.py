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
        local_data = json.load(file)
        local_exchange_rate = local_data.get('course')
        uah = local_data.get('UAH')
        usd = local_data.get('USD')
        local_delta = local_data.get('delta')
    return local_exchange_rate, uah, usd, local_delta, local_data


data_of_current_recording = current_data_state()
exchange_rate = data_of_current_recording[0]
uah_available = data_of_current_recording[1]
usd_available = data_of_current_recording[2]
delta = data_of_current_recording[3]
data = data_of_current_recording[4]


def current_data_recording(money_available):
    with open(current_data_location, 'w') as file:
        json.dump(money_available, file)


def rate(local_exchange_rate):
    print(local_exchange_rate)


def available(local_usd_available, local_uah_available):
    print('USD', local_usd_available, 'UAH', local_uah_available)


def buy_xxx(amount, local_uah_available, local_usd_available, local_exchange_rate):
    amount_in_uah = amount * local_exchange_rate
    if local_uah_available >= amount_in_uah:
        local_uah_available -= rounding_after_decimal_point(amount_in_uah)
        local_usd_available += rounding_after_decimal_point(amount)
        uah_usd_available_update = {"USD": local_usd_available,
                                    "UAH": local_uah_available}
        data.update(uah_usd_available_update)
        current_data_recording(data)
    else:
        print('REQUIRED BALANCE UAH ', amount_in_uah, ' AVAILABLE ', local_uah_available)


def sell_xxx(amount, local_usd_available, local_uah_available, local_exchange_rate):
    amount_in_uah = amount * local_exchange_rate
    if local_usd_available >= amount:
        local_uah_available += rounding_after_decimal_point(amount_in_uah)
        local_usd_available -= rounding_after_decimal_point(amount)
        uah_usd_available_update = {"USD": local_usd_available,
                                    "UAH": local_uah_available}
        data.update(uah_usd_available_update)
        current_data_recording(data)
    else:
        print('REQUIRED BALANCE USD ', amount, ' AVAILABLE ', local_usd_available)


def buy_all(local_uah_available, local_exchange_rate, local_usd_available):
    value_usd = local_uah_available / local_exchange_rate
    uah_usd_available_update = {"USD": local_usd_available + rounding_after_decimal_point(value_usd),
                                "UAH": local_uah_available - rounding_after_decimal_point(local_exchange_rate * value_usd)}
    data.update(uah_usd_available_update)
    current_data_recording(data)


def sell_all(local_usd_available, local_uah_available, local_exchange_rate):
    value_uah = local_usd_available * local_exchange_rate
    uah_usd_available_update = {"USD": 0,
                                "UAH": local_uah_available + rounding_after_decimal_point(value_uah)}
    data.update(uah_usd_available_update)
    current_data_recording(data)


def next_step(local_exchange_rate, local_delta):
    new_exchange_rate = rounding_after_decimal_point(random.triangular(local_exchange_rate - local_delta,
                                                                       local_exchange_rate + local_delta))
    current_data_update = {"course": new_exchange_rate}
    data.update(current_data_update)
    current_data_recording(data)


def restart():
    with open(configuration_file_path) as file_config:
        data_update = json.load(file_config)
    current_data_recording(data_update)
