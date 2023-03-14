from Conducir import Conducir, vehiculo_1, vehiculo_2
class Corredor1(Conducir): 
     
    

     def conduce_auto ():
      nombre = "Alexander"
      return ("El corredor {} le gusta Concudir el vehiculo {} {} {}".format(nombre, vehiculo_1.marca, vehiculo_1.modelo, vehiculo_1.año))
     
manejar1 = Corredor1

#print (manejar.conduce_auto())