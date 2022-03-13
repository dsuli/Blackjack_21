global juega_banca
juega_banca=0
global juega_jugador1
juega_jugador1=True
global mazo
mazo=[]
global apuesta
apuesta=10
global apuesta_seguro
apuesta_seguro=0
global cant_mazos
global seguimos_jugando
seguimos_jugando = True
contador=0

cartas_banca=[]
cartas_jugador=[]
valores={"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}

import random

class Jugador():
    def __init__(self,nombre,fichas,apuesta,apuesta_seguro=0,cartas_recibidas=[]):
        self.nombre=nombre
        self.fichas=fichas
        self.apuesta=apuesta
        self.apuesta_seguro=apuesta_seguro
        self.cartas_recibidas=cartas_recibidas
    
    def __str__(self):
        return (f"El Jugador {self.nombre} ahora tiene {self.fichas} fichas")

def inicio():
    global jugador
    print("")
    print("bienvenido al juego de Blackjack")
    # la variable "jugador" formara parte del objeto "mi_jugador" de la clase "Jugador"
    # y por lo tanto sera global
    jugador=(input("Como te llamas? ")).capitalize()

    while 1:
            reglas=input("Sabes las reglas? (Si/No)")
            if reglas.lower()=="si":
                print(f"Perfecto! juguemos {jugador}")
                break
            elif reglas.lower()=="no":
                print("Estas son las reglas: bla bla bla")
                break
            else:
                print("solo puedes ingresar Si/No")

def fichas_iniciales():
    global fichas
    # la cantidad de fichas con las que inicia el juego seran una variable globla
    # y formara parte del objeto "mi_jugador" de la clase "Jugador"
    # ademas en ella impactaran las ganacias y perdidas
    while 1:
        try:
            fichas=float(input("Ingresa cuantas fichas quieres cambiar: "))
            if 10000>=fichas>=500:
                print(f"Perfecto, tendras inicialmente {fichas}")
                return fichas
                break
            elif fichas<500:
                print("Elige un numero mas alta RATA DE ALCANTARILLA ")
            else:
                print("Quien sos? Ricardo Fort???")
        except:
            print("ingresa un numero entero por favor")

def apuestas_iniciales():
    global apuesta
    # la cantidad apostada en cada turno sera ingresada y sera una variable global
    # "apuesta" debe estar en un rango y simultaneamento no mayor a la cantdad de "fichas"
    # al momento de hacer la apuesta
    while 1:
        try:
            apuesta=float(input("Ingresa la apuesta: "))
            if apuesta<fichas:
                if (100)>=apuesta>=(5):
                    print(f"Perfecto, las apuestas seran de {apuesta}")
                    return apuesta
                elif apuesta<(5):
                    print("Elige una apuesta minima mas alta que 5 RATA DE ALCANTARILLA ")
                else:
                    print("Quien sos? Ricardo Fort???")
            else:
                print(f"No tenes tantas fichas para apostar, te quedan: {fichas}")
        except:
            print("ingresa un numero entero por favor que no sea mayo a 100 ni menor a 5")

def cantidad_de_mazos():
    global cant_mazos
    while 1:
        try:
            cant_mazos=int(input("Ingresa con cuantos mazos quieres jugar: "))
            if 6>=cant_mazos>=1:
                print(f"Perfecto, jugaremos con {cant_mazos} mazos")
                return cant_mazos
                break
            elif cant_mazos<1:
                print("Elige un numero mas alto CHICO LISTO ")
            else:
                print("Estas seguro que entendes el juego?")
        except:
            print("ingresa un numero entero por favor")

def crear_mazo():
    mazo.clear()
    for k in range(cant_mazos):
        for j in ["Co","Pi","Tr","Di"]:
            for i in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
                mazo.append((i,j))

def mezclar_si_pocas_cartas():
    if len(mazo) < 0.25*52*cant_mazos:
        crear_mazo()
        print("Se ha mezclado")
    else:
        pass

def quiere_seguro():
    global apuesta_seguro
    #en caso que la carta visible sea 1
    if cartas_banca[0][0] == "A":
        apuesta_seguro=0
        while 1:
            quiere_seguro=(input("Quiere tomar un seguro contra Blackjack que paga 2 a 1)? (Si/No)")).lower()
            if quiere_seguro=="si":
                print(f"Perfecto, usted ha apostado {apuesta*0.5} a que la banca tiene Blackjack")
                apuesta_seguro=apuesta*0.5
                break
            elif quiere_seguro=="no":
                print("Si la banca saca Blackjack y usted no, entonces pierde automaticamente")
                print("Si la banca saca Blackjack y usted tambien, entonces es empate")
                break
            else:
                print("Ingrese Si o No")
    else:
        pass

def resultado_seguro():
    global juega_jugador1
    global apuesta_seguro
    global fichas
    global apuesta
    #Esta funcion determina si has tomado el seguro
    #y que sucedio con esa apuesta
    # ademas, si la banca saco blackjack salda cuentas y termina la mano 
    if apuesta_seguro>0:
        if cartas_banca[1][0]=="10" or cartas_banca[1][0]=="J" or cartas_banca[1][0]=="Q" or cartas_banca[1][0]=="K":
            if sumador(cartas_jugador)==21:
                print(f"Empate y ganas por haber tomado el seguro ${apuesta_seguro*2}")
                fichas=fichas+apuesta_seguro*2
                juega_jugador1=False
            elif sumador(cartas_jugador)<21:
                print(f"Has perdido la apuesta inicial ${apuesta} pero ganado por haber tomado el seguro ${apuesta_seguro*2}")
                print(f"Has perdido ${apuesta_seguro*2-apuesta}")
                fichas=fichas+apuesta_seguro*2-apuesta
                juega_jugador1=False
        else:
            print(f"La banca no tiene Blackjack por lo que has perdido tu apuesta de ${apuesta_seguro}")
            fichas=fichas-apuesta_seguro
            juega_jugador1=True
            print("El juego continua")
    else:
        pass

def sumador(lista_de_cartas):
    global juega_jugador1
    global fichas

    suma=0

    for i in range(len(lista_de_cartas)):
        suma+=valores.get(lista_de_cartas[i][0])
    hay_as=0
    for i,j in lista_de_cartas:
        if i=="A":
            hay_as+=1
    if (hay_as>0) and (suma<12):
        suma+=10
    if suma>21:
        fichas=fichas-apuesta
        juega_jugador1=False

    return suma

def sumador_banca(lista_de_cartas):

    suma=0

    for i in range(len(lista_de_cartas)):
        suma+=valores.get(lista_de_cartas[i][0])
    hay_as=0
    for i,j in lista_de_cartas:
        if i=="A":
            hay_as+=1
    if (hay_as>0) and (suma<12):
        suma+=10
    if suma>21:
        pass

    return suma

def impresora_inicial_cancelada():
    #Esta funcion imprime la primera mano
    print(mazo[-1])
    cartas_banca.append(mazo.pop())
    print("( ? , ? )")
    cartas_banca.append(mazo.pop())
    print(mazo[-1])
    cartas_jugador.append(mazo.pop())
    print(mazo[-1])
    cartas_jugador.append(mazo.pop())
    print(f"Las cartas del jugador suman {sumador(cartas_jugador)}")

def impresora_inicial():
    #Esta funcion limpia la pantalla y despues imprime las cartas iniciales de la banca (una oculta)
    #  y las cartas acumuladas del jugador con su correspondiente subtotal
    #y lo mas importante es que suma una carta
    print("\n" *100)
    print(cartas_banca[0])
    print("( ? ) , ( ? )")
    print("")
    cartas_jugador.append(mazo.pop())
    print(cartas_jugador)
    print(f"               {sumador(cartas_jugador)}")
    return

def impresora_turno_jugador():
    global juega_jugador1
    global juega_banca
    global apuesta
    apuestas_iniciales()
    impresora_inicial_cancelada()
    quiere_seguro()
    resultado_seguro()
    


    while juega_jugador1 == True:
        var=(input("Ingrese su jugada: \n Quedarse (Q) \n Ultima carta doblando la apuesta (U) \n Otra carta (O): ")).lower()
        if var=="q":
            print(f"Perfecto, tu cartas suman {sumador(cartas_jugador)}")
            juega_banca+=1
            juega_jugador1=False
        elif var=="u":
            apuesta=apuesta*2
            print(f"Has duplicado tu apuesta a {apuesta}")
            impresora_inicial()
            juega_banca+=1
            juega_jugador1=False
        elif var=="o":
            impresora_inicial()

def volver_a_jugar():
    global seguimos_jugando
    while seguimos_jugando == True:
        var=input("Ingrese su ENTER para seguir jugando ")
        if var=="":
            break
        else:
            seguimos_jugando = False

def jugada_banca():
    global fichas
    if juega_banca>0:
        #si hace falta que la Banca juegue se activa el codigo
        #imprime la situacion actual
        print("La banca tiene: ")
        print(cartas_banca)
        print(f"Las cartas de la Banca suman {sumador_banca(cartas_banca)}")
        print("El jugador tiene: ")
        print(cartas_jugador)
        print(f"Las cartas del jugador suman {sumador_banca(cartas_jugador)}")
        if sumador_banca(cartas_banca)==21:
            #chequeo si la banca tiene Blackjack
            print("La Banca tiene Blackjack")
            if sumador_banca(cartas_jugador)==21 and len(cartas_jugador)==2:
                #chequeo si el jugador tiene Blackjack
                print("Y tu tambien tienes Blackjack!")
                print("Han empatado")
                return
            else:
                #si el jugador no tiene blackjack
                print("Gana la Banca")
                fichas=fichas-apuesta
                print(f"Ahora tiene ${fichas} en fichas")
                return
        else:
            pass
        if sumador_banca(cartas_jugador)==21 and len(cartas_jugador)==2:
            #chequeo si el jugador tiene Blackjack
            print("Tienes Blackjack!")
            print(f"Has ganado {apuesta*1.5}")
            fichas=fichas+apuesta*1.5
            print(f"Ahora tiene ${fichas} en fichas")
            return
        while 1:
    #De aca en adelante se que ninguno de los 2 tiene blackjack
            if sumador_banca(cartas_banca)<17:
                #si la Banca tiene que pedir
                cartas_banca.append(mazo.pop())
                print(cartas_banca)
                print(f"Las cartas de la Banca suman {sumador_banca(cartas_banca)}")
            elif 21>=sumador_banca(cartas_banca)>=17:
                #si la Banca se tiene que plantar
                print("La banca ha sacado:")
                print(cartas_banca)
                print(f"Las cartas de la Banca suman {sumador_banca(cartas_banca)}")
                print("La Banca se planta")
                print("El jugador ha sacado:")
                print(cartas_jugador)
                print(f"Las cartas del jugador suman {sumador_banca(cartas_jugador)}")
                if sumador_banca(cartas_jugador)==sumador_banca(cartas_banca):
                    print("Empate")
                    return
                elif sumador_banca(cartas_jugador)<sumador_banca(cartas_banca):
                    print("Has perdido esta partida")
                    fichas=fichas-apuesta
                    print(f"Ahora tienes ${fichas} en fichas")
                    return
                else:
                #si la banca saco menos que el jugador y se tuvo que plantar
                    print("Has Ganado")
                    fichas=fichas+apuesta
                    print(f"Ahora tienes ${fichas} en fichas")
                    return
            else:
            #si la Banca hizo BUST
                print("Has Ganado")
                fichas=fichas+apuesta
                print(f"Ahora tienes ${fichas} en fichas")
                return

def acciones_jugador():
    global fichas
    global juega_jugador1
    global juega_banca
    global apuesta
    global apuesta_seguro
    apuestas_iniciales()
    impresora_inicial()
    quiere_seguro()
    resultado_seguro()
    while juega_jugador1:
        var=(input("Ingrese su jugada: \n Quedarse (Q) \n Darse por vencido (D) \n Ultima carta doblando la apuesta (U) \n Otra carta (O): ")).lower()
        if var=="d":
            print(f"Se te devolvera la mitad de tu apuesta, es decir {apuesta*0.5}")
            fichas=fichas-apuesta+apuesta*0.5
            juega_banca+=0
            juega_jugador1=False
        elif var=="q":
            print(f"Perfecto, tu cartas suman {sumador(cartas_jugador)}")
            juega_banca+=1
            juega_jugador1=False
        elif var=="u":
            apuesta=apuesta*2
            print(f"Has duplicado tu apuesta a {apuesta}")
            impresora_turno_jugador()
            break
        elif var=="o":
            impresora_turno_jugador()


if __name__=="__main__":
    inicio()
    cantidad_de_mazos()
    crear_mazo()
    fichas_iniciales()
    mi_jugador=Jugador(jugador,fichas,apuesta)
    random.shuffle(mazo)
    
    print(mi_jugador)
    while seguimos_jugando==True:
        cartas_banca=[]
        cartas_jugador=[]
        juega_banca=0
        juega_jugador1=True
        mezclar_si_pocas_cartas()
        impresora_turno_jugador()
        jugada_banca()
        mi_jugador=Jugador(jugador,fichas,apuesta)
        print(mi_jugador)
        print(fichas)
        contador+=1
        volver_a_jugar()
    if seguimos_jugando==False:
        print("Gracias, vuelva pronto")
        mi_jugador=Jugador(jugador,fichas,apuesta)
        print(f"Has jugado {contador} veces")
