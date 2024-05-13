import typing
import re

def generator_numbers(text: str)->typing.Callable[[],float]:

    float_list=map(float, re.findall(r"\s[\+\-0-9]+\.[0-9]*[\s]|[\s][\+\-0-9]*\.[0-9]+[\s]",text))

    def next_float()->float:
        nonlocal float_list
        try:
            while True:
                yield float_list.__next__()
        except StopIteration:
            pass
                           
    return  next_float                    

def sum_profit(text: str, func: typing.Callable[[str],typing.Callable[[],float]])->float:
    return sum(func(text)())

text = "Загальний дохід працівника складається з декількох частин:\
      1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# #Загальний дохід: 1351.46

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

