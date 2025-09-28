lista_especialidades=[]
lista_cupos=[]

option=0

while option!=10:
    print('''"MENU" 
            "1- Añadir especialidades a la lista" 
            "2- Añadir cupos a las especialidades"
            "3- Mostrar agenda" 
            "4- Consultas cupos de una especialidad" 
            "5- Listar especialidades SIN cupos" 
            "6- Agregar especialidad & Cupos" 
            "7- Ver especialidades sin cupo" 
            "8- Actualizar cupos (Reservar/Cancelar)" 
            "9- Ver agenda con horarios" 
            "10- Salir"''')

    option_letter=True
    option_outnumber=True

    while option_letter or option_outnumber:
        option=str(input("Elija la opcion que desea utilizar:"))

        if (not(option.isdigit()) or option==""):
            print("No es una opcion valida, por favor ingrese una de las opciones: ")
        else:
                option_letter=False
                option=int(option)
                if(option<1 or option>10):
                    print("No es una opcion valida, por favor ingrese una de las opciones: ")
                    option_letter=True
                else:
                    option_outnumber=False

    if option==1:
        add_elements=True
        while(add_elements):
            speciality_checker=True
            aux_speciality=str(input("Que especialidad desea ingresar?: "))
            while(speciality_checker):
                if(aux_speciality=="" or aux_speciality in lista_especialidades):
                    print("Especialidad incorrecta, por favor ingrese nuevamente: ")
                    aux_speciality=str(input("Que especialidad desea ingresar?: "))
                else:
                    speciality_checker=False
                    print("Especialidad ingresada con exito")
                    lista_especialidades.append(aux_speciality)
                    check_more_specialities=input("Para agregar otra, pulse Y. Pulse cualquier otra tecla para finalizar")
                    check_more_specialities=check_more_specialities.upper()
                    if(check_more_specialities!="Y"):
                        add_elements=False

    if option==2:
        for i in range(len(lista_especialidades)):
            print (f"Cuantos cupos se le asignaran a la especialidad {lista_especialidades[i]}: ")
            aux_cupos=input()
            while(not(aux_cupos.isdigit())):
                print("Valor incorrecto, por favor ingrese la cantidad de cupos:")
                aux_cupos=input()
            aux_cupos=int(aux_cupos)
            lista_cupos.append(aux_cupos)
            print("Cupos agregados exitosamente")


    elif option==3:
        for i in range (len(lista_especialidades)):
            print (f"{lista_especialidades[i]}: {lista_cupos[i]} cupos")

    elif option==4:
        aux_request=str(input("Que especialidad desea consultar? "))
        speciality_checker=True
        while(speciality_checker):
            if(aux_request=="" or not(aux_request in lista_especialidades)):
                print("Especialidad incorrecta, por favor ingrese nuevamente: ")
                aux_request=str(input("Que especialidad desea consultar?: "))
            else:
                speciality_checker=False
                index=lista_especialidades.index(aux_request)
                print(f"La especialidad {lista_especialidades[index]} tiene {lista_cupos[index]} cupos")

    elif option==5:
        aux_list=[]
        for i in range (len(lista_especialidades)):
            if(lista_cupos[i]==0):
                aux_list.append(lista_especialidades[i])

        print(aux_list)

    elif option==6:
        add_elements=True
        while(add_elements):
            speciality_checker=True
            aux_speciality=str(input("Que especialidad desea ingresar?: "))
            while(speciality_checker):
                if(aux_speciality=="" or aux_speciality in lista_especialidades):
                    print("Especialidad incorrecta, por favor ingrese nuevamente: ")
                    aux_speciality=str(input("Que especialidad desea ingresar?: "))
                else:
                    speciality_checker=False
                    lista_especialidades.append(aux_speciality)
                    print("Especialidad ingresada con exito. Cuantos cupos desea incorporar?")
                    aux_cupos=input()
                    while(not(aux_cupos.isdigit())):
                        print("Valor incorrecto, por favor ingrese la cantidad de cupos:")
                        aux_cupos=input()
                        aux_cupos=int(aux_cupos)
                    lista_cupos.append(aux_cupos)
                    print("Cupos agregados exitosamente")
                    check_more_specialities=input("Para agregar otra, pulse Y. Pulse cualquier otra tecla para finalizar")
                    check_more_specialities=check_more_specialities.upper()
                    if(check_more_specialities!="Y"):
                        add_elements=False

    elif option==7:
        aux_list=[]
        for i in range (len(lista_especialidades)):
            if(lista_cupos[i]==0):
                aux_list.append(lista_especialidades[i])

        print(aux_list)

    elif option==8:
        flag_menu=True    

        while(flag_menu):
            user_choice=input("Desea reservar o cancelar citas? Escriba Salir para finailzar.")
            while(not(user_choice.isalpha()) or user_choice==""):
                print("No es string o está vacio")
                user_choice=input("Desea reservar o cancelar citas? Escriba Salir para finailzar.")
                
            user_choice=user_choice.lower()
            print("Es un string")

            if(user_choice=="reservar"):
                speciality_checker=True
                aux_speciality=str(input("En que especialidad desea hacer una reserva? v1: "))
                print(aux_speciality)
                aux_speciality=aux_speciality.lower()

                while(speciality_checker):
                    if(aux_speciality=="" or (not(aux_speciality in lista_especialidades))):
                        print("Especialidad incorrecta, por favor ingrese nuevamente: ")
                        aux_speciality=str(input("En que especialidad desea hacer una reserva? v2: "))
                    else:
                        speciality_checker=False
                        index=lista_especialidades.index(aux_speciality)
                        print(f"Quedan {lista_cupos[index]} cupos en la especialidad de {lista_especialidades[index]}")
                        if(lista_cupos[index]>0):
                            lista_cupos[index]-=1
                            print("Se ha hecho una reserva con exito.")
                            print(f"Quedan {lista_cupos[index]} cupos en la especialidad de {lista_especialidades[index]}")
                        else:
                            print(f"NO Quedan cupos en la especialidad de {lista_especialidades[index]}")     

            elif(user_choice=="cancelar"):
                speciality_checker=True
                aux_speciality=str(input("En que especialidad desea cancelar una reserva?: "))
                while(speciality_checker):
                    if(aux_speciality=="" or (not(aux_speciality in lista_especialidades))):
                        print("Especialidad incorrecta, por favor ingrese nuevamente: ")
                        aux_speciality=str(input("En que especialidad desea hacer una reserva?: "))
                    else:
                        speciality_checker=False
                        index=lista_especialidades.index(aux_speciality)
                        lista_cupos[index]+=1
                        print("La reserva ha sido cancelada")
                        print(f"Quedan {lista_cupos[index]} cupos en la especialidad de {lista_especialidades[index]}")

            elif(user_choice=="salir"):
                print("Gracias")
                flag_menu=False

            else:
                print("No es una opcion correcta. Por favor ingrese, si desea reservar, cancelar o salir")
                        

    elif option==9:
        ##Suponiendo que todas las especialidades trabajan de 10:00 a 20:00 horas, y hay 10 cupos como maximo##
        ##Cada especialidad, tendra distinta cantidad de horas, y finalizaría la jornada antes, siempre con un maximo de 10 horas##
        for i in range (len(lista_especialidades)):
            turnos=(10-lista_cupos[i])
            hora_maxima=10+turnos
            if(turnos>0):
                print(f"{lista_especialidades[i]} tiene {turnos} turnos por lo cual su jornada es de")
                print(f"10:00 a {hora_maxima}:00 horas")
            else:
                print(f"La especialidad de {lista_especialidades[i]} no tiene turnos el dia de la fecha")


    elif option==10:
        print("GRACIAS")
        print("---------------")


print("---------------")
print("---------------")
print("---------------")