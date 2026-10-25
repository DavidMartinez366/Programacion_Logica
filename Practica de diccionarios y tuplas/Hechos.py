
hechos_entrevistas = { #Uso de diccionarios
    "ardilla": (
        "EsMamifero",
        "TieneColaFrondosa",
        "TrepaArboles",
        "ComeSemillas",
        "EsArdilla",
    ),
    "colibri": (
        "EsAve",
        "PicoLargoYDelgado",
        "ComeNectar",
        "VuelaHaciaAtras",
        "EsColibri",
    ),
}

vinculos_entrevista = (
    (
        ("EsMamifero", "TieneColaFrondosa", "TrepaArboles", "ComeSemillas"),
        "EsArdilla",
    ),
    (
        ("EsAve", "PicoLargoYDelgado", "ComeNectar", "VuelaHaciaAtras"),
        "EsColibri",
    ),
)

def hechos_entrevista(animal):
    animal = animal.lower()
    if animal in hechos_entrevistas:
        print(f"Hechos para {animal}: {hechos_entrevistas[animal]}") 
if __name__ == "__main__":
    hechos_entrevista("ardilla")
    print("\n")
    hechos_entrevista("colibri")