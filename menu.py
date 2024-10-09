from validates import validar_numero_positivo, validar_valor_vacio

#OPCION 1
def cargar_pacientes(pacientes:list)->list:
    '''
    Carga al sistema la cantidad de pacientes que el usuario desee.
    Parametro: pacientes (list)
    Retorno: pacientes (list)
    '''
    numero_pacientes = validar_numero_positivo(input("¿Cuantos pacientes desea ingresar?: "))

    for i in range(numero_pacientes):
        print(f"\nPACIENTE N°{i+1}:")
        historia_clinica = validar_numero_positivo(input("-Ingrese el número de Historia Clínica: ")) 
        nombre = validar_valor_vacio(input("-Nombre del paciente: "))
        edad = validar_numero_positivo (input("-Edad: "))
        diagnostico = validar_valor_vacio(input("-Diagnostico: "))
        dias_internacion = validar_numero_positivo(input("-Días de internación: "))

        pacientes.append([historia_clinica,nombre,edad,diagnostico,dias_internacion])
    
    print("\033[32m¡PACIENTE AGREGADO EXITOSAMENTE!\033[0m")   
    return pacientes


#OPCION 2
def mostrar_pacientes(pacientes:list)->None:
    '''
    Imprime en pantalla la lista de pacientes.
    Parametro: pacientes (list)
    Retorno: None
    '''

    if pacientes == []:
        return print("\033[31mNO hay pacientes registrados.\033[0m")
    
    for i in range(len(pacientes)): 
                print("-------------------------------------")
                print(f"\033[32m[{i+1}] N° Historia Clínica: {pacientes[i][0]} | Nombre: {pacientes[i][1]} | Edad: {pacientes[i][2]} | Diagostico: {pacientes[i][3]} | Días de internación: {pacientes[i][4]}\033[0m")


#OPCION 3
def buscar_pacientes_historia_clinica(pacientes:list)->None:
    '''
    Busca en la lista de pacientes si el número de Historia Clínica existe y si lo hace imprime los datos del paciente..
    Parametro: pacientes (list)
    Retorno: None
    '''

    if pacientes == []:
        return print("\033[31mNO hay pacientes registrados.\033[0m")
    
    print("\n- Buscar paciente por Historia Clínica -")
    paciente_a_buscar = int(input("Ingrese el número de historia clinica: "))
    paciente_encontrado = []

    for paciente in pacientes:
        if paciente_a_buscar == paciente[0]:
            print(paciente)
            paciente_encontrado = paciente
    
    if paciente_encontrado != []:
        print("\nPACIENTE ENCONTRADO")
        print(f"\n\033[32m-N° Historia Clínica: {paciente_encontrado[0]} | Nombre: {paciente_encontrado[1]} | Edad: {paciente_encontrado[2]} | Diagnóstico: {paciente_encontrado[3]} | Dias de internación: {paciente_encontrado[4]}\033[0m")
    else:
        print("\n\033[31mNO existe un paciente con ese número de Historia Clinica.\033[0m")


#OPCION 4
def ordenar_pacientes_historia_clinica(pacientes:list)->None:
    '''
    Ordenar la lista de pacientes por el número de Historia Clínica en forma ascendente.
    Parametro: pacientes (list)
    Retorno: None
    '''

    if pacientes == []:
        return print("\033[31mNO hay pacientes registrados.\033[0m")
    
    for i in range(len(pacientes)):
            for j in range(0, len(pacientes) - i - 1):
                if pacientes[j][0] > pacientes[j + 1][0]:
                    pacientes[j], pacientes[j + 1] = pacientes[j + 1], pacientes[j]

    print("\nLista de pacientes ordenada por Historial Clinico de forma ascendente:")
    for paciente in pacientes:
        print(f"\n \033[32mHistoria Clínica: {paciente[0]} | Nombre: {paciente[1]} | Edad: {paciente[2]} | Diagnóstico: {paciente[3]} | Días de internación: {paciente[4]}\033[0m")


#OPCION 5
def paciente_mas_dias_internacion(pacientes:list)->None:
    '''
    Busca al paciente con más días de internación e imprime sus datos en pantalla.
    Parametro: pacientes (list)
    Retorno: None
    '''

    if pacientes == []:
        return print("\033[31mNO hay pacientes registrados.\033[0m")
    
    paciente_mas_dias = pacientes[0]

    for paciente in pacientes:
        if paciente[4] > paciente_mas_dias[4]:
            paciente_mas_dias = paciente
    
    respuesta = (f"\n\033[32mEl paciente con mas días de internación fue {paciente_mas_dias[1]} con {paciente_mas_dias[4]} días de internación:\033[0m")
    print(respuesta)


#OPCION 6
def paciente_menos_dias_internacion(pacientes:list)->None:
    '''
    Busca al paciente con menos días de internación e imprime sus datos en pantalla.
    Parametro: pacientes (list)
    Retorno: None
    '''

    if pacientes == []:
        return print("\033[31mNO hay pacientes registrados.\033[0m")
    
    paciente_menos_dias = pacientes[0]

    for paciente in pacientes:
        if paciente[4] < paciente_menos_dias[4]:
            paciente_menos_dias = paciente
    
    respuesta = (f"\n\033[32mEl paciente con menos dias de internación fue {paciente_menos_dias[1]} con {paciente_menos_dias[4]} días de internación:\033[0m")
    print(respuesta)


#OPCION 7
def pacientes_mas_5_dias_internacion(pacientes:list)->None:
    '''
    Recorre la lista de pacientes e imprime en pantalla cuántos pacientes tienen más de 5 días de internación.
    Parametro: inventario (list)
    Retorno: None
    '''

    if pacientes == []:
        return print("\033[31mNO hay pacientes registrados.\033[0m")
    
    pacientes_mas_5_dias = 0

    for paciente in pacientes:
        if paciente[4] > 5:
            pacientes_mas_5_dias += 1

    print(f"\033[32mCantidad de pacientes con más de 5 días de internación: {pacientes_mas_5_dias}.\033[0m")

#OPCION 8
def promedio_dias_internacion(pacientes:list)->None:
    '''
    Calcula e imprime en pantalla el promedio de días de internacíon de todos los pacientes registrados.
    Parametro: inventario (list)
    Retorno: None
    '''

    if pacientes == []:
        return print("\033[31mNO hay pacientes registrados.\033[0m")
    
    total_dias_internacion = 0
    
    for paciente in pacientes:
        total_dias_internacion += paciente[4]
    
    total_pacientes = len(pacientes)
    promedio_dias_internacion = total_dias_internacion // total_pacientes

    print(f"\033[32mPromedio de días de internación: {promedio_dias_internacion} días.\033[0m")


































