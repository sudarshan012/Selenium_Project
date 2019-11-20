from selenium import webdriver
import time
import unittest
from Modules_Test.POM_Demo.Pages.LoginPage import LoginPage
from Modules_Test.POM_Demo.Pages.HomePage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="D:\Daily updates\Sample_Modules\Modules\Selenium\Drivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

        login=LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("test Completed")


if __name__=='__main__':
    unittest.main()

# driver.find_element_by_link_text("logout").click()
