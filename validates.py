
def validar_numero_positivo(valor_input:str)->float:
    '''
    Verifica que el valor ingresado no sea un string vacio y que sea un número entero positivo. Finalmente convierte el str a int.
    Parametro: valor_input (str)
    Retorno: valor_input (float)
    '''
    while valor_input == "" or not valor_input.isdigit() or valor_input.startswith("-") or "." in valor_input or valor_input == "0":
        valor_input = input("\033[31mDebe ingresar un número valido. Vuelva a intentar: \033[0m")
    valor_input = int(valor_input)
    return valor_input


def validar_valor_vacio (valor_input:str)->str:
    while valor_input == "":
        valor_input = input("\033[31mDebe ingresar una respuesta. Vuelva a interarlo: \033[0m")
    return valor_input