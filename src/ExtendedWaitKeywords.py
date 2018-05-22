from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.ui import WebDriverWait
from SeleniumLibrary.base import LibraryComponent
from time import sleep
from timeit import itertools



class ExtendedWaitKeywords(LibraryComponent):

    ROBOT_LIBRARY_VERSION = 1.0

    def __init__(self):
        pass

    def wait_until_angular_ready(self, timeout=None):
        timeout = int(self.get_timeout(timeout))
        _driver = self._get_current_driver()
        javaScriptToLoadAngular= ('var injector = window.angular.element(\'body\').injector();'
                                  'var $http = injector.get(\'$http\');'
                                  'return ($http.pendingRequests.length === 0)')  

        self._wait_for_no_exception(javaScriptToLoadAngular,timeout)
        self._wait_until_jscript_ready(timeout)
        self._wait_until_jquery_ready(timeout)
        

     
    def wait_until_jscript_ready(self,timeout=None):
        self._wait_until_jscript_ready(timeout)
        
    def wait_until_jquery_ready(self,timeout=None):
        self._wait_until_jquery_ready(timeout)

    def wait_for_new_window(self, handles_before, timeout=None):
        timeout = int(self.get_timeout(timeout))
        _driver = self._get_current_driver()
        wait = WebDriverWait(_driver, timeout)
        wait.until(lambda _driver: len(handles_before) != len(_driver.window_handles))
            
    def _wait_until_jquery_ready(self, timeout=None):
        timeout = int(self.get_timeout(timeout))
        _driver = self._get_current_driver() 
        self._wait_for_no_exception("return jQuery.active==0",timeout)
                     
    def _wait_until_jscript_ready(self, timeout=None):
        timeout = int(self.get_timeout(timeout))
        _driver = self._get_current_driver() 
        self._wait_for_no_exception("return document.readyState=='complete'",timeout)
        
    def _wait_for_no_exception(self,scripttoexec,timeout=None):
        timeout = int(self.get_timeout(timeout))
        _driver = self._get_current_driver()
        wait = WebDriverWait(_driver, timeout)
        
        for _ in itertools.repeat(None, 10):
                try:
                    wait.until(lambda _driver: _driver.execute_script(scripttoexec))
                except Exception:
                    sleep(1)
                    continue
                break        
            
    def _get_current_driver(self):
        currentdriver = BuiltIn().get_library_instance('SeleniumLibrary')._current_browser() 
        return currentdriver    
