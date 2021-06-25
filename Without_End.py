# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.


# without_end('Hello') → 'ell'
# without_end('java') → 'av'
# without_end('coding') → 'odin'

name = input("Enter Your Name : ")
print(name[2:] + name[0:2])