import calendar

#############################################################################
# Écrire le code de la fonction est_bissextile de la question 1             #
#############################################################################
def est_bissextile(annee):
    """retourne True si annee est bissextile et False sinon"""
    assert type(annee) == int
    return annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0)

#############################################################################
# Écrire le code de la fonction determiner_phase de la question 2           #
#############################################################################
def determiner_phase(j):
    """
    retourne le numero de la phase correspondant à j
    """
    assert type(j) == int and 1 <= j <= 28
    phase = {1 : range(1, 6), 2 : range(6,14), 3: range(14,15), 4: range(15,29)}
    for num, plage in phase.items():
        if j in plage:
            return num

#############################################################################
# Fonctions fournies pour la question 3                                     #
#############################################################################
def jours_dans_mois(annee, mois):
    """Renvoie le nombre de jours dans un mois donné d'une année donnée.
       Utilise le module calendar pour gérer les années bissextiles."""
    if mois == 2:  # février
        return 29 if calendar.isleap(annee) else 28
    elif mois in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30

def ajouter_jours(date, nb_jours):
    """Ajoute nb_jours à une date donnée et renvoie la nouvelle date.
       La date est représentée par un tuple (jour, mois, année)."""
    jour, mois, annee = date
    jour = jour + nb_jours

    # Ajustement du jour et du mois si dépassement
    while jour > jours_dans_mois(annee, mois):
        jour = jour - jours_dans_mois(annee, mois)
        mois = mois + 1
        if mois > 12:  # passage à l'année suivante
            mois = 1
            annee = annee + 1

    return (jour, mois, annee)

def test_ajouter_jours():
    assert ajouter_jours((7, 9, 2025), 3) == (10, 9, 2025)
    #ajout dans le même mois la même année
    assert ajouter_jours((1, 1, 2026), 30)   == (31, 1, 2026)
    #ajout la même année avec changement de mois
    assert ajouter_jours((1, 1, 2026), 31)   == (1, 2, 2026)
    #ajout sur une année non bissextile
    assert ajouter_jours((1, 2, 2026), 28)   == (1, 3, 2026)
    #ajout sur une année bissextile
    assert ajouter_jours((1, 2, 2028), 28)   == (29, 2, 2028)
    #ajout d'une année non bissextile vers année bissextile
    assert ajouter_jours((28, 2, 2027), 366) == (29, 2, 2028)
    print("bvo, les tests q3 sont passés")

#############################################################################
# Fonction fournie pour la question 4                                       #
#############################################################################
def calendrier_cycles(date_regles):
    """Renvoie une chaîne de caractère contenant au format iCalendar, l'ensemble
    des dates de début de règles qui se présentent dans les 100 jours suivants 
    `date_regles`, date incluse.

    Hypothèse : cycle régulier de 28 jours. """

    cal_lignes = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:']

    date_courante = date_regles
    jours_ecoules = 0

    # On ajoute les dates tant que l'on ne dépasse pas 100 jours écoulés
    while jours_ecoules + 28 <= 100:
        jour, mois, annee = date_courante  
        cal_lignes.append('BEGIN:VEVENT')
        cal_lignes.append('SUMMARY: Règles')
        date = str(annee)+f'{mois:02d}'+ f'{jour:02d}'
        cal_lignes.append('DTSTART:'+date)
        cal_lignes.append('END:VEVENT')
        date_courante = ajouter_jours(date_courante, 28)
        jours_ecoules += 28 

    cal_lignes.append('END:VCALENDAR')

    # La méthode join va renvoyer ici une unique chaîne contenant toutes les
    # chaînes de la liste séparées par des sauts de lignes.
    return '\n'.join(cal_lignes)

def test_calendrier_cycles():
    '''Crée un calendrier et le charge avec le module ics pour vérifier sa
    validité.

    Nécessite que le module ics soit présent sur la machine (pip install ics).
    '''
    from ics import Calendar
    c = calendrier_cycles( (12,3,2026) )
    print(c)
    cal = Calendar(c)
    print(cal.events)

#q1
assert est_bissextile(2000)
assert est_bissextile(2024)
assert not est_bissextile(2026)
assert not est_bissextile(2100)
print("bvo, les tests q1 sont passés")

#q2
assert determiner_phase(1)  == 1
assert determiner_phase(6)  == 2
assert determiner_phase(14) == 3
assert determiner_phase(20) == 4
print("bvo, les tests q2 sont passés")

#q3
test_ajouter_jours()

#q4
test_calendrier_cycles()

############### output :
# SUMMARY: Règles
# DTSTART:202649
# END:VEVENT
# BEGIN:VEVENT
# SUMMARY: Règles
# DTSTART:202657
# END:VEVENT
# END:VCALENDAR
# .........
# ValueError: month must be in 1..12

# On note une ValueError et le print() de la ligne 107 affiche deux dates
# qui ne respecte pas le format sur AAAAMMJJ car il manque des 0.
# la chaine 'date' est construite ligne 87 : date = str(annee)+str(mois)+str(jour)
# une f-string règle le problème avec le formatage :02d
# affiche des nombres entiers décimaux sur deux caractères et place un 0 devant si besoin