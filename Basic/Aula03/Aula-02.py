
animal = str(input("Digite, vertebrado ou invertebrado: ").lower())
   

    
if (animal == "vertebrado"):
            animal= str(input("Ave ou mamifero: ").lower)
            if (animal =="ave"):
                animal = str(input("Carnivoro ou onivoro: ").lower())
                
                if(animal == "carnivoro"):
                    print("Aguia")
                else:
                    print("Pomba")
            else:
                animal = str(input("Onivoro ou Herbivoro: ").lower())
                
                if (animal == "onivoro"):
                    print("Homem")
                else:
                    print("Vaca!")
                
            
else:
            animal= str(input("Inseto ou Anelideo: ").lower)
            
            if (animal =="Inseto"):
                animal = str(input("Hematofago ou Herbivoro: ").lower())
                
                if(animal == "Hematofago"):
                    print("Pulga")
                else:
                    print("Lagarta")
            else:
                animal = str(input("Onivoro ou Hematofago: ").lower())
                
                if (animal == "onivoro"):
                    print("Minhoca")
                else:
                    print("Sanguessuga!")
    