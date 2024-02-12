from sys import argv
import os 

listefichiers = []
listeDossiers = []    

def affiche(chemin):
   for p in os.listdir(chemin): 
    print(p)

if __name__ == "__main__":
    if len(sys.agrv[1])!= 2:
        print("mauvais nombre d'argument ")

    else:
        if not os.path.exists(sys.argv[1]):
            print(f"chemin fourni {sys.argv[1]}")

        else:
            affiche(sys.argv[1])
            recherche(sys.argv[1])        


            
def affiche():
     for i in os.listdir(argv[1]):
          print(i)


def main():
     try:
          if len(argv) == 1:
               print("aucune argument n'a ete passé en parametre")

          elif os.path.exists(argv[1]) == False:
               print("le dossier n'eiste pas")
          else:
               affiche()
     except Exception as e:
          print("une erreur est survenue ", e )




if __name__ == "__main__":
    main()
     