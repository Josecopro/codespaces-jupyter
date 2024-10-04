def resta_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Los arrays deben tener la misma longitud")
    return [a - b for a, b in zip(array1, array2)]

# Ejemplo de uso
array1 = [10, 20, 30, 40]
array2 = [1, 2, 3, 4]
resultado = resta_arrays(array1, array2)
print(resultado)  # Output: [9, 18, 27, 36]