from decimal import Decimal, ROUND_FLOOR



number = 12


def rounding_after_decimal_point(number):
    number = Decimal(str(number))
    number = number.quantize(Decimal("1.00"), ROUND_FLOOR)
    return number


number = rounding_after_decimal_point(number)

print(number)
