#abby
import os

from appium import webdriver
from selenium.webdriver.common import utils

from common.base_page import BasePage
from page.main import Main


class App(BasePage):

    '''
    管理app
    '''
    '''
    启动appp，
    '''
    def start(self):
        if self._driver is None:
            caps = {
                "platformName": "Android",
                "deviceName": "Android Emulator",
                "appPackage": "com.xfyoucai.youcai",
                "appActivity": ".activity.SplashActivity",
                "autoGrantPermissions": "true",
                "noReset": "true",
                "skipServerInstallation":"true",
                "skipDeviceInitialization": "true",
                # "newCommandTimeout":"100"
                # "printPageSourceOnFindFailure": "true"

            }

            caps['udid'] = os.getenv('udid', None)

            # forward 的端口会冲突
            caps['systemPort']=utils.free_port()
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            # setattr(Constant,'driver',self._driver)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(6)
        return self

    '''
           停止app
        '''

    # def stop(self):
    #     # driver = getattr(Constant, 'driver')
    #     #
    #     # driver.quit()

    '''
    重启app
    '''
    def restart(self):
        pass
        # driver:WebDriver = getattr(Constant, 'driver')
        #
        # driver.reset()


    '''
       进入主页,入口函数
    '''
    def main(self)->Main:

        return Main(self._driver)