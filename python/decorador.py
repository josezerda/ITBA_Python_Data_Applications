def mi_decorador(func):
    def envoltura():
        print("Algo se está preparando antes de ejecutar la función.")
        func()
        print("Algo se hace después de la función.")
    return envoltura

@mi_decorador
def saluda():
    print("¡Hola Mundo!")

saluda()

