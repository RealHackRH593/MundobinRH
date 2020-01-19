#-*galery/python3
import random
import getopt
import time
import os
import sys
import datetime
from random import randint

#COLORES
rojo = '\033[31;1m'
azul = '\033[34;1m'
verde = '\033[32;1m'
amarillo = '\033[33;1m'
morado = '\033[35;1m'
celeste = '\033[36;1m'
plomo = '\033[30;1m'
close = '\033[0m'

##DATOS
rest = "xxxxxxxxxx"
list = [2022,2023,2024,2025,2026,2027]
list2 = ['ESTADOS UNIDOS', 'BRAZIL', 'COLOMBIA', 'ESPAÑA', 'SINGAPUR', 'CANADA', 'ALEMANIA']
nume = random.randrange(500000, 599999)
masterc = str("{0}{1}". format(nume, rest))
nume2 = random.randrange(400000, 499999)
visa = str("{0}{1}". format(nume2, rest))
nume3 = random.randrange(30000, 39999)
amex = str("{0}{1}". format(nume3, rest))
nume4 = random.randrange(600000, 699999)
disc = str("{0}{1}". format(nume4, rest))
cvv =random.randint(100, 999)
cid = random.randint(1000, 9999)
data3 = random.choice(list2)
cpf = random.randrange(1, 99999999999)
by = 'BY : @★RealHackRH★_593'
x = "x"
r = "xxxxxx"
sp = '|'
space = '\n==================================================================\n@MundoNetRH (Telegram)\n==================================================================\n'
it = "................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................"

