from Corredor1 import Corredor1, manejar1
from Corredor2 import Corredor2, manejar2

class Imprimir (Corredor2, Corredor1):
  pass
print (manejar1.conduce_auto())
print (manejar2.conduce_auto())
