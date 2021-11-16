#El encargado de Jurassic World nos solicita que desarrollemos un algoritmo que nos permita
#resolver los siguientes requerimientos:
#1. almacenar los datos de los distintos dinosaurios que hay en la isla, de cada uno se
#conoce su nombre, código de cinco dígitos y zona de ubicación (un dígito y un carácter
#por ejemplo 7A), existen varios dinosaurios con el mismo nombre pero sus códigos son
#distintos, los códigos no pueden ser repetidos (tenga cuidado);
#2. se deben almacenar los datos en dos arboles uno ordenado por nombre y otro por
#código;
#3. realizar un barrido en orden del árbol ordenado por nombre;
#4. mostrar toda la información del dinosaurio 792;
#5. mostrar toda la información de todos los T-Rex que hay en la isla;
#6. modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal
#cargado, su nombre correcto es Stygimoloch;
#7. mostrar la ubicación de todos los Raptores que hay en la isla;
#8. contar cuantos Diplodocus hay en el parque;
#9. debe cargar al menos 15 elementos.
from arbol_binario import Arbol
from random import choice, randint


arbol_por_nombre = Arbol()
arbol_por_codigo = Arbol()


Dinosaurios = {"nombre": "TRICERATOPS" ,"codigo":"243678" , "zona de ubicacion":(randint (1,15),choice("ABCDEFGHIJKLMOPQRST"))}
arbol_por_nombre = arbol_por_nombre.insertar_nodo(Dinosaurios["nombre"],Dinosaurios)
arbol_por_codigo = arbol_por_codigo.insertar_nodo(Dinosaurios["codigo"],Dinosaurios)
Dinosaurios = {"nombre": "T-REX" ,"codigo":"87632", "zona de ubicacion":(randint (1,15),choice("ABCDEFGHIJKLMOPQRST"))}
arbol_por_nombre = arbol_por_nombre.insertar_nodo(Dinosaurios["nombre"],Dinosaurios)
arbol_por_codigo = arbol_por_codigo.insertar_nodo(Dinosaurios["codigo"],Dinosaurios)
Dinosaurios = {"nombre": "RAPTOR" ,"codigo":"06593", "zona de ubicacion":(randint (1,15),choice("ABCDEFGHIJKLMOPQRST"))}
arbol_por_nombre = arbol_por_nombre.insertar_nodo(Dinosaurios["nombre"],Dinosaurios)
arbol_por_codigo = arbol_por_codigo.insertar_nodo(Dinosaurios["codigo"],Dinosaurios)
Dinosaurios = {"nombre": "BRONTOSAURIO" ,"codigo":"17532", "zona de ubicacion":(randint (1,15),choice("ABCDEFGHIJKLMOPQRST"))}
arbol_por_nombre = arbol_por_nombre.insertar_nodo(Dinosaurios["nombre"],Dinosaurios)
arbol_por_codigo = arbol_por_codigo.insertar_nodo(Dinosaurios["codigo"],Dinosaurios)
Dinosaurios = {"nombre": "STEGOSAURIO" ,"codigo":"75532", "zona de ubicacion":(randint (1,15),choice("ABCDEFGHIJKLMOPQRST"))}
arbol_por_nombre = arbol_por_nombre.insertar_nodo(Dinosaurios["nombre"],Dinosaurios)
arbol_por_codigo = arbol_por_codigo.insertar_nodo(Dinosaurios["codigo"],Dinosaurios)
Dinosaurios = {"nombre": "ANKILOSAURIO" ,"codigo":"63401", "zona de ubicacion":(randint (1,15),choice("ABCDEFGHIJKLMOPQRST"))}
arbol_por_nombre = arbol_por_nombre.insertar_nodo(Dinosaurios["nombre"],Dinosaurios)
arbol_por_codigo = arbol_por_codigo.insertar_nodo(Dinosaurios["codigo"],Dinosaurios)
Dinosaurios = {"nombre": "DIPLODOCUS" ,"codigo":"22134", "zona de ubicacion":(randint (1,15),choice("ABCDEFGHIJKLMOPQRST"))}
arbol_por_nombre = arbol_por_nombre.insertar_nodo(Dinosaurios["nombre"],Dinosaurios)
arbol_por_codigo = arbol_por_codigo.insertar_nodo(Dinosaurios["codigo"],Dinosaurios)
Dinosaurios = {"nombre": "SGIMOLOCH" ,"codigo":"00792", "zona de ubicacion":(randint (1,15),choice("ABCDEFGHIJKLMOPQRST"))}
arbol_por_nombre = arbol_por_nombre.insertar_nodo(Dinosaurios["nombre"],Dinosaurios)
arbol_por_codigo = arbol_por_codigo.insertar_nodo(Dinosaurios["codigo"],Dinosaurios)
Dinosaurios = {"nombre": "ANKILOSAURIO" ,"codigo":"77834", "zona de ubicacion":(randint (1,15),choice("ABCDEFGHIJKLMOPQRST"))}
arbol_por_nombre = arbol_por_nombre.insertar_nodo(Dinosaurios["nombre"],Dinosaurios)
arbol_por_codigo = arbol_por_codigo.insertar_nodo(Dinosaurios["codigo"],Dinosaurios)
Dinosaurios = {"nombre": "STEGOSAURIO" ,"codigo":"01899", "zona de ubicacion":(randint (1,15),choice("ABCDEFGHIJKLMOPQRST"))}
arbol_por_nombre = arbol_por_nombre.insertar_nodo(Dinosaurios["nombre"],Dinosaurios)
arbol_por_codigo = arbol_por_codigo.insertar_nodo(Dinosaurios["codigo"],Dinosaurios)
Dinosaurios = {"nombre": "BRONTOSAURIO" ,"codigo":"66347", "zona de ubicacion":(randint (1,15),choice("ABCDEFGHIJKLMOPQRST"))}
arbol_por_nombre = arbol_por_nombre.insertar_nodo(Dinosaurios["nombre"],Dinosaurios)
arbol_por_codigo = arbol_por_codigo.insertar_nodo(Dinosaurios["codigo"],Dinosaurios)
Dinosaurios = {"nombre": "T-REX" ,"codigo":"91546", "zona de ubicacion":(randint (1,15),choice("ABCDEFGHIJKLMOPQRST"))}
arbol_por_nombre = arbol_por_nombre.insertar_nodo(Dinosaurios["nombre"],Dinosaurios)
arbol_por_codigo = arbol_por_codigo.insertar_nodo(Dinosaurios["codigo"],Dinosaurios)



#3
print("Barrido inorden arbol nombres:")
arbol_por_nombre.inorden()
print()

#4
buscado = "00792"
pos = arbol_por_codigo.busqueda(buscado)
if pos:
    print ("Dinosaurio con el codigo:",buscado," ",pos.datos)
print()

#5
print("T-rex que hay en la isla: ")
arbol_por_nombre.inorden_trex()
print()

#6
buscado = "SGIMOLOCH"
pos = arbol_por_nombre.busqueda(buscado)
if pos:
 nombre_corecto="Stygimoloch"
 arbol_por_nombre.eliminar_nodo(buscado)
 Dinosaurios["nombre"] = nombre_corecto
 arbol = arbol_por_nombre.insertar_nodo(nombre_corecto,Dinosaurios)
 print()




#7
print("Ubicacion de los raptores: ")
arbol_por_nombre.inorden_raptores()
print()

#8
print("Hay",arbol_por_nombre.contar_ocurrencias("DIPLODOCUS"), "Diplodocus en el la isla")
print()

print("barrido fianl:")
arbol_por_nombre.inorden()
print()