#GENERADOR BASADO EN ALGORITMO LUHN
def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """

    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )

###GENERACION DE XXXXXXXXXXXX

def ccgen(bin_format):
    out_cc = ""
    if len(bin_format) == 16:
#Iteration over the bin
        for i in range(15):
            if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                out_cc = out_cc + bin_format[i]
                continue
            elif bin_format[i] in ("x and X"):
                out_cc = out_cc + str(randint(0,9))
            else:
                print(verde)
                print("\nERROR: EL BIN " ,bin_format, "NO ES VALIDO\n")
                print("POR FAVOR INTRODUCE UN BIN VALIDO QUE CONTENGA 15 O 16 DIGITOS Y LAS 'x' SEAN MINUSCULAS")
                print("SI ESTO CONTINUA COMUNICATE CON @REALHACKRH593 (Telegram)")

#Generate checksum (last digit) -- IMPLICIT CHECK
        for i in range(10):
            checksum_check = out_cc
            checksum_check = checksum_check + str(i)

            if cardLuhnChecksumIsValid(checksum_check):
                out_cc = checksum_check
                break
            else:
                checksum_check = out_cc

    else:
        print(verde)
        print("\nERROR: EL BIN " ,bin_format, "NO ES VALIDO\n")
        print("POR FAVOR INTRODUCE UN BIN VALIDO QUE CONTENGA 15 O 16 DIGITOS Y LAS 'x' SEAN MINUSCULAS O MAYUSCULA")
        print("SI ESTO CONTINUA COMUNICATE CON @REALHACKRH593 (Telegram)")

    return(out_cc)

#RANDOM CCV GEN
def ccvgen():
    num = randint(10,999)

    if num < 100:
        ccv = "0" + str(num)
    else:
        ccv = str(num)

    return(ccv)

#CHECK GEN
def checker():
    chec = ['\033[32;1mLIVE\033[33;1m', '\033[31;1mDIE\033[33;1m','\033[35;1mUNKNOWN\033[33;1m']
    check =random.choice(chec)
    return(check)

#DATA1GEN
def data1gen():
    data1 = random.randrange( 1, 12)
    if data1 < 10:
        date = "0" + str(data1)
    else:
        date = str(data1)

    return(date)

###DATA2GEN
def data2gen():
    data2 = random.choice(list)
    return(data2)

######EXTRAPOLACION BASICA
def genbasico():
 ba = (bin1[0:10])
 ba2 = (bin2[0:10])
 genba = "{0}{1}". format(ba, r)
 genba2 = "{0}{1}". format(ba2, r)
 print("EXTRAPOLACION EXITOSA : ",genba)
 print("EXTRAPOLACION EXITOSA : ",genba2)
 return(by)

#####EXTRAPOLACION MEDIA
def genmedio():
 ex = (bin1[0:7])
 ex2 = (bin2[0:7])
 tra = (bin1[8:10])
 tra2 = (bin2[8:10])
 po = (bin1[12:14])
 po2 = (bin2[12:14])
 la = (bin1[15:])
 la2 = (bin2[15:])

 gen = "{a}{y}{b}{y}{y}{c}{y}{d}".format(a=(ex), y=x, b=(tra), c=(po), d=(la))
 gen2 = "{a}{y}{b}{y}{y}{c}{y}{d}".format(a=(ex2), y=x, b=(tra2), c=(po2), d=(la2))
 print("EXTRAPOLACION FABULOSA : ",gen)
 print("EXTRAPOLACION FABULOSA : ",gen2)
 return(by)


###EXTRAPOLACION AVANZADA
def genavanzado():
 comp = str("{0}{1}". format(bin1[9], bin1[10]))
 comp2 = str("{0}{1}". format(bin2[9], bin2[10]))
 sum1 = (int(comp[0]) + int(comp2[0]))
 sum2 = (int(comp[1]) + int(comp2[1]))
 result1 = str(int(sum1) / int("2")* 5)
 result2 = str(int(sum2) / int("2")* 5)

 add = (str("{0}{1}". format(result1[0], result1[1])))
 add2 = (str("{0}{1}". format(result2[0], result2[1])))
 extrapolado = (int(add) + int(add2))

 fingen = "{0}{1}{2}{3}{4}".format(bin1[0:6], x, x, extrapolado, r)
 print("EXTRAPOLACION SUPER VIP : ",fingen)
 return(by)

### ACCES
os.system ("clear")
os.system ("cowsay -f eyes •MUNDO RealHackRH_593• | lolcat")
os.system ("toilet -f big ' RealHackRH' -F gay | lolcat")
print(amarillo)
nic = str(input(' TU NICK BINERO PARA EL MUNDOCARDING ★RH★:  '))
os.system ("clear")
time.sleep(1)

######By: Boss
while True:
    os.system ("toilet -f big ' CC_GEN_RH' -F gay | lolcat")
    print("\n\n\033[33;1m HOLA \033[31;1m†★",nic,"★†\033[33;1m BIENVENIDO AL MUNDO ☆REALKING RH☆\n  ★SOMOS CALIDAD Y NO CANTIDAD★ RECUERDANOS\n")
    time.sleep(2)
    print('	    +——————————————————————————————+')
    print('                | MUNDO BINS ★RH★ PRO  |')
    print('	    +——————————————————————————————+')
    print(azul)
    print('  [ 1 ] TARGETAS DE CREDITO MASTERCARD')
    print('  [ 2 ] BUSCADOR DE BINS VISA')
    print('  [ 3 ] BUSCADOR DE BINS AMEX')
    print('  [ 4 ] BUSCADOR DE BINS DISCOVER')
    print('  [ 5 ] GENERADOR VIP DE BINS')
    print('  [ 6 ] MULTI EXTRAPOLADOR DE CC')
    print('  [ 7 ] SALIR DEL SCRIPT\n')

    bi = str(input(' \033[01;33m%%%%%%\033[01;34m%%%%\033[01;31m%%%%\033[01;32m MUNDO BINS ★RH★ \033[01;33m%%%%%%\033[01;34m%%%%\033[01;31m%%%%\033[01;32m  # \033[01;37m'))

    if bi == '1':
        os.system ("clear")
        time.sleep(1)
        print("$ BUSCANDO TARGETAS DE CREDITO CON INJECCION RH",it)
        time.sleep(10)
        os.system ("clear")
        print(verde)
        print(space)
        print('TARGETA DE CREDITO:',masterc)
        print('CVV :',cvv)
        print('FECHA :',data1gen(),sp,data2gen())
        print('IP :' ,data3)
        print('CPF DE LA TARGETA :',cpf)
        print(by)
        print(space)
        print('AHORA DEBES PROBAR EN DIRERENTES PAGINAS TU CC' ,masterc,'Y SIQUIERES QUE TE FUNCIONE DEBES EXTRAPOLAR, ALGUNAS SON \nMULTIFUNCIONALES Y PUES ALGUNAS PUEDEN JALAR EN COMPRAS, ALGUNAS \nPUEDEN ESTAR QUEMADAS O MUERTAS, SOLO DEBES PROBAR UNA POR UNA Y \nTENER PACIENCIA \nSI NO TE FUNCIONA CON ESE PAIS PUEDES PROBAR CON ESTADOS UNIDOS\n')
        time.sleep(2)

    elif bi == '2':
        os.system ("clear")
        time.sleep(1)
        print("$ BUSCANDO TARGETAS DE CREDITO CON INJECCION RH",it)
        time.sleep(10)
        os.system ("clear")
        print(celeste)
        print(space)
        print('TARGETA DE CREDITO:',visa)
        print('CVV :',cvv)
        print('FECHA :',data1gen(),sp,data2gen())
        print('IP :' ,data3)
        print('CPF DE LA TARGETA :',cpf)
        print(by)
        print(space)
        print('AHORA DEBES PROBAR EN DIRERENTES PAGINAS TU CC' ,nume2,'Y SIQUIERES QUE TE FUNCIONE DEBES EXTRAPOLAR, ALGUNAS SON \nMULTIFUNCIONALES Y PUES ALGUNAS PUEDEN JALAR EN COMPRAS, ALGUNAS \nPUEDEN ESTAR QUEMADAS O MUERTAS, SOLO DEBES PROBAR UNA POR UNA Y \nTENER PACIENCIA \nSI NO TE FUNCIONA CON ESE PAIS PUEDES PROBAR CON ESTADOS UNIDOS\n')
        time.sleep(2)

    elif bi == '3':
        os.system ("clear")
        time.sleep(1)
        print("$ BUSCANDO TARGETAS DE CREDITO CON INJECCION RH",it)
        time.sleep(10)
        os.system ("clear")
        print(morado)
        print(space)
        print('TARGETA DE CREDITO:',amex)
        print('CID :',cid)
        print('FECHA :',data1gen(),sp,data2gen())
        print('IP :' ,data3)
        print('CPF DE LA TARGETA :',cpf)
        print(by)
        print(space)
        print('AHORA DEBES PROBAR EN DIRERENTES PAGINAS TU CC' ,nume3,'Y /nSIQUIERES QUE TE FUNCIONE DEBES EXTRAPOLAR, ALGUNAS SON \nMULTIFUNCIONALES Y PUES ALGUNAS PUEDEN JALAR EN COMPRAS, ALGUNAS \nPUEDEN ESTAR QUEMADAS O MUERTAS, SOLO DEBES PROBAR UNA POR UNA Y \nTENER PACIENCIA \nSI NO TE FUNCIONA CON ESE PAIS PUEDES PROBAR CON ESTADOS UNIDOS\n')
        time.sleep(2)

    elif bi == '4':
        os.system ("clear")
        time.sleep(1)
        print("$ BUSCANDO TARGETAS DE CREDITO CON INJECCION RH",it)
        time.sleep(10)
        os.system ("clear")
        print(amarillo)
        print(space)
        print('TARGETA DE CREDITO:',disc)
        print('CCV :',cvv)
        print('FECHA :',data1gen(),sp,data2gen())
        print('IP :' ,data3)
        print('CPF DE LA TARGETA :',cpf)
        print(by)
        print(space)
        print('AHORA DEBES PROBAR EN DIRERENTES PAGINAS TU CC' ,nume4,'Y \nSIQUIERES QUE TE FUNCIONE DEBES EXTRAPOLAR, ALGUNAS SON \nMULTIFUNCIONALES Y PUES ALGUNAS PUEDEN JALAR EN COMPRAS, ALGUNAS \nPUEDEN ESTAR QUEMADAS O MUERTAS, SOLO DEBES PROBAR UNA POR UNA Y \nTENER PACIENCIA \nSI NO TE FUNCIONA CON ESE PAIS PUEDES PROBAR CON ESTADOS UNIDOS\n')
        time.sleep(2)

    elif bi == '5':
        os.system ("clear")
        time.sleep(1)
        print(rojo)
        os.system ("toilet 'BINS_GEN'")
        print(verde,space)
        bin_format = str(input('DIGITE SU BIN DE 16 DIGITOS  #: '))
        can = int(input("CANTIDAD A GENERAR  #: "))
        print(rojo,"\n\n|| CREDIT CARD  || CVV ||MES|| AÑO ||| CHECKER |||")
        print(amarillo)
        for i in range(can):
            time.sleep(0.5)
            print(ccgen(bin_format),sp,ccvgen(),sp,data1gen(),sp,data2gen(),sp,">",checker())
        print(verde, by)
        print(celeste, "\n SE GENERO CON EXITO TU BIN" ,bin_format, "Y SI NO VES LIVES EN TU BIN,\nINTENTA GENERAR MAS TARGETAS")
        print(verde, space)
        time.sleep(2)

    elif bi == '6':
        os.system ("clear")
        time.sleep(2)
        print(amarillo)
        os.system ("toilet ' CC_LIVE'")
        print(rojo,"————————————————————————————————————————————————————————————————")
        print(celeste)
        bin1 = str(input("PONGA SU PRIMERA CC : "))
        bin2 = str(input("PONGA SU SEGUNDA CC : "))
        print(azul,space)
        time.sleep(2)
        print(rojo, "                   ∆ EXTRAPOLACION BASICA ∆",amarillo)
        print(genbasico())
        time.sleep(2)
        print(rojo,"\n                   ∆ EXTRAPOLACION MEDIA ∆",amarillo)
        print(genmedio())
        time.sleep(2)
        print(rojo,"\n                   ∆ EXTRAPOLACION AVANZADA ∆",amarillo)
        print(genavanzado())
        print(morado,"\nESTA EXTRAPOLACION AVANZADA SE SACO DE LA BASE DE DATOS DEL BANCO")
        print(azul, space)
        print(verde,"      > EXTRAPOLACION COMPLETADA.....\n\n")
        time.sleep(2)

    elif bi == '7':
        os.system ("clear")
        print(amarillo)
        os.system ("toilet 'RHSociety'")
        print(plomo)
        print("[•]DESARROLLADO POR \033[32;1m@REALHACKRH593 (Telegram)\033[30;1m \n[•]PROHIBIDO LA VENTA DE LA HERRAMIENTA\n[•]UNETE A: \033[32;1m@MundoNetRH (Telegram)\033[30;1m PARA MAS!.\n[•]SIEMPRE AGRADECE POR LO QUE HACEMOS.\n[•]EL CONOCIMIENTO NO TIENE FIN\n[•]ESTA HERRAMIENTA TE AYUDA A CONSEGUIR TARGETAS DE CREDITOS Y GENERACION DE BINS\n[•]AYUDAME CON UNA DONACION A MI CUENTA PAYPAL\n[•]SIEMPRE AGRADECE POR LO QUE HACEMOS.\n[•]EL CONOCIMIENTO ES GRATIS Y HACI QUE COMPARTELO\n[•]LA MEJOR APK DE CARDING \n",verde,"[•]https://apkpure.com/u/2822488/post/4729661 \n  [•]http://www.appcreator24.com/app729139 \n\n",rojo,"[•]MI CANAL DE YOUTUBE\n",morado,"https://m.youtube.com/channel/UCgQQLnIEodkiZIXb8hNcjqg \033[30;01m\n[•]NOS VEMOS",nic,"AGRADECE A REALHACKRH POR LA SCRIPT GRATIS\n")
        sys.exit()
        break

    else:
        os.system ("clear")
        print(rojo)
        print("OPCION INCORRECTA \nPOR FAVOR DIJITA DE NUEVO AMIG@")
        time.sleep(2)
        os.system ("clear")