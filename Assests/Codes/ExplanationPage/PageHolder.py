from .Page import Page

class PageHolder:

    def __init__(self):
        self.PageList : list = []

    def addPages(self, *pages:Page):
        for page in pages:
            self.PageList.append(page)