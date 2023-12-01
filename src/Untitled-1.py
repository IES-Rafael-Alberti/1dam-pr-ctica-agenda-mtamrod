def restriccion_telefono(numero_tlf):
    numero_tlf = numero_tlf.replace(" ", "")

    if not numero_tlf.startswith("+34") and len(numero_tlf) == 9:
        reestriccion = True
    elif numero_tlf.startswith("+34") and len(numero_tlf) == 12:
        reestriccion = True
    else:
        reestriccion = False

    while reestriccion == False:
        numero_tlf = input("Introduce un teléfono válido: ")
        numero_tlf = numero_tlf.replace(" ", "")

        if not numero_tlf.startswith("+34") and len(numero_tlf) == 9:
            reestriccion = True
        elif numero_tlf.startswith("+34") and len(numero_tlf) == 12:
            reestriccion = True

    return reestriccion

def main():
    numero_tlf = input("Introduce numero: ")
    print (restriccion_telefono(numero_tlf))

if __name__ == "__main__":
    main()