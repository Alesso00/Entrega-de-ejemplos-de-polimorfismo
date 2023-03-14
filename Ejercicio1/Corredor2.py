from Conducir import Conducir, vehiculo_1, vehiculo_2
class Corredor2(Conducir): 
     
    

     def conduce_auto ():
      nombre = "Jose"
      return ("El corredor {} le gusta Concudir el vehiculo {} {} {}".format(nombre, vehiculo_2.marca, vehiculo_2.modelo, vehiculo_2.año))
     
manejar2 = Corredor2

#print (manejar.conduce_auto())