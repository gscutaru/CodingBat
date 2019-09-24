"""
Given two strings, return True if either of the strings appears at the very end
of the other string, ignoring upper/lower case differences (in other words,
the computation should not be "case sensitive").
Note: s.lower() returns the lowercase version of a string.
Hint:
In Python s1.endswith(s2) tests if string s1 ends with string s2
-- makes this much easier!

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
"""

def end_other(a, b):
    a_l = a.lower()
    b_l = b.lower()
    if a_l.endswith(b_l) or b_l.endswith(a_l):
        return True
    else:
        return False


print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
