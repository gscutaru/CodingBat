"""
Return True if the string "cat" and "dog" appear t
he same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""

def cat_dog(str):
    count_cat = 0
    count_dog = 0
    for i in range(len(str) - 1):
        if str[i:i + 3] == "cat":
            count_cat += 1
        elif str[i:i + 3] == "dog":
            count_dog += 1
    if count_cat == count_dog:
        return True
    else:
        return False


print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))
