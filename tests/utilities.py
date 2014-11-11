import sys
from sauceclient import SauceClient


def update_result_on_sauce_dashboard(self):
    sauce_username = self.driver._holmium_config['remote'].split(':')[1].strip('//')
    sauce_password = self.driver._holmium_config['remote'].split(':')[2].split('@')[0]
    sauce = SauceClient(sauce_username, sauce_password)
    try:
        if sys.exc_info() == (None, None, None):
            sauce.jobs.update_job(self.driver.session_id, passed=True)
        else:
            sauce.jobs.update_job(self.driver.session_id, passed=False)
    finally:
        pass # do nothing
