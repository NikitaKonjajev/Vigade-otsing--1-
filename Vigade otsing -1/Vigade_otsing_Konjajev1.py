from math import * #rikutud sõnade järjekorda

print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #Panin kehvad kükid ja kirjutasin input
S=a**2
print("Ruudu pindala", round (S,1))
P=4*a
print("Ruudu ümbermõõt", round (P)) #parandas sepiseid
di=a*sqrt(2) #kirjutasin sqrt
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #oli üleliigne sulg
b=float(input("Sisesta ristküliku 1. külje pikkus => "))
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print("Ristküliku pindala", round(S,1)) #parandas sepiseid ja kirjutasin round
P=2*(b+c) #kirjutasin *
print("Ristküliku ümbermõõt", round(P,1))
di=sqrt(b*2+c*2) #kustutas sõna
print("Ristküliku diagonaal", round(di,1)) #kirjutasin di,1
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #oli üleliigne klamber ja ei ole õige tärnid 
d=2*r #Korrutamine
print("Ringi läbimõõt",  round (d,1)) # muutis sõnade järjestust
S=pi*r**2 #kustutas 
print("Ringi pindala", round(S,2))
C=2*pi*r #pani sepised
print("Ringjoone pikkus", round(C,2)) #Sulg ei olnud suletud
