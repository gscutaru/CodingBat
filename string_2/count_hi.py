"""
Return the number of times that the string "hi"
appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""

def count_hi(str):
    count = 0
    for letter in range(len(str) - 1):
        if str[letter] + str[letter + 1] == "hi":
            count += 1
    return count


print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))
