# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).


# combo_string('Hello', 'hi') → 'hiHellohi'
# combo_string('hi', 'Hello') → 'hiHellohi'
# combo_string('aaa', 'b') → 'baaab'

name_a = input("Enter Your Name : ")
name_b = input("Enter Your Name : ")

if name_a > name_b:
    print (name_a + name_b + name_a)
if name_a < name_b:
    print (name_b + name_a + name_b)