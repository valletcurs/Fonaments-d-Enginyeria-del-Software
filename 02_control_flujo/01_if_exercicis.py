###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
nivellSenyal = float(input("Introdueix el nivell de senyal Wi-Fi (en dBm): "))
if nivellSenyal >= -50:
    print("La cobertura Wi-Fi és excel·lent.")
elif nivellSenyal >= -67:
    print("La cobertura Wi-Fi és bona.")
elif nivellSenyal >= -75:
    print("La cobertura Wi-Fi és feble.")
else:
    print("La cobertura Wi-Fi és molt feble.")

# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
potenciaobtica = input("Introdueix la potència òptica rebuda (en dBm): ")
potenciaobtica = float(potenciaobtica)
if potenciaobtica >= -27 and potenciaobtica <= -8:
    print("La potència òptica rebuda és acceptable.")
elif potenciaobtica < -27:
    print("La potència òptica rebuda és massa baix.")
else:
    print("La potència òptica rebuda és massa alt.")

# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
consumDades = float(input("Introdueix el consum de dades en GB: "))
if consumDades <= 20:
    print("El consum de dades està dins del límit.")
else:
    print(f"El consum de dades ha superat el límit en {consumDades - 20} GB.")

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
indicadorLOS = input("L'indicador LOS del terminal òptic està encès? (sí/no): ").strip().lower()
indicadorInternet = input("L'indicador d'Internet del router està encès? (sí/no): ").strip().lower()
if indicadorLOS == "sí":
    print("Cal revisar el cable de fibra.")
elif indicadorInternet == "sí":
    print("La connexió sembla funcionar correctament.")
else:
    print("Cal comprovar el servei del proveïdor.")

# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
percentatgeBateria = int(input("Introdueix el percentatge de bateria del SAI: "))
if percentatgeBateria < 20:
    print("El nivell de bateria és crític.")
elif percentatgeBateria < 50:
    print("El nivell de bateria és baix.")
else:
    print("El nivell de bateria és suficient.")

# Exercici 6: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.
latencia = float(input("Introdueix la latència en ms: "))
perdua = float(input("Introdueix el percentatge de paquets perduts: "))
if latencia < 0 or perdua < 0 or perdua > 100:
    print("Valors invàlids. Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.")
elif latencia <= 30 and perdua <= 1:
    print("La connexió és excel·lent.")
elif latencia <= 80 and perdua <= 3:
    print("La connexió és bona.")
elif latencia <= 150 and perdua <= 5:
    print("La connexió és acceptable.")
else:
    print("La connexió és deficient.")

# Exercici 7: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.
tipusPla = input("Introdueix el tipus de pla (bàsic/plus): ").strip().lower()
consumMensual = float(input("Introdueix el consum mensual en GB: "))
if consumMensual < 0:
    print("Consum negatiu. Rebutjat.")
elif tipusPla == "bàsic":
    if consumMensual <= 10:
        cost = 10
    else:
        cost = 10 + (consumMensual - 10) * 1.50
    print(f"El cost total del pla bàsic és de {cost:.2f} €.")
elif tipusPla == "plus":
    if consumMensual <= 30:
        cost = 20
    else:
        cost = 20 + (consumMensual - 30) * 0.75
    print(f"El cost total del pla plus és de {cost:.2f} €.")
else:
    print("Tipus de pla desconegut. Rebutjat.")

# Exercici 8: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.
compteActiu = input("El compte està actiu? (sí/no): ").strip().lower()
if compteActiu == "sí":
    contrasenyaCorrecta = input("La contrasenya és correcta? (sí/no): ").strip().lower()
    if contrasenyaCorrecta == "sí":
        codiVerificacio = input("El codi de doble verificació és correcte? (sí/no): ").strip().lower()
        if codiVerificacio == "sí":
            print("Accés permès.")
        else:
            print("Accés denegat: el codi de doble verificació és incorrecte.")
    else:
        print("Accés denegat: la contrasenya és incorrecta.")
else:
    print("Accés denegat: el compte està desactivat.")
# Exercici 9: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.
routerEncès = input("El router està encès? (sí/no): ").strip().lower()
if routerEncès == "no":
    print("Cal encendre el router.")
else:
    losEncès = input("L'indicador LOS del terminal òptic està encès? (sí/no): ").strip().lower()
    internetEncès = input("L'indicador d'Internet del router està encès? (sí/no): ").strip().lower()
    if losEncès == "sí":
        print("Cal revisar el cable de fibra.")
    elif internetEncès == "no":
        print("Cal contactar amb el proveïdor.")
    else:
        print("La connexió funciona correctament.")
# Exercici 10: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
serveiCritic = input("La incidència afecta un servei crític? (sí/no): ").strip().lower()
usuarisAfectats = int(input("Nombre d'usuaris afectats: "))
alternativaDisponible = input("Hi ha una alternativa de connexió disponible? (sí/no): ").strip().lower()
if usuarisAfectats < 0:
    print("Error: el nombre d'usuaris afectats no pot ser negatiu.")
elif serveiCritic == "sí" and alternativaDisponible == "no":
    print("Prioritat crítica.")
elif usuarisAfectats >= 50 and alternativaDisponible == "no":
    print("Prioritat crítica.")
elif usuarisAfectats >= 10 or serveiCritic == "sí":
    print("Prioritat alta.")
else:
    print("Prioritat baixa.")