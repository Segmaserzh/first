import random
denga=int(input("Skolko u vas deneg"))
while denga>0: 
  a=random.randint(1,2)
  stavka=int(input("vasha stavka"))
  vybor=int(input("vvedite 1 or 2"))
  if vybor==a:
    stavka=stavka*2
    denga=denga+stavka
    print(denga)
  else:
    denga=denga-stavka
    print(denga)
print("casino always wins")