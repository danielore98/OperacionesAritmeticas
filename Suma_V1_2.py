class OperacionesAritmeticas():
    def ingresarNumeros(self):
        numero1 = float(input('Ingrese sumando 1: '))
        numero2 = float(input('Ingrese sumando 2: '))
        return numero1, numero2

    def suma(self, numero1, numero2):
        return numero2 + numero1


if __name__ == 'main':
    operacion = OperacionesAritmeticas()
    num1, num2 = operacion.ingresarNumeros()
    print(f"{num1} + {num2} = {operacion.suma(num1, num2)}")
