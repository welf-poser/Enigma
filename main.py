from enigma.rotor import Rotor
from enigma.reflector import Reflector

r1 = Rotor(1, 1)
r2 = Rotor(1, 1)
r3 = Rotor(1, 1)

refl = Reflector('B')


swap1 = r1.swap('a')
swap2 = r2.swap(swap1)
swap3 = r3.swap(swap2)

refl1 = refl.swap(swap3)

rev_swap3 = r3.reverse_swap(refl1)
rev_swap2 = r2.reverse_swap(rev_swap3)
rev_swap1 = r1.reverse_swap(rev_swap2)


print(swap1)
print(swap2)
print(swap3)

print(refl1)

print(rev_swap3)
print(rev_swap2)
print(rev_swap1)