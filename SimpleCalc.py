import pyfiglet

ascii_banner = pyfiglet.figlet_format("Calcolatrice!!")

print(ascii_banner)
ascii_banner_exit=pyfiglet.figlet_format("Bye")




while True:
    num1=int(input("Inserisci il primo numero : > "))
    num2=int(input("Inserisci il secnd numero : > "))
   
    scelta=input("Scegli operazione da effettuare: digita : \n '1' per addizione \n '2' per sottrazione\n '3' per moltiplicazione \n '4' per divisione\n>>>")
    if scelta=="1":
       print(num1+num2)

    elif scelta=="2":
           print(num1-num2)
            
    elif scelta=="3":

        print(num1*num2)

    elif scelta=="4":
        print(num1//num2)

    else :
        while True:        
                print("Hai inserito una scelta non valida!")
                break                 


    altro_esc=(input("Digita 'Esc' per uscire o 'A' per altra operazione: > "))
    altro_esc=altro_esc.lower()
    if altro_esc=="esc":
        print(ascii_banner_exit)
        break
    elif altro_esc=="a":
        print(ascii_banner)
        continue