import materiasFunciones as mt

def main():

    # Uso de la función para mostrar materias a las que puedes inscribirte
    print("Materias a las que puedes inscribirte:")
    materias_disponibles = mt.listar_materias_disponibles(mt.materias)
    for materia in materias_disponibles:
        print(materia.ToString())

    print("Materias para rendir: ")
    mt.mostrarNoAprobadas(mt.materias)
if __name__ == "__main__":
    main()