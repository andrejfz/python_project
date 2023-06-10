import string,random,pyfiglet


ascii_banner = pyfiglet.figlet_format("Password Generator!!")

print(ascii_banner)
ascii_banner_exit=pyfiglet.figlet_format("Bye")
while True:
    scelta=int(input("Digita il numero di caratteri che deve avere la tua password,deve essere un numero compreso da 4 a 20 \n>: "))
    if scelta >20 or scelta <4:
       
       continue


    count=[]#numero cifre
    lista=[]#lista di tutti i caratteri
    password=[]
    for i in range(scelta):
     count.append(i)




    lista=[]
    min=(string.ascii_lowercase)

    for i in min:
    
     lista.append(i)
    
    
    max=(string.ascii_uppercase)
    for i in max:
       lista.append(i)
    num=["0","1","2","3","4","5","6","7","8","9"]
    for i in num:
      lista.append(i)
    special_char=["?","!","&","$"]
    for i in special_char:
         lista.append(i)
    for i in range(len(count)):
        i=(random.choice(lista))
        password.append(i)
    
   
    password_str=''.join(password)
    print("E' STATA GENERATA LA PASSWORD : ",password_str)
   
    scelta=input("Vuoi generare una nouva password? digita 's' per generare altra password e 'esc' per uscire :")
    scelta=scelta.lower()
    
    if scelta=="s":
       continue
       
                
    elif scelta=="esc":
        print(ascii_banner_exit)
        break
                
    else:
        print("scelta non valida ")



   


