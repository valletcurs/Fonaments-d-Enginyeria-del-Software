###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
ubicacio_encaminador = "Sala de Servidors"
nom_encaminador = "Router1"
num_ports = 8
esta_ences = True
f_string = f"L'encaminador {nom_encaminador} està ubicat a {ubicacio_encaminador}, té {num_ports} ports i està encès: {esta_ences}."
print(f_string)

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
gb_inclosos = 10
gb_consumits = 4
gb_restants = gb_inclosos - gb_consumits
print(f"GB restants: {gb_restants}")

gb_consumits = 6
gb_restants = gb_inclosos - gb_consumits
print(f"GB restants després de l'actualització: {gb_restants}")