# Example file for Advanced Python: Language Features by Joe Marini
# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

# define some starting values
b = bytes([0x41, 0x42, 0x43, 0x44])
print(b)

s = "This is a string"
print(s)

# TODO: Try combining them.

# TODO: Bytes and strings need to be properly encoded and decoded
# before you can work on them together
# python has built-in methods for encoding and decoding strings
# into a sequence of bytes and vice versa

# example using decode() method, then concatenating
# s2 = b.decode('utf-8')
# print(s + s2)

# example using encode() method, then concatenating
# b2 = s.encode('utf-8')
# print(b + b2)

# TODO: encode the string as UTF-32
b3 = s.encode('utf-32')
print(b3)

# remember that strings and bytes are not the same thing!
# be careful when mixing them, and use the proper methods
