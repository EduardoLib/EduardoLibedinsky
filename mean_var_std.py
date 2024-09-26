import numpy as np

 
def calculations(lista):
    if len(lista) != 9:
        raise ValueError("La lista debe contener nueve números")
    
    # Convertir la lista en una matriz de 3x3
    matriz = np.array(lista).reshape(3, 3)
    
    # Calcular los valores solicitados
    calculos = {
        'media': [np.mean(matriz, axis=0).tolist(), np.mean(matriz, axis=1).tolist(), np.mean(matriz)],
        'varianza': [np.var(matriz, axis=0).tolist(), np.var(matriz, axis=1).tolist(), np.var(matriz)],
        'desviacion_std': [np.std(matriz, axis=0).tolist(), np.std(matriz, axis=1).tolist(), np.std(matriz)],
        'max': [np.max(matriz, axis=0).tolist(), np.max(matriz, axis=1).tolist(), np.max(matriz)],
        'min': [np.min(matriz, axis=0).tolist(), np.min(matriz, axis=1).tolist(), np.min(matriz)],
        'suma': [np.sum(matriz, axis=0).tolist(), np.sum(matriz, axis=1).tolist(), np.sum(matriz)]
    }

    return calculos   


try:
    entrada = input("Por favor, ingrese 9 números separados por comas: ")
    lista = [int(num) for num in entrada.split(",")]
    
    resultado = calculations(lista)
    print("Resultados:")
    print(resultado)
except ValueError as e:
    print(f"Error: {e}")