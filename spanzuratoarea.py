import random
import string
from words import words


def selectare_cuvant(words):
    """Selects a random word from the list of words.

  Args:
    words: A list of words.

  Returns:
    A random word.
  """
    cuvant_ales = random.choice(words)
    while '-' in cuvant_ales or ' ' in cuvant_ales:
        cuvant_ales = random.choice(words)
    return cuvant_ales


def hangman():
      """Plays the game of hangman.

  Args:
    words: A list of words.

  
  """
      cuvant_gasit=selectare_cuvant(words)
      literele_cuvantului=set(cuvant_gasit)
      alfabet=set(string.ascii_uppercase)
      litere_deja_folosite=set()
      vieti=5

      while len(cuvant_gasit)>0 and vieti>0:
        print(f'Mai ai {vieti} vieti si ai folosit deja literele: ', ' '.join(litere_deja_folosite))
        lista_cuvantului=[litera if litera in litere_deja_folosite else '-' for litera in cuvant_gasit]
        print('Cuvantul actual este: ',' '.join(lista_cuvantului))
        
           

        litera_jucatorului=input("Incearca sa ghicesti o litera: ").upper()
        if litera_jucatorului in alfabet-litere_deja_folosite:
            litere_deja_folosite.add(litera_jucatorului)
            if litera_jucatorului in literele_cuvantului:
                    literele_cuvantului.remove(litera_jucatorului)
            else:
                 vieti=vieti-1
                 print("Ai gresit!")        
        elif litera_jucatorului in litere_deja_folosite:
            
            print('AI FOLOSIT DEJA LITERA ASTA!!')
        else:  
            print('AI INTRODUS UN CARACTER INVALID!!')    
            
        if vieti==0:
           print(f"Ai pierdut, cuvantul era {cuvant_gasit}")
        else:
            print(f"Ai ghicit cuvantul {cuvant_gasit}!")     


hangman()
