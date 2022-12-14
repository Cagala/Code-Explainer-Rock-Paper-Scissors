from Assests.Codes import bcolors as ccolors
from Assests.Codes.RPSGame import Game
from Assests.Codes.BasicRPS.BasicExplanation import BasicExplanation
from os import system, name

def clearConsole():
    system('cls' if name == 'nt' else 'clear')

appRun = True
def main():
    while appRun:
        print("""1-)Basit Taş-Kağıt-Makas Yapımı\n2-)Orta Seviye Taş-Kağıt-Makas Yapımı\n3-)Taş-Kağıt-Makas Oyna\n""")
        print("https://github.com/Cagala\n")
        try:
            choice = int(input("Seçeneğinizi Girin: "))
            
            if choice == 1:
                BasicExplanation().startExplanation()
            
            elif choice == 2:
                clearConsole()

            elif choice == 3:
                Game().startGame()
                clearConsole()

            else:
                clearConsole()
        except:
            clearConsole()
            print(f"{ccolors.FAIL}Sayı girmedin!{ccolors.ENDC}")
if __name__ == "__main__":
    main()