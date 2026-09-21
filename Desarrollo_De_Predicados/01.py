Universo = {
    "Profesor": {
        "Ricardo": ["InteligenciaArtificial"], 
        "Jose": ["ProgramacionLogica"]
    },
    "Estudiante": { 
        "Juan": ["InteligenciaArtificial", "ProgramacionLogica"],
        "Pablo": ["InteligenciaArtificial", "ProgramacionLogica"], 
        "Maria":["InteligenciaArtificial", "ProgramacionLogica"]
    },
    "Calificacion": {
        100, 40, 60
    },
    "Materia": {
        "InteligenciaArtificial": [207], 
        "ProgramacionLogica": [210]
    },

}

Inscripciones = {
    ("Juan", "InteligenciaArtificial") 
    }
Profesores = {
    ("Ricardo", "ProgramacionLogica")
    }
Seriadas = {
    ("ProgramacionLogica", "InteligenciaArtificial")
    }


# Predicados 

# 1.Estudiante
def Estudiantes(x):
    return x in Universo["Estudiante"]

# 2.Profesor
def Profesor(x):
    return x in Universo["Profesor"]

#3. Materia
def materia(x):
    return x in Universo["Materia"]

# 4.Aula
def aula(x):
    return any(x in aulas for aulas in Universo["Materia"].values())

# 5.Inscrito
def inscrito(x, m):
    return (x, m) in Inscripciones

# 6.Imparte
def imparte(p, m):
    return(p, m) in Profesores

# 7.Seriada
def seriada(m1, m2):
    return(m1, m2) in Seriadas

print("Consulta positiva --> Estudiante Juan es:", Estudiantes("Juan"))
print("Consulta negativa --> Estudiante Ricardo es:", Estudiantes("Ricardo"))

print("Consulta positiva --> Profesor Ricardo es:", Profesor("Ricardo"))
print("Consulta negativa --> Profesor Juan:", Profesor("Juan"))

print("Consulta positiva --> Materia Inteligencia_Artificial es:", materia("Inteligencia_Artificial"))
print("Consulta negativa --> Materia 207 es:", materia("207"))

print("Consulta positiva --> Aula 207 es:", aula(207))
print("Consulta negativa --> Aula Inteligencia_Artificial es:", aula("Inteligencia_Artificial"))

print("Consulta positiva --> Juan inscrito en Ingeligencia_Artificial es:", inscrito("Juan", "Inteligencia_Artificial"))
print("Consulta negativa --> Ricardo inscrito en Inteligencia_Artificial es:", inscrito("Ricardo", "Inteligencia_Artificial"))

print("Consulta positiva --> Ricardo imparte en Programacion_Logica es:", imparte("Ricardo", "Programacion_Logica"))
print("Consulta negativa --> Juan imparte en Programacion_Logica es:", imparte("Juan", "Programacion_logica"))

print("Consulta positiva --> Programacion_Logica seriada_con_Inteligencia_Artificial es:", seriada("Programacion_Logica", "Inteligencia_Artificial"))
print("Consulta negativa --> Programacion_Logica seriada_con_207 es:", seriada("Programacion_Logica", "207"))