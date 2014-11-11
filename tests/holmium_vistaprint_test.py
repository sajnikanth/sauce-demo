import unittest
import pages
import utilities


class VistaPrintTests(unittest.TestCase):

    def test_login(self):
        # instantiate corp page object and click on login link
        corp_site = pages.corp.CorpMain(self.driver, self.config['url'])
        corp_site.login_link.click()

        # instantiate login page object and login (function defined in pages/login.py)
        login_page = pages.login.LoginMain(self.driver)
        login_page.do_login(self.config['username'], self.config['password'])

        # instantiate home page object and assert if you see a logout link
        home_page = pages.home.HomeMain(self.driver)
        assert home_page.welcome_message.is_displayed()
        utilities.update_result_on_sauce_dashboard(self)

if __name__ == "__main__":
    unittest.main()
