from ..ExplanationPage.PageHolder import PageHolder
from .BasicExplainPages import B_Pages
from ..consoleColors import bcolors as ccolors

from os import system, name

class BasicExplanation:

    def __init__(self):
        self.Pages = PageHolder()
        self.Pages.addPages(*B_Pages)
        
        self.pageSize = len(self.Pages.PageList)
        self.currentPage = 0
        self.run = True

        self.description = f"""\n
{ccolors.OKBLUE}1-){ccolors.ENDC}Sonraki sayfa
{ccolors.OKBLUE}2-){ccolors.ENDC}Önceki sayfa
{ccolors.OKBLUE}3-){ccolors.ENDC}Açıklamadan çık
{ccolors.OKBLUE}4-){ccolors.ENDC}Son sayfaya git (Tam kod)
{ccolors.OKBLUE}5-){ccolors.ENDC}İlk sayfaya git\n"""

    def clearConsole(self):
        system('cls' if name == 'nt' else 'clear')

    def seePage(self):
        print(self.Pages.PageList[self.currentPage].getPage(), f"\n{ccolors.OKCYAN}{'/'*84}", self.description) #Prints the current page and ends with "/" symbols

    def nextPage(self):
        if self.currentPage < len(self.Pages.PageList) - 1:
            self.currentPage += 1
            self.seePage()

    def previousPage(self):
        if self.currentPage > 0:
            self.currentPage -= 1
            self.seePage()

    def startExplanation(self):
        self.clearConsole()
        self.seePage()
        
        while self.run:
            pageChoice = int(input("Seçeneğinizi girin: "))
            
            if pageChoice == 1:
                if self.currentPage == self.pageSize - 1:
                    self.clearConsole()
                    self.seePage()
                    print(f"{ccolors.FAIL}Sonraki sayfayı açamazsın, zaten son sayfadasın!{ccolors.ENDC}")
                else:
                    self.clearConsole()
                    self.currentPage += 1
                    self.seePage()            
            
            elif pageChoice == 2:
                if self.currentPage == 0:
                    self.clearConsole()
                    self.seePage()
                    print(f"{ccolors.FAIL}Önceki sayfaya dönemezsin, zaten ilk sayfadasın!{ccolors.ENDC}")
                else:
                    self.clearConsole()
                    self.currentPage -= 1
                    self.seePage()
            
            elif pageChoice == 3:
                self.clearConsole()
                self.run = False

            elif pageChoice == 4:
                if self.currentPage == self.pageSize - 1:
                    self.clearConsole()
                    self.seePage()
                    print(f"{ccolors.FAIL}Zaten son sayfadasın!{ccolors.ENDC}")
                else:
                    self.clearConsole()
                    self.currentPage = self.pageSize - 1
                    self.seePage()

            elif pageChoice ==5:
                if self.currentPage == 0:
                    self.clearConsole()
                    self.seePage()
                    print(f"{ccolors.FAIL}Zaten ilk sayfadasın!{ccolors.ENDC}")
                else:
                    self.currentPage = 0
                    self.clearConsole()
                    self.seePage()
            else:
                self.clearConsole()
                self.seePage()
                print(f"{ccolors.FAIL}Üstteki seçeneklere uygun bir sayı girmedin!{ccolors.ENDC}")
                