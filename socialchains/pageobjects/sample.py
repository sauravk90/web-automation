## add objects in below format

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.xpathLink = "//a[text()='%s']"
        self.xpathBottomFrame = "//frame[@name='frame-bottom']"

    def verify_tex(self):
        #self.driver.blablabla
        pass