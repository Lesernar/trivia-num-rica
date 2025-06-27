def trivia_fetch(num):
    trivia_data = {
        42: "El 42 es la respuesta a la vida, el universo y todo lo demas.",
        1000: "1000 es diez veces 100, y es un número redondo.",
        1: "El número 1 es el primer número natural y también es considerado un número primo.",
        2: "El número 2 es el único número par que es primo.",
        3: "El número 3 es el primer número impar y también es un número primo.",
        7: "El número 7 es considerado un número de la suerte en muchas culturas.",
    }
    return {
        "number": num,
        "trivia": trivia_data.get(num, "No hay trivia disponible para este número.")
    }

def main():
    print("🎉 Bienvenido a la trivia de números 🎉")
    while True:
        try:
            entrada = input("Ingresa un número (o escribe 'salir' para terminar): ")
            if entrada.lower() == 'salir':
                print("¡Gracias por usar la trivia! ¡Adiós!")
                break
            num = int(entrada)
            resultado = trivia_fetch(num)
            print(f"Número: {resultado['number']}")
            print(f"Trivia: {resultado['trivia']}\n")
        except ValueError:
            print("Por favor ingresa un número válido o 'salir'.")

if __name__ == "__main__":
    main()
