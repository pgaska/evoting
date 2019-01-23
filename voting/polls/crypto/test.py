import argparse
import sys

from ecurve.elliptic import EllipticCurve
from ecurve.elgamal import Elgamal
from ecurve.point import Point

class Curve(object):
   def __init__(self):
       self.p=8884933102832021670310856601112383279507496491807071433260928721853918699951
       self.n=8884933102832021670310856601112383279454437918059397120004264665392731659049
       self.a4=2481513316835306518496091950488867366805208929993787063131352719741796616329
       self.a6=4387305958586347890529260320831286139799795892409507048422786783411496715073
       self.r4=5473953786136330929505372885864126123958065998198197694258492204115618878079
       self.r6=5831273952509092555776116225688691072512584265972424782073602066621365105518
       self.gx=7638166354848741333090176068286311479365713946232310129943505521094105356372
       self.gy=762687367051975977761089912701686274060655281117983501949286086861823169994
       self.r=8094458595770206542003150089514239385761983350496862878239630488323200271273


curve = Curve()
print('zadzialalo')

elgamal = Elgamal(curve)

#tworzenie kluczy
(publickey, privatekey) = elgamal.keygen()

with open('wazna_wiad', "rb") as file:
      with open('wazny_szyfr', 'w') as cipher:
         buffer_size = 35
         byte = file.read(buffer_size)
         while byte:
            m = int.from_bytes(byte, sys.byteorder)
            (c1, c2) = elgamal.encrypt(publickey, m)
            cipher.write(str(c1)+ "\n")
            cipher.write(str(c2.x)+ "\n")
            cipher.write(str(c2.y)+ "\n")
            byte = file.read(buffer_size)
         cipher.close()
      file.close()

with open('wazny_szyfr', "r") as cipher:
      with open('wazny_odczyt', 'wb') as file:
         lines = cipher.readlines()
         ii = 0
         while ii < len(lines):
            c2 = Point(curve, int(lines[ii + 1]), int(lines[ii + 2]))
            m = elgamal.decrypt(privatekey, int(lines[ii]), c2)
            file.write(m.to_bytes(m.bit_length()//8 + 1, sys.byteorder))
            ii += 3
         file.close()
      cipher.close()
