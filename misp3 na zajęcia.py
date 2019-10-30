#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pulp import *
import pandas as pd
import numpy as np

pracownicy = ['Igor', 'Marcin', 'Franek', 'Pioter', 'Ania', 'Zenek']
godz_pracy = [4, 4, 3, 8, 10, 5]
stawka_godz = [170, 60, 80, 200, 90, 70]

dzien_tyg = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota']
godz_bib = [8, 4, 4, 4, 8, 2]

i=0
j=0
war_1=0
war_2=0
war=0
warDzien=0
warImie=0

pracownik_dzien=[['IgorPoniedziałek', 'IgorWtorek', 'IgorŚroda', 'IgorCzwartek', 'IgorPiątek', 'IgorSobota'], ['MarcinPoniedziałek', 'MarcinWtorek', 'MarcinŚroda', 'MarcinCzwartek', 'MarcinPiątek', 'MarcinSobota'], ['FranekPoniedziałek', 'FranekWtorek', 'FranekŚroda', 'FranekCzwartek', 'FranekPiątek', 'FranekSobota'], ['PioterPoniedziałek', 'PioterWtorek', 'PioterŚroda', 'PioterCzwartek', 'PioterPiątek', 'PioterSobota'], ['AniaPoniedziałek', 'AniaWtorek', 'AniaŚroda', 'AniaCzwartek', 'AniaPiątek', 'AniaSobota'], ['ZenekPoniedziałek', 'ZenekWtorek', 'ZenekŚroda', 'ZenekCzwartek', 'ZenekPiątek', 'ZenekSobota']]
pracownik_dzien2=[['IgorPoniedziałek', 'IgorWtorek', 'IgorŚroda', 'IgorCzwartek', 'IgorPiątek', 'IgorSobota'], ['MarcinPoniedziałek', 'MarcinWtorek', 'MarcinŚroda', 'MarcinCzwartek', 'MarcinPiątek', 'MarcinSobota'], ['FranekPoniedziałek', 'FranekWtorek', 'FranekŚroda', 'FranekCzwartek', 'FranekPiątek', 'FranekSobota'], ['PioterPoniedziałek', 'PioterWtorek', 'PioterŚroda', 'PioterCzwartek', 'PioterPiątek', 'PioterSobota'], ['AniaPoniedziałek', 'AniaWtorek', 'AniaŚroda', 'AniaCzwartek', 'AniaPiątek', 'AniaSobota'], ['ZenekPoniedziałek', 'ZenekWtorek', 'ZenekŚroda', 'ZenekCzwartek', 'ZenekPiątek', 'ZenekSobota']]


# In[2]:


