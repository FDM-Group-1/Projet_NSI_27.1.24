Liste_test = [{"joueur" : "MAM", "Jeux" : "Hand", "Score" : 1012},{"joueur" : "AAA", "Jeux" : "DDD", "Score" : 111}]

#Affichage des différents joueurs avec leurs noms, jeux et scores
def jrs_stats (dico):
    compt = 0 #Compteur pour savoir le nombre de joueur total
    print("Voici les différents joueurs avec leurs scores")
    for valeurs in dico:
        compt = compt +1
        print(f"Joueur ({compt}) : {valeurs["joueur"]}, Jeux : {valeurs["Jeux"]}, Score : {valeurs["Score"]}") 
    return f"nombre de joueurs : {compt}" #Nombre total de joueurs

print(jrs_stats(Liste_test))
