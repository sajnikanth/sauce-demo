from holmium.core import Page, Element, Locators

class HomeMain(Page):

    welcome_message = Element(Locators.XPATH, '//*[@id="divPageInner"]/div[1]/header[2]/div[3]/div[1]/a/span[2]/span[2]', timeout=1)
