from selenium import webdriver
from sauceclient import SauceClient
import unittest
import sys


class VistaPrintTests(unittest.TestCase):

    def setUp(self):
        # Check if sauce credentials are available during runtime
        self.credentials_index = [i for i, arguments in enumerate(sys.argv) if '-cred' in arguments]
        if len(self.credentials_index) > 0:
            sauce_username = sys.argv[self.credentials_index[0]].split('=')[1].split(':')[0]
            sauce_access_key = sys.argv[self.credentials_index[0]].split('=')[1].split(':')[1]
            sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
            self.driver = webdriver.Remote(
                    desired_capabilities={'platform': 'Windows 8', 'browserName': 'chrome', 'name': 'vistaprint_login'},
                 command_executor=sauce_url % (sauce_username, sauce_access_key)
            )
            self.driver.implicitly_wait(30)
            self.sauce = SauceClient(sauce_username, sauce_access_key)
        else: # default to firefox
            self.driver = webdriver.Firefox()

    def test_login(self):
        self.driver.get('http://vistaprint.com')
        # Click on Login link on Corp page
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/nav/div/header[2]/div[3]/div[1]/a/span[2]/span[1]').click()
        # Login
        self.driver.find_element_by_id('txtEmail').clear()
        self.driver.find_element_by_id('txtEmail').send_keys('test@sajnikanth.com')
        self.driver.find_element_by_id('txtSignInPassword').clear()
        self.driver.find_element_by_id('txtSignInPassword').send_keys('ten20304050')
        self.driver.find_element_by_name('btnSignIn').click()
        # Assert welcome message
        assert self.driver.find_element_by_xpath('//*[@id="divPageInner"]/div[1]/header[2]/div[3]/div[1]/a/span[2]/span[2]').is_displayed()

    def tearDown(self):
        try:
            if len(self.credentials_index) > 0:
                if sys.exc_info() == (None, None, None):
                    self.sauce.jobs.update_job(self.driver.session_id, passed=True)
                else:
                    self.sauce.jobs.update_job(self.driver.session_id, passed=False)
            else:
                pass # do nothing
        finally:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
