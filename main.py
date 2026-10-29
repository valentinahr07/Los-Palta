import json


def cargar_lugares():
    with open("lugares.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def obtener_ubicacion():
    return input("¿Dónde te encuentras?: ").strip().lower()


def preguntar_interes():
    return (
        input("Hay información histórica cerca. ¿Quieres verla? (si/no): ")
        .strip()
        .lower()
    )


def buscar_lugar(ubicacion, lugares):
    return lugares.get(ubicacion)


def mostrar_informacion(nombre, datos):
    print(f"\n📍 {nombre.title()}")
    for hecho in datos["historia"]:
        print(f"• {hecho}")


def main():
    lugares = cargar_lugares()

    while True:
        ubicacion = obtener_ubicacion()
        respuesta = preguntar_interes()

        if respuesta != "si":
            print("Volviendo al inicio...\n")
            continue

        lugar = buscar_lugar(ubicacion, lugares)

        if lugar:
            mostrar_informacion(ubicacion, lugar)
        else:
            print("\nNo tenemos información de ese lugar.")

        break


if __name__ == "__main__":
    main()
