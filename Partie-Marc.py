liAA = [{"joueur" : "MAM", "Jeux" : "Hand", "Score" : 1012},{"joueur" : "AAA", "Jeux" : "DDD", "Score" : 111}]

#Affichage des différents joueurs avec leurs noms, jeux et scores
def jrs_stats (dico):
    compt = 0 #Compteur pour savoir le nombre de joueur total
    print("Voici les différents joueurs avec leurs scores :")
    print("----------------------------------------------")
    for valeurs in dico:
        compt = compt +1
        print(f"Joueur ({compt}) : {valeurs["joueur"]},  Jeux : {valeurs["Jeux"]},  Score : {valeurs["Score"]} ") 
    print("----------------------------------------------")
    return f"nombre total de joueurs : {compt}" #Nombre total de joueurs

print(jrs_stats(liAA))
dico_participants=[{'nom':'mike','score':3.4},{'nom':'erwan','score':4.1},{'nom':'claire','score':4.8},{'nom':'camille','score':4.7},{'nom':'paul','score':1.8},{'nom':'ashley','score':3.9},{'nom':'axel','score':3.4},{'nom':'edouard','score':4.7},{'nom':'steve','score':5.0},{'nom':'sylvain','score':2.5},{'nom':'marie','score':3.2},{'nom':'phillipe','score':2.9},{'nom':'lucas','score':3.2},{'nom':'cristine','score':1.6},{'nom':'elea','score':4.1},{'nom':'jules','score':4.5},{'nom':'matteo','score':4.8},{'nom':'Elisa','score':2.0},{'nom':'Jayden','score':3.5},{'nom':'richard','score':4.7},{'nom':'pierre','score':5.0}]


