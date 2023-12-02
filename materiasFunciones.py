class Materia:
    def __init__(self, num, nombre, regulares, aprobadas,regular, aprobada):
        self.num = num
        self.nombre = nombre
        self.regulares = regulares
        self.aprobadas = aprobadas
        self.regular = regular
        self.aprobada = aprobada

    def ToString(self):
        return f"{self.num} | {self.nombre}"

t = True
f = False

materias = [
    Materia(1, "AM1", [], [], f,f),
    Materia(2, "AGA", [], [],t,f),
    Materia(3, "FIS1", [], [],f,f),
    Materia(4, "Ing1", [], [],t,t),
    Materia(5, "LED", [], [],t,t),
    Materia(6, "AED", [], [],t,t),
    Materia(7, "ACO", [], [],t,f),
    Materia(8, "SPN", [], [],t,t),
    Materia(9, "AM2", [1,2], [],f,f),
    Materia(10, "FIS2", [1,3], [],f,f),
    Materia(11, "ISO", [], [],t,t),
    Materia(12, "Ing2", [4], [],t,t),
    Materia(13, "SSL", [5,6], [],f,f),
    Materia(14, "PPR", [5,6], [],t,t),
    Materia(15, "SOP", [7], [],t,f),
    Materia(16, "ASI", [6,8], [],t,f),
    Materia(17, "PyE", [1,2], [],f,f),
    Materia(18, "Eco", [], [1,2],f,f),
    Materia(19, "BD", [13,16], [5,6],f,f),
    Materia(20, "DDS", [14,16],[5,6],f,f),
    Materia(21, "CDD", [],[3,7],f,f),
    Materia(22, "AN", [9], [1,2],f,f),
    Materia(23, "DSI", [14,16], [4,6,8],f,f),
    Materia(99, "SeminarioAnalista", [16], [6,8,13,14],f,f)
    ]

def mostrarMaterias(materias):
    for materia in materias:
        print(materia.ToString())

def mostrarRegulares(materias):
    regulares = []
    for materia in materias:
        if materia.regular:
            regulares.append(materia)
            print(materia.ToString())
    return regulares

def mostrarAprobadas(materias):
    aprobadas = []
    for materia in materias:
        if materia.aprobada:
            aprobadas.append(materia)
            print(materia.ToString())

def listar_materias_disponibles(materias):
    inscribibles = []
    for materia in materias:
        puede_inscribirse = True
        
        if materia.aprobada == False and materia.regular == False:
            # Verificar si tiene todas las materias regulares requeridas
            for materia_regular in materia.regulares:
                if not materias[materia_regular - 1].regular:
                    puede_inscribirse = False
                    break
            
            # Verificar si tiene todas las materias aprobadas requeridas
            for materia_aprobada in materia.aprobadas:
                if not materias[materia_aprobada - 1].aprobada:
                    puede_inscribirse = False
                    break
            
            # Si cumple con todos los requisitos, se agrega a la lista de inscribibles
            if puede_inscribirse:
                inscribibles.append(materia)

    return inscribibles

def mostrarNoAprobadas(materias):
    for materia in materias:
        if not materia.aprobada and materia.regular:
            print(materia.ToString())
