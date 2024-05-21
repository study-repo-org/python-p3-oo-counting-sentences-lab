#!/usr/bin/env python3

import re

class MyString():

    def __init__(self, value = ''):
        self._value = value
        
    def get_value(self):
        return self._value

    def set_value(self, value):
        if (type(value) == str):
            print(f"Setting value to {value}")
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        if self.value == '':
            return 0
            
        return len(re.split(r'[!\?\.](?= )', self.value))

# re.split(r'[\?!\.](?= )', string)
simple_string = MyString("one. two. three?")
empty_string = MyString()
complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")

print(simple_string.count_sentences())
print(complex_string.count_sentences())
print(empty_string.count_sentences())