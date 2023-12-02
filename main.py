import materiasFunciones as mt
import os
import platform

def limpiar_consola():
    input("Presiones cualquier tecla para continuar...")
    sistema_operativo = platform.system()

    if sistema_operativo == 'Windows':
        os.system('cls')  # En Windows
    else:
        os.system('clear')  # En Linux/macOS

def validar_opcion_entre_a_y_b(mensaje, a, b):
    op = int(input(mensaje))
    while a > op > b:
        op = int(input(mensaje))
    return op

def menu():
    print("1. Mostrar materia.")
    print("2. Editar materia.")
    print("3. Materias para inscribirme.")
    print("4. Materias para rendir.")
    print("5. Salir.")
    print("")
    op = validar_opcion_entre_a_y_b("Ingrese la opcion deseada: ", 1, 4)
    return op
    
def menu_op1():
    print("1. Editar regularidad.")
    print("2. Editar aprobación.")
    print("")
    op = validar_opcion_entre_a_y_b("Ingrese la opcion deseada: ",1,2) 
    return op

def mostrar_materia(materias):
    num = int(input("Numero de materia: "))
    for materia in materias:
        if num == materia.num:
            print(materia.ToString())
    limpiar_consola()

def editar_materia(materias):
    numMateria = int(input("Numero de materia: "))
    encontrada = False
    for materia in materias:
        if numMateria == materia.num:
            encontrada = True
            opcion1 = menu_op1()
            if opcion1 == 1:
                materia.regular = not materia.regular
            else:
                materia.aprobacion = not materia.aprobacion
            print("")
            print("Resultado: ")
            print("")
            print(materia.ToString())
            print("")
    if not encontrada:
        print(f"No se encontro ninguna materia con el numero {numMateria}")
    limpiar_consola()


def main():
    op = menu()            
    execute = True
    while execute:
        
        if op == 1: #Mostrar materia
            print("")
            mostrar_materia(mt.materias)
            op = menu()            
            
        elif op == 2: # Editar materia
            print("")
            editar_materia(mt.materias)
            op = menu()
        elif op == 3:
            print("")
            materias_inscribirse = mt.listar_materias_disponibles(mt.materias)
            for materia in materias_inscribirse:
                print(materia.ToString())
            print("")
            limpiar_consola()
            op = menu()
        elif op == 4: #Materias para rendir
            print("")
            print("Materias para rendir: ")
            mt.mostrarNoAprobadas(mt.materias)
            print("")
            limpiar_consola()
            op = menu()

        else:
            execute = False
            limpiar_consola()
    
if __name__ == "__main__":
    main()