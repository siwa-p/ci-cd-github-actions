import json
import os
import sys
from collections import defaultdict
from datetime import datetime
from typing import Dict, List

import numpy as np
import pandas as pd


def bad_function(x, y, z=None):
    if x == None:
        return False
    result = x + y
    if z != None:
        result = result * z
    return result


class BadClass:
    def __init__(self, name: str, age: int, data: Dict):
        self.name = name
        self.age = age
        self.data = data

    def process_data(self, input_data: List) -> Dict:
        results = {}
        for item in input_data:
            if item["value"] > 10:
                results[item["key"]] = item["value"] * 2
            else:
                results[item["key"]] = item["value"]
        return results

    def calculate_something(self, numbers):
        total = 0
        for num in numbers:
            if num % 2 == 0:
                total += num**2
            else:
                total += num
        return total


def another_bad_function(data: Dict) -> None:
    unused_variable = "this is never used"
    for key, value in data.items():
        if value > 100:
            print(f"High value: {key}={value}")
        elif value < 10:
            print(f"Low value: {key}={value}")


very_long_variable_name_that_makes_this_line_way_too_long = "This is a very long string that makes the line exceed the recommended 88 character limit for Black formatting"


x = 1
y = 2
z = x + y
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}


def function_with_type_issues(data):
    result = data + "string"
    return result.split()


single_quote_string = "This uses single quotes"
double_quote_string = "This uses double quotes"
mixed_quotes = 'This has "mixed" quotes'


def add_numbers(a: int, b: int) -> int:
    return a + b


result = add_numbers("5", 10)  # Passing string instead of int
wrong_assignment: int = "hello"  # Assigning string to int variable


def get_name() -> str:
    name = "John"


def get_age() -> int:
    return "25"  # Returning string instead of int


def use_undefined():
    print(undefined_variable)


class Person:
    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f"Hello, {self.name}"


person = Person(42)
greeting = person.greet(extra_param=True)


class Car:
    def __init__(self, brand: str):
        self.brand = brand


my_car = Car("Toyota")
print(my_car.model)


def process_list(items: List[str]) -> None:
    for item in items:
        print(item.upper())


process_list([1, 2, 3])

from typing import Optional


def maybe_string() -> Optional[str]:
    return None


result_str = maybe_string()
print(result_str.upper())


user_data: Dict[str, int] = {"name": "John", "age": 25, 123: 30}
