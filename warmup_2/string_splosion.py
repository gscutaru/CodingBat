"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""

def string_splosion(str):
    new_string = ""
    for i in range(len(str)):
        new_string += str [:i + 1]
    return new_string


print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