godziny = LpProblem('Najtańszy koszt pracowników biblioteki', LpMinimize)
IgorPoniedziałek = pulp.LpVariable('IgorPoniedziałek', lowBound=0, upBound=4, cat='Continous')
IgorWtorek = pulp.LpVariable('IgorWtorek', lowBound=0, upBound=4, cat='Continous')
IgorŚroda = pulp.LpVariable('IgorŚroda', lowBound=0, upBound=4, cat='Continous')
IgorCzwartek = pulp.LpVariable('IgorCzwartek', lowBound=0, upBound=4, cat='Continous')
IgorPiątek = pulp.LpVariable('IgorPiątek', lowBound=0, upBound=4, cat='Continous')
IgorSobota = pulp.LpVariable('IgorSobota', lowBound=0, upBound=4, cat='Continous')
MarcinPoniedziałek = pulp.LpVariable('MarcinPoniedziałek', lowBound=0, upBound=4, cat='Continous')
MarcinWtorek = pulp.LpVariable('MarcinWtorek', lowBound=0, upBound=4, cat='Continous')
MarcinŚroda = pulp.LpVariable('MarcinŚroda', lowBound=0, upBound=4, cat='Continous')
MarcinCzwartek = pulp.LpVariable('MarcinCzwartek', lowBound=0, upBound=4, cat='Continous')
MarcinPiątek = pulp.LpVariable('MarcinPiątek', lowBound=0, upBound=4, cat='Continous')
MarcinSobota = pulp.LpVariable('MarcinSobota', lowBound=0, upBound=4, cat='Continous')
FranekPoniedziałek = pulp.LpVariable('FranekPoniedziałek', lowBound=0, upBound=3, cat='Continous')
FranekWtorek = pulp.LpVariable('FranekWtorek', lowBound=0, upBound=3, cat='Continous')
FranekŚroda = pulp.LpVariable('FranekŚroda', lowBound=0, upBound=3, cat='Continous')
FranekCzwartek = pulp.LpVariable('FranekCzwartek', lowBound=0, upBound=3, cat='Continous')
FranekPiątek = pulp.LpVariable('FranekPiątek', lowBound=0, upBound=3, cat='Continous')
FranekSobota = pulp.LpVariable('FranekSobota', lowBound=0, upBound=3, cat='Continous')
PioterPoniedziałek = pulp.LpVariable('PioterPoniedziałek', lowBound=0, upBound=8, cat='Continous')
PioterWtorek = pulp.LpVariable('PioterWtorek', lowBound=0, upBound=8, cat='Continous')
PioterŚroda = pulp.LpVariable('PioterŚroda', lowBound=0, upBound=8, cat='Continous')
PioterCzwartek = pulp.LpVariable('PioterCzwartek', lowBound=0, upBound=8, cat='Continous')
PioterPiątek = pulp.LpVariable('PioterPiątek', lowBound=0, upBound=8, cat='Continous')
PioterSobota = pulp.LpVariable('PioterSobota', lowBound=0, upBound=8, cat='Continous')
AniaPoniedziałek = pulp.LpVariable('AniaPoniedziałek', lowBound=0, upBound=10, cat='Continous')
AniaWtorek = pulp.LpVariable('AniaWtorek', lowBound=0, upBound=10, cat='Continous')
AniaŚroda = pulp.LpVariable('AniaŚroda', lowBound=0, upBound=10, cat='Continous')
AniaCzwartek = pulp.LpVariable('AniaCzwartek', lowBound=0, upBound=10, cat='Continous')
AniaPiątek = pulp.LpVariable('AniaPiątek', lowBound=0, upBound=10, cat='Continous')
AniaSobota = pulp.LpVariable('AniaSobota', lowBound=0, upBound=10, cat='Continous')
ZenekPoniedziałek = pulp.LpVariable('ZenekPoniedziałek', lowBound=0, upBound=5, cat='Continous')
ZenekWtorek = pulp.LpVariable('ZenekWtorek', lowBound=0, upBound=5, cat='Continous')
ZenekŚroda = pulp.LpVariable('ZenekŚroda', lowBound=0, upBound=5, cat='Continous')
ZenekCzwartek = pulp.LpVariable('ZenekCzwartek', lowBound=0, upBound=5, cat='Continous')
ZenekPiątek = pulp.LpVariable('ZenekPiątek', lowBound=0, upBound=5, cat='Continous')
ZenekSobota = pulp.LpVariable('ZenekSobota', lowBound=0, upBound=5, cat='Continous')
IgorPoniedziałek = pulp.LpVariable('IgorPoniedziałek', lowBound=0, upBound=4, cat='Continous')
MarcinPoniedziałek = pulp.LpVariable('MarcinPoniedziałek', lowBound=0, upBound=4, cat='Continous')
FranekPoniedziałek = pulp.LpVariable('FranekPoniedziałek', lowBound=0, upBound=3, cat='Continous')
PioterPoniedziałek = pulp.LpVariable('PioterPoniedziałek', lowBound=0, upBound=8, cat='Continous')
AniaPoniedziałek = pulp.LpVariable('AniaPoniedziałek', lowBound=0, upBound=10, cat='Continous')
ZenekPoniedziałek = pulp.LpVariable('ZenekPoniedziałek', lowBound=0, upBound=5, cat='Continous')
IgorWtorek = pulp.LpVariable('IgorWtorek', lowBound=0, upBound=4, cat='Continous')
MarcinWtorek = pulp.LpVariable('MarcinWtorek', lowBound=0, upBound=4, cat='Continous')
FranekWtorek = pulp.LpVariable('FranekWtorek', lowBound=0, upBound=3, cat='Continous')
PioterWtorek = pulp.LpVariable('PioterWtorek', lowBound=0, upBound=8, cat='Continous')
AniaWtorek = pulp.LpVariable('AniaWtorek', lowBound=0, upBound=10, cat='Continous')
ZenekWtorek = pulp.LpVariable('ZenekWtorek', lowBound=0, upBound=5, cat='Continous')
IgorŚroda = pulp.LpVariable('IgorŚroda', lowBound=0, upBound=4, cat='Continous')
MarcinŚroda = pulp.LpVariable('MarcinŚroda', lowBound=0, upBound=4, cat='Continous')
FranekŚroda = pulp.LpVariable('FranekŚroda', lowBound=0, upBound=3, cat='Continous')
PioterŚroda = pulp.LpVariable('PioterŚroda', lowBound=0, upBound=8, cat='Continous')
AniaŚroda = pulp.LpVariable('AniaŚroda', lowBound=0, upBound=10, cat='Continous')
ZenekŚroda = pulp.LpVariable('ZenekŚroda', lowBound=0, upBound=5, cat='Continous')
IgorCzwartek = pulp.LpVariable('IgorCzwartek', lowBound=0, upBound=4, cat='Continous')
MarcinCzwartek = pulp.LpVariable('MarcinCzwartek', lowBound=0, upBound=4, cat='Continous')
FranekCzwartek = pulp.LpVariable('FranekCzwartek', lowBound=0, upBound=3, cat='Continous')
PioterCzwartek = pulp.LpVariable('PioterCzwartek', lowBound=0, upBound=8, cat='Continous')
AniaCzwartek = pulp.LpVariable('AniaCzwartek', lowBound=0, upBound=10, cat='Continous')
ZenekCzwartek = pulp.LpVariable('ZenekCzwartek', lowBound=0, upBound=5, cat='Continous')
IgorPiątek = pulp.LpVariable('IgorPiątek', lowBound=0, upBound=4, cat='Continous')
MarcinPiątek = pulp.LpVariable('MarcinPiątek', lowBound=0, upBound=4, cat='Continous')
FranekPiątek = pulp.LpVariable('FranekPiątek', lowBound=0, upBound=3, cat='Continous')
PioterPiątek = pulp.LpVariable('PioterPiątek', lowBound=0, upBound=8, cat='Continous')
AniaPiątek = pulp.LpVariable('AniaPiątek', lowBound=0, upBound=10, cat='Continous')
ZenekPiątek = pulp.LpVariable('ZenekPiątek', lowBound=0, upBound=5, cat='Continous')
IgorSobota = pulp.LpVariable('IgorSobota', lowBound=0, upBound=4, cat='Continous')
MarcinSobota = pulp.LpVariable('MarcinSobota', lowBound=0, upBound=4, cat='Continous')
FranekSobota = pulp.LpVariable('FranekSobota', lowBound=0, upBound=3, cat='Continous')
PioterSobota = pulp.LpVariable('PioterSobota', lowBound=0, upBound=8, cat='Continous')
AniaSobota = pulp.LpVariable('AniaSobota', lowBound=0, upBound=10, cat='Continous')
ZenekSobota = pulp.LpVariable('ZenekSobota', lowBound=0, upBound=5, cat='Continous')

