import os
import getpass

valida = False
limit = 4
while valida == False:
    print("Bienvenido a Decryp-Ubee")
    red = input("Ingresa los ultimos 4 digitos del SSID: " )
    red = red.upper()
    d_red = len(red)
    mac = input("Ingresa la MAC de la red sin los 2 puntos: ")
    mac = mac.upper()
    digitos = len(mac)
    USER = getpass.getuser()

    if d_red == 4:
        for i in red:
            if i == ":" or i == "," or i == "#":
                print(f"el SSID no puede llevar: '{i}' pues es un caracter especial o un espacio")

            elif i == "-":
                print("EL SSID no puede llevar numeros negativos")

            else:
                if digitos == 16:
                    for i in mac:
                        if i == ":":
                            print(f"LA MAC no debe contener {i}")

                        elif i == "@":
                            print(f"la MAC solo admite nuemeros y letras {i} es un caracter especial")

                        elif mac == "000000000000":
                            print(f"La MAC {mac} no es valida")

                        elif i == "-":
                            print("La MAC no pude llevar numeros negativos")

                        else:
                            print(f"La clave de la red Ubee-{red} con mac {mac[0:2]}:{mac[2:4]}:{mac[4:6]}:{mac[6:8]}:{mac[8:10]}:{mac[10:12]}:{mac[12:14]}:{mac[14:16]} es: '{mac[2:14]}{red}'")
                            valida = True
                            file = open(f"/home/{USER}/Documentos/clave.txt", "w")
                            file.write(f"La clave de la red Ubee-{red} con mac {mac[0:2]}:{mac[2:4]}:{mac[4:6]}:{mac[6:8]}:{mac[8:10]}:{mac[10:12]}:{mac[12:14]}:{mac[14:16]} es:" + os.linesep)
                            file.write(f"'{mac[2:14]}{red}'")
                            file.close()
                            break


    elif d_red <= 0:
        print("El SSID debe tener 4 digitos")

    elif d_red > 4:
        print("SSID no debe superar 4 caracteres")

    elif digitos < 16:
        print(f"La mac: {mac} esta incompleta")

    elif digitos > 16:
        print(f"La MAC: {mac} excede los 16 digitos")



#
