import random

def wortlistgenerator():
    wortBasis='test'
    wievieleWoerter=99
    listederWoerter=[]
    for i in range(wievieleWoerter):
        anzuhaengendesWort=wortBasis+str(i)
        listederWoerter.append(anzuhaengendesWort)
    return listederWoerter
    
def woerterAuswaehlen():
    random.shuffle(wortListe)
    dieersten5=wortListe[:5]
    return dieersten5



wortListe=wortlistgenerator()
wortlistemitnur5=woerterAuswaehlen()
zufallsZahl=random.choice(range(5))
dasgesuchtePasswort=wortlistemitnur5[zufallsZahl]
versuchsBegrenzung=0
print wortListe
print wortlistemitnur5
print zufallsZahl
print dasgesuchtePasswort

print wortlistemitnur5

while True:
    startCount=0


    while True:
        userEingabe=raw_input()
        if len(userEingabe)<5 or len(userEingabe)>6:
            print "bitte erneut eingeben"
        else:
            break
    if len(userEingabe)==5 and len(dasgesuchtePasswort)==5:
        for i in range(5):
            if userEingabe[i]==dasgesuchtePasswort[i]:
                startCount+=1
    elif len(userEingabe)==5 and len(dasgesuchtePasswort)==6:
        for i in range(5):
            if userEingabe[i]==dasgesuchtePasswort[i]:
                startCount+=1
    elif len(userEingabe)==6 and len(dasgesuchtePasswort)==5:
        for i in range(5):
            if userEingabe[i]==dasgesuchtePasswort[i]:
                startCount+=1
    else:
        for i in range(6):
            if userEingabe[i]==dasgesuchtePasswort[i]:
                startCount+=1

    versuchsBegrenzung+=1


    print "Du hast"+str(startCount)+"richtig geraten"

    if startCount==6:
        break
    if versuchsBegrenzung==4:
        print "maximal Anzahl an Versuchen vorbei"+str(versuchsBegrenzung)+"vorbei"
        break
    

