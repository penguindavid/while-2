#input

h=int(input("digite el valor de h "))

#procesing

n=0
q=h/5

while h>=q:
    h=0.9*h
    n=n+1

print("el numero de rebotes es " + str (n) )