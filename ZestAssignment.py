class AmazonSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver= Chrome('F:\Softwares\Python\Lib\site-packages\selenium\Chrome\chromedriver.exe'
    def  amazonsearch(self):
        self.driver.get("https://www.amazon.com")
        self.driver.maximize_window()
        a=self.ActionChains(driver)
        e=self.driver.find_element_by_xpath(".//*[@id='nav-link-accountList']")
        self.a.move_to_element(e).perform();
        self.driver.find_element_by_class_name("nav-action-button").click()
        self.driver.find_element_by_id("ap_email").send_keys("samalshudi@gmail.com")
        self.driver.find_element_by_id("ap_password").send_keys("shudi12345")
        self.driver.find_element_by_id("signInSubmit").click()
        ee= self.driver.find_element_by_id("twotabsearchtextbox")
        self.a.move_to_element(ee).perform()
        self.ee.send_keys("iPhone XR (64GB) - Yellow")
        de=self.driver.find_element_by_class_name("nav-input")
        self.de.click()
        phone=self.driver.find_element_by_partial_link_text("Apple-iPhone-XR-64GB-Yellow")
        self.phone.click()
        price=self.driver.find_element_by_id("priceblock_ourprice").gettext()
    def  flipkartsearch(self):
        self.driver.get("https://www.flipkart.com/")
        self.driver.maximize_window()
        self.driver.find_element_by_class_name("_2zrpKA _1dBPDZ").send_keys("7978646176")# Username
        self.driver.find_element_by_class_name("_39M2dM JB4AMj").send_keys("shudi12345") # Password
        self.driver.find_element_by_class_name("_2AkmmA _1LctnI _7UHT_c").click()
        searchbox= self.driver.find_element_by_name("q")
        self.a.move_to_element(searchbox).perform()
        self.searchbox.send_keys("iPhone XR (64GB) - Yellow")
        search=self.driver.find_element_by_class_name("_2BhAHa")
        self.search.click()
        phonesearch=self.driver.find_element_by_class_name("_3wU53n")
        self.phonesearch.click()
        pricess=self.driver.find_element_by_class_name("_1vC4OE _2rQ-NK").gettext()
    if price<pricess:
        print("The price in Amazon is less than Flipkart")
        print("price")
    else:
        print("Price in Flipkart is less than Amazon ")
        print("pricess")
@classmethod
def tearDownClass(cls):
    cls.driver.close()
cls.driver.close()
if __name__='__main__':
    unittest.main(HtmlTestRunner(Output="F:\Softwares\Python\Python\venv\Task\Reporting.html")
