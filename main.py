import connector

#Crear una funcion main que pasa variables a otras funciones

lista_nombres = []
lista_asignaturas = []
lista_fechas = []

def main():
    opcion = 0

    while opcion != "s":

        opcion = input("Que quieres hacer, crear una nueva tarea (c), ver tareas pendientes (p) o salir (s): ").lower()

        if opcion == "c":
            nombre_tarea = input("Escribe el nombre de tu tarea: ")
            asignatura = input("Escribe la asignatura de la tarea: ")
            fecha = input("Cuando tienes esta tarea: ")
            crear_tarea(asignatura, nombre_tarea, fecha)

        elif opcion ==  "p":
            tareas_pendientes()

        elif opcion == "s":
            print("Adios")


# Funcion que cree tareas pendientes eligiendo la asignatura, nombre de la tarea y fecha
def crear_tarea(asignatura, nombre_tarea, fecha):
    
    connector.setJSON((connector.getTarea()+":separator:"+nombre_tarea), (connector.getAsignatura()+":separator:"+asignatura), (connector.getFecha()+":separator:"+fecha))

    print(f"Se ha creado correctamente la tarea {nombre_tarea} de la asignatura {asignatura} el dia {fecha} \n")


#crear la funcion que asigne a tres listas distintas las tres variables: nombre, asignatura y fecha

def tareas_pendientes():
    lista_nombres = []
    lista_asignaturas = []
    lista_fechas = []

    tarea = connector.getTarea()
    tarea = tarea.split(":separator:")
    for i in tarea: 
        if i !="": lista_nombres.append(i)



    asignatura = connector.getAsignatura()
    asignatura = asignatura.split(":separator:")
    for i in asignatura: 
        if i !="": lista_asignaturas.append(i)
    
    fechas = connector.getFecha()
    fechas = fechas.split(":separator:")
    for i in fechas: 
        if i !="": lista_fechas.append(i)    

    for i in range(len(lista_nombres)):
        print(f"tienes una tarea pendiente llamada, {lista_nombres[i]} de la asignatura {lista_asignaturas[i]} el dia {lista_fechas[i]} \n")
# Las tareas se deben guardar para poder verlas en cualquier momento desde la consola



# hacer funcion que dependiendo de la letra escrita de la opcion de: 
    #1.- Escribir nueva tarea (Hecho)
    #2.- Ver tareas pendientes (Hecho)
    #3.- poder marcar una tarea como completada y que esta se elimine



# (opcional) funcion que se encargue de avisar al usuario de sus tareas

main()
