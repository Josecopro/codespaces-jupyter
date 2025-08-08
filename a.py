def Opciones(lista, respuesta = [], totalrespuesta = []):

    if len(respuesta) == len(lista):
        totalrespuesta.append(respuesta[:])
        return
    for i in range(len(lista)):
        if i not in respuesta:
            respuesta.append(i)
            Opciones(lista, respuesta, totalrespuesta)
            respuesta.pop()
    return totalrespuesta


Opciones = Opciones([1, 2, 3])

print(Opciones)


def Opciones2(lista, respuesta = "", totalrespuesta = []):
    if len(respuesta) == len(lista):
        totalrespuesta.append(respuesta)
        return
    for i in range(len(lista)):
        if str(i) not in respuesta:
            Opciones2(lista, respuesta + str(i), totalrespuesta)
    return totalrespuesta


Opciones2 = Opciones2([1, 2, 3])

print(Opciones2)