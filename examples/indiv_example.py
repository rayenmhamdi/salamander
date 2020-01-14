
from individual import Individual


BINARIES_ENCODING = 'binaries'
DIGITS_ENCODING = 'digits'
BOOLEANS_ENCODING = 'booleans'
LETTERS_ENCODING = 'letters'
CUSTOM_ENCODING = 'custom'

a = Individual()
a.create_individual(5,BINARIES_ENCODING)

b = Individual()
b.create_individual(5, BOOLEANS_ENCODING)

c = Individual()
c.create_individual(5, DIGITS_ENCODING)

d = Individual()
d.create_individual(5,LETTERS_ENCODING)

e = Individual()
e.create_individual(5, CUSTOM_ENCODING, ['Forward', 'Backword', 'Left', 'Right'])

print(a)
print(b)
print(c)
print(d)
print(e)

