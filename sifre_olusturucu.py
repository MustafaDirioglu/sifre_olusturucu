import random


secme = []
liste = []
passaword = []
a=0

print("Merhaba Şifre Üreticiye hoş geldiniz")

while True:
    a+=1
    if a==8:
        break
    alfabe = "abcdefghijklmnoprstuvyz"

    for harf in alfabe:
        liste += harf

    for i in range(14):
        liste+=str(i)

    bul=len(liste)
    secme = list(range(bul))
    secme = random.choice(secme)
    secme = liste[secme]
    passaword += secme

for i in passaword:
    print(i,end="")
input()