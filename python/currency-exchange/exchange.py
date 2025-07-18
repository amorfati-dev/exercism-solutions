"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """
    Calculate the value of the exchanged currency.
    """
    return budget / exchange_rate

    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """


def get_change(budget, exchanging_value):
    """
    Calculate the amount of money left after the exchange.
    """
    return budget - exchanging_value

    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """


def get_value_of_bills(number_of_bills, denomination):
    """
    Calculate the total value of the bills.
    """
    return number_of_bills * denomination

    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """




def get_number_of_bills(amount, denomination):
    """
    Calculate the number of bills that can be obtained from the amount.
    """
    return amount // denomination

    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """


def get_leftover_of_bills(value, denomination):
    """
    Calculate the amount that is leftover after exchanging into bills.
    """
    return value % denomination

    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """




def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate the maximum value that can be exchanged into bills.
    """
    # Calculate the actual exchange rate with spread
    actual_rate = exchange_rate * (1 + spread / 100)
    
    # Calculate the value in the new currency
    value = budget / actual_rate
    
    # Calculate how many bills we can get
    bills = get_number_of_bills(value, denomination)
    
    # Return the total value of the bills
    return get_value_of_bills(bills, denomination)

    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """