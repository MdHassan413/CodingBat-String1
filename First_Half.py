# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'

even = input("Enter Your 'Even Length' : ")
print(even[:len(even)/2])