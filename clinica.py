from menu import *

pacientes = []

salida = ""

while salida == "":
    mensaje_menu = '''
    \033[32mSistema de Gestión de Clínica\033[0m
    1. Cargar pacientes
    2. Mostrar todos los pacientes
    3. Buscar pacientes por número de Historia Clínica
    4. Ordenar pacientes por número de historia clínica
    5. Mostrar paciente con más días de internación
    6. Mostrar paciente con menos días de internación
    7. Cantidad de pacientes con más de 5 días de internación
    8. Promedio de días de internación de todos los pacientes
    9. Salir

    -Ingrese el número de la opcion de menu que desea ingresar: '''

    opcion_menu = input(mensaje_menu)

    match opcion_menu:
        case "1":
            cargar_pacientes(pacientes)
        case "2":
            mostrar_pacientes(pacientes)
        case "3":
            buscar_pacientes_historia_clinica(pacientes)
        case "4":
            ordenar_pacientes_historia_clinica(pacientes)
        case "5":
            paciente_mas_dias_internacion(pacientes)
        case "6":
            paciente_menos_dias_internacion(pacientes)
        case "7":
            pacientes_mas_5_dias_internacion(pacientes)
        case "8":
            promedio_dias_internacion(pacientes)
        case "9":
            print("\033[32mSaliendo del programa...\033[0m")
            salida = "saliendo"
        case _:
            print("\033[31mOpción de menu invalida. Vuelva a intentar.\033[0m")