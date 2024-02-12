from sys import argv
import os 


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
     
