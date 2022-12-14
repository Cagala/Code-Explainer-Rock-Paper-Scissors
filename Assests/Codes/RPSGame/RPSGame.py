from random import choice
from os import system, name

from ...Codes import bcolors as ccolors

class Game():

    def __init__(self) -> None:
        self.gameRun = True
        self.choicesList = ("taş", "kağıt", "makas")

        self.userPoint = 0
        self.computerPoint = 0
        self.winNumber = None

        self.winCombinations = {"kağıt":"taş", "makas":"taş", "taş":"makas"}

    def clearConsole(self):
        system('cls' if name == 'nt' else 'clear')

    def startGame(self):
        self.clearConsole() #If you don't clear console, colorful words don't work in windows
        
        numberChoiceRun = True
        while numberChoiceRun:
            try:
                self.winNumber = int(input("Kaçıncı skorda kazanılsın: "))
                numberChoiceRun = False
                self.clearConsole()
                
            except:
                self.clearConsole()
                print(f"{ccolors.FAIL}Sayı girmedin!{ccolors.ENDC}")
                
        while self.gameRun:
            computerChoice = choice(self.choicesList)
            userChoice = input("Seçiminizi yapın (Taş, Kağıt, Makas): ").lower()

            if userChoice not in self.choicesList:
                self.clearConsole()
                print(f"{ccolors.FAIL}Seçiminiz hatalı! Lütfen tekrar seçin yapın. {ccolors.OKCYAN}(Önceki seçiminiz: {userChoice}){ccolors.ENDC}\n")
            else:
                self.clearConsole()
                print(f"\n{ccolors.OKBLUE}{'Bilgisayarın Seçimi':<20}:{computerChoice.capitalize():^10}{ccolors.ENDC}\n{ccolors.OKGREEN}{'Oyuncu Seçimi':<20}:{userChoice.capitalize():^10}{ccolors.ENDC}")
                
                if userChoice == computerChoice:
                    print(f"\n{ccolors.BG_GREY}{'Berabere!':^30}{ccolors.ENDBG}\n{'Bilgisayar Puanı  |  Oyuncu Puanı':^30}\n{f'{self.computerPoint}  |  {self.userPoint}':^38}")
                
                elif self.winCombinations[userChoice] == computerChoice: #If userChoice's win statement equals to computerChoice / userChoice = Paper, userChoice's win statement = Rock
                    self.userPoint += 1
                    print(f"\n{ccolors.BG_GREEN}{'Oyuncu kazandı!':^30}{ccolors.ENDBG}\n{'Bilgisayar Puanı  |  Oyuncu Puanı':^30}\n{f'{self.computerPoint}  |  {self.userPoint}':^38}")
                else:
                    self.computerPoint += 1
                    print(f"\n{ccolors.BG_RED}{'Bilgisayar kazandı!':^30}{ccolors.ENDBG}\n{'Bilgisayar Puanı  |  Oyuncu Puanı':^30}\n{f'{self.computerPoint}  |  {self.userPoint}':^38}")

                if self.userPoint == self.winNumber:
                    print(f"\n{ccolors.BG_GREEN}Kaybettin!{ccolors.ENDBG}")
                    endChoiceRun = True
                    while endChoiceRun:
                        try:
                            endChoice = int(input("Tekrar oynamak istiyor musun? [1-)Tekrar oyna 2-)Oyundan çık]: "))
                        
                            if endChoice == 1:
                                endChoiceRun = False                                    
                                Game().startGame()
                            elif endChoice == 2:
                                endChoiceRun = False
                                self.gameRun = None
                                self.clearConsole()
                            else:
                                pass
                        except:
                            pass

                elif self.computerPoint == self.winNumber:
                    print(f"\n{ccolors.BG_RED}Kaybettin!{ccolors.ENDBG}")
                    endChoiceRun = True
                    while endChoiceRun:
                        try:
                            endChoice = int(input("Tekrar oynamak istiyor musun? [1-)Tekrar oyna 2-)Oyundan çık]: "))
                        
                            if endChoice == 1:
                                endChoiceRun = False                                    
                                Game().startGame()
                            elif endChoice == 2:
                                endChoiceRun = False
                                self.gameRun = None
                                self.clearConsole()
                            else:
                                pass
                        except:
                            pass