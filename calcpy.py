#!/usr/bin/env python3
#_*_ coding: utf8 _*_

class Calculadora ():
    def __init__ (self,valor1=0,valor2=0):
        self.valor1 = valor1
        self.valor2 = valor2

    def suma (self):
        return self.valor1+self.valor2

    def resta (self):
        return self.valor1 - self.valor2

    def multiplicacion (self):
        return self.valor1 * self.valor2

    def division (self):
        return self.valor1+self.valor2

    def entrada_datos(self):
        self.valor1 = float(input("Introduzca el primer valor: "))
        self.valor2 = float(input("Introduzca el segundo valor: "))
        return None
    
    def mensaje_menu(self):
        print("""
                CALCULADORA CON POO - PYTHON
                1-SUMA
                2-RESTA
                3-MULTIPLICACION
                4-DIVISION
                CUALQUIER TECLA PARA SALIR
                ENTRADA: """,end="")
        return None
        
    def comparacion (self,entrada):
        if entrada == "1":
            return True
        elif entrada == "2":
            return True
        elif entrada == "3":
            return True
        elif entrada == "4":
            return True
        else:
            return False

    def Menu(self):
        self.mensaje_menu()
        opcion = input()

        while True:
            if self.comparacion(opcion) !=True:
                print("\nSaliendo del programa...")
                break

            self.entrada_datos()
            if opcion == "1":
                print(f"El resultado de la suma es: {self.suma()}")

            elif opcion == "2":
                self.resta()
                #print("resta") 
                print(f"El resultado de la resta es: {self.resta()}")

            elif opcion == "3":
                #self.multiplicacion()
                #print("multiplicacion")
                print(f"El resultado de la multiplicacion es: {self.multiplicacion()}")

            
            elif opcion == "4":
                #print("division")
                self.division()
                print(f"El resultado de la division es: {self.division()}")
            
            self.mensaje_menu()
            opcion = input()

        quit()

