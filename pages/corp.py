from holmium.core import Page, Element, Locators

class CorpMain(Page):

    login_link = Element(Locators.XPATH, "/html/body/div[1]/div/div/div/nav/div/header[2]/div[3]/div[1]/a/span[2]/span[1]", timeout=1)
