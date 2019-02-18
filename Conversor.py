import math

def potencias (base, exponente):
    result = 1
    for i in range(exponente):
        result*= base
    return result

def convetitabinario(numero):
    num =float(numero)
    signo = ""
    if (num<0):
        signo = "1 "
    else:
        signo = "0 "
    num = math.fabs(num)
    entero = int(num)
    pot = 7
    ent = ""
    while (pot>0):
        if (entero>=math.pow (2,pot)):
            ent += "1"
            entero -=math.pow (2,pot)
        else:
            ent += "0"
        pot -= 1
    frat = numero.split (".")
    frac = "0."+frat[1]
    fraccion = float(frac)
    f=""
    pot = 1
    while (pot<8):
        if (fraccion>=math.pow(2,-1*pot)):
            f += "1"
            fraccion-=math.pow(2,-1 * pot)
        else:
            f += "0"
        pot+=1
    expo = len(ent)-1
    expo+= 127
    pot = 7
    ent2 = ""
    while (pot > 0):
        if (expo >= math.pow(2, pot)):
            ent2 += "1"
            expo -= math.pow(2, pot)
        else:
            ent2 += "0"
        pot -= 1
    ent =ent[1:len(ent)]

    res =  signo + ent2+" "+ ent + f
    return res


def convertiradecimal(numero):
    signo = numero[0];
    exponente = numero[1] + numero[2] + numero[3] + numero[4] + numero[5] + numero[6] + numero[7] + numero[8]
    fraccion = numero[9] + numero[10] + numero[11] + numero[12] + numero[13] + numero[14] + numero[15]
    expo = 0
    for i in range(8):
        if exponente[i] == "1":
            expo+= potencias(2,7-i)
    if (expo == 0):
        fraco = 0.0
        expo = 1;
    elif (expo == 255):
        return "Infinito"
    else:
        fraco = 1.0
    for i in range(7):
        if fraccion[i] == "1":
            fraco += (1 / potencias(2, i + 1))
    res = fraco * potencias(2, expo - 127)
    if signo == "1":
        res = -1 * res
    return res


print("Bienvenido al programa")
opcion = input ("Eliga el número de la opción a realizar\n1.Binario a decimal\n2. Decimal a binario\n")
numero = input("Introduce el número binario que desea convertir: ")
if (opcion=="1"):
    print (convertiradecimal(numero))
elif (opcion=="2"):
    print (convetitabinario(numero))
else:
    print ("Ingrese una opción válida")