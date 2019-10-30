#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pulp import *
import pandas as pd
import numpy as np


# In[2]:


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

pracownik_dzien = ['0']*len(pracownicy)
for x in range(len(pracownik_dzien)):
    pracownik_dzien[x]=['0']*len(dzien_tyg)

pracownik_dzien2 = ['0']*len(pracownicy)
for x in range(len(pracownik_dzien2)):
    pracownik_dzien2[x]=['0']*len(dzien_tyg)

while i<len(pracownicy):
    while j<len(dzien_tyg):
        pracownik_dzien[i][j] = str(pracownicy[i])+str("_")+str(dzien_tyg[j])
        pracownik_dzien2[i][j] = str(pracownicy[i])+str("_")+str(dzien_tyg[j])
        j=j+1
    j=0
    i=i+1
i=0

war_3=[['0']]*len(pracownicy)
war_4=[['0']]*len(dzien_tyg)

# def nowy_pracownik(imie, czas, stawka):
#     return pracownicy.append(imie), godz_pracy.append(czas), stawka_godz.append(stawka)


# In[3]:


godziny = LpProblem('Najtańszy koszt pracowników biblioteki', LpMinimize)
 
while i<len(pracownicy):
    while j<len(dzien_tyg):
        pracownik_dzien[i][j] = pulp.LpVariable(pracownik_dzien[i][j], lowBound=0, upBound=godz_pracy[i], cat='Continous')
        print("%s = pulp.LpVariable('%s', lowBound=0, upBound=%d, cat='Continous')" % (pracownik_dzien2[i][j], pracownik_dzien2[i][j], godz_pracy[i]))
        warImie=warImie+pracownik_dzien[i][j] #poniedziałekIgor+wtorekIgor+
        j=j+1
    war_3[i]=warImie #[[suma Igora], [suma Marcina], ...]
    j=0
    i=i+1
    warImie=0
i=0
#print(war_3)
    
while j<len(dzien_tyg):
    while i<len(pracownicy):
        pracownik_dzien2[i][j] = pulp.LpVariable(pracownik_dzien2[i][j], lowBound=0, upBound=godz_pracy[i], cat='Continous')
        print("%s = pulp.LpVariable('%s', lowBound=0, upBound=%d, cat='Continous')" % (pracownik_dzien2[i][j], pracownik_dzien2[i][j], godz_pracy[i]))
        warDzien=warDzien+pracownik_dzien2[i][j]
        i=i+1
    war_4[j]=warDzien #[[suma poniedziałków], [suma wtorków], ...]
    i=0
    j=j+1
    warDzien=0
j=0
#print(war_4)

print("")
    
while i<len(pracownicy):
    war_1 += war_3[i]*stawka_godz[i]
    war_2 += war_3[i]
    i=i+1
i=0
godziny += war_1
print("godziny += %s" % war_1)
godziny += war_2 == 30
print("godziny += %s == 30" % war_2)

while i<len(godz_pracy):
    godziny += war_3[i] <= godz_pracy[i]
    print("godziny += %s <= %s" % (war_3[i], godz_pracy[i]))
    godziny += war_4[i] <= godz_bib[i]
    print("godziny += %s <= %s" % (war_4[i], godz_bib[i]))
    i=i+1
i=0
    
godziny.solve()
    
for variable in godziny.variables():
    print("{} = {}".format(variable.name, variable.varValue))
        
# print("")
# print("Aby dopisać nowego pracownika, wpisz: nowy_pracownik('imie', maksymalny czas pracy, stawka za 1 godzine pracy)")
# print("Na przykład: nowy_pracownik('Jasio', 3, 45)")