godziny += 90*AniaCzwartek + 90*AniaPiątek + 90*AniaPoniedziałek + 90*AniaSobota + 90*AniaWtorek + 90*AniaŚroda + 80*FranekCzwartek + 80*FranekPiątek + 80*FranekPoniedziałek + 80*FranekSobota + 80*FranekWtorek + 80*FranekŚroda + 170*IgorCzwartek + 170*IgorPiątek + 170*IgorPoniedziałek + 170*IgorSobota + 170*IgorWtorek + 170*IgorŚroda + 60*MarcinCzwartek + 60*MarcinPiątek + 60*MarcinPoniedziałek + 60*MarcinSobota + 60*MarcinWtorek + 60*MarcinŚroda + 200*PioterCzwartek + 200*PioterPiątek + 200*PioterPoniedziałek + 200*PioterSobota + 200*PioterWtorek + 200*PioterŚroda + 70*ZenekCzwartek + 70*ZenekPiątek + 70*ZenekPoniedziałek + 70*ZenekSobota + 70*ZenekWtorek + 70*ZenekŚroda
godziny += AniaCzwartek + AniaPiątek + AniaPoniedziałek + AniaSobota + AniaWtorek + AniaŚroda + FranekCzwartek + FranekPiątek + FranekPoniedziałek + FranekSobota + FranekWtorek + FranekŚroda + IgorCzwartek + IgorPiątek + IgorPoniedziałek + IgorSobota + IgorWtorek + IgorŚroda + MarcinCzwartek + MarcinPiątek + MarcinPoniedziałek + MarcinSobota + MarcinWtorek + MarcinŚroda + PioterCzwartek + PioterPiątek + PioterPoniedziałek + PioterSobota + PioterWtorek + PioterŚroda + ZenekCzwartek + ZenekPiątek + ZenekPoniedziałek + ZenekSobota + ZenekWtorek + ZenekŚroda == 30
godziny += IgorCzwartek + IgorPiątek + IgorPoniedziałek + IgorSobota + IgorWtorek + IgorŚroda <= 4
godziny += AniaPoniedziałek + FranekPoniedziałek + IgorPoniedziałek + MarcinPoniedziałek + PioterPoniedziałek + ZenekPoniedziałek <= 8
godziny += MarcinCzwartek + MarcinPiątek + MarcinPoniedziałek + MarcinSobota + MarcinWtorek + MarcinŚroda <= 4
godziny += AniaWtorek + FranekWtorek + IgorWtorek + MarcinWtorek + PioterWtorek + ZenekWtorek <= 4
godziny += FranekCzwartek + FranekPiątek + FranekPoniedziałek + FranekSobota + FranekWtorek + FranekŚroda <= 3
godziny += AniaŚroda + FranekŚroda + IgorŚroda + MarcinŚroda + PioterŚroda + ZenekŚroda <= 4
godziny += PioterCzwartek + PioterPiątek + PioterPoniedziałek + PioterSobota + PioterWtorek + PioterŚroda <= 8
godziny += AniaCzwartek + FranekCzwartek + IgorCzwartek + MarcinCzwartek + PioterCzwartek + ZenekCzwartek <= 4
godziny += AniaCzwartek + AniaPiątek + AniaPoniedziałek + AniaSobota + AniaWtorek + AniaŚroda <= 10
godziny += AniaPiątek + FranekPiątek + IgorPiątek + MarcinPiątek + PioterPiątek + ZenekPiątek <= 8
godziny += ZenekCzwartek + ZenekPiątek + ZenekPoniedziałek + ZenekSobota + ZenekWtorek + ZenekŚroda <= 5
godziny += AniaSobota + FranekSobota + IgorSobota + MarcinSobota + PioterSobota + ZenekSobota <= 2
godziny.solve()


tablicaM=[]
tablicaT=[]
tablicaW=[]
tablicaTu=[]
tablicaF=[]
tablicaSa=[]

print("-------Schedule-------")
for variable in godziny.variables():
    #print ("{} = {}".format(variable.name,variable.varValue))
    wartosc=variable.varValue
    imie=variable.name
    
    if(imie.count("Poniedziałek")== 1):
        tablicaM.append(wartosc)
    elif(imie.count("Wtorek")== 1 and imie.startswith("Czwartek")== 0):
        tablicaT.append(wartosc)        
    elif(imie.count("Środa")== 1):
        tablicaW.append(wartosc)        
    elif(imie.count("Czwartek")== 1):
        tablicaTu.append(wartosc)
    elif(imie.count("Piątek")== 1):
        tablicaF.append(wartosc)        
    elif(imie.count("Sobota")== 1):
        tablicaSa.append(wartosc)

        
print()


print("           Ania Franus Igor Pioter Marcin Zuzia\nPoniedzieli: {} \nWtorek:      {}".format(tablicaM,tablicaT))
print("Środa:       {}\nCzwartek:    {}\nPiątek:      {}\nSobota:      {}".format(tablicaW,tablicaTu,tablicaF,tablicaSa))


# In[ ]:




