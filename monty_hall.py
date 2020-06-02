import numpy as np
import random

strategie = 2 # 0 : garder le choix initial, 1 : changer de choix, 2 : random

nombre_iterations = 100000

succes = 0
echec  = 0

for i in range(0, nombre_iterations):
    position_boule = random.randint(0, 2) # position réelle de la boule
    choix          = random.randint(0, 2) # choix initial du joueur

    revelation          = [x for x in range(0, 3) if (x != position_boule and x != choix)][0] # La révélation du présentateur, qui ne contient ni la boule, ni le choix initial 
    positions_restantes = [x for x in range(0, 3) if x != revelation]                         # Les choix restants au joueur : toutes les positions sauf la révélation
        
    if strategie == 0:   # garder choix initial
        nouveau_choix = choix
    elif strategie == 1: # changer de choix
        nouveau_choix = [x for x in positions_restantes if x != choix][0]
    else:                # choisir aléatoirement
        nouveau_choix = random.choice(positions_restantes)

    if nouveau_choix == position_boule:
        succes += 1
    else:
        echec += 1


print("Succes : "+str(np.round((succes/(succes+echec)*100), 2))+'% ('+str(succes)+'/'+str(succes+echec)+')')
print("Echec  : "+str(np.round((echec/(succes+echec)*100), 2))+'% ('+str(echec)+'/'+str(succes+echec)+')')
            
        

        
        
        

