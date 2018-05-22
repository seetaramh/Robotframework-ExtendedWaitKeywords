#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Extended Wait Keywords - extended keywords for Robot framework to handle AngularJS support.
#    Copyright (c) 2018 Seetaram Hegde <seetaramh@users.noreply.github.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.ui import WebDriverWait
from SeleniumLibrary.base import LibraryComponent
from time import sleep
from timeit import itertools


class ExtendedWaitKeywords(LibraryComponent):

    ROBOT_LIBRARY_VERSION = 1.0

    def __init__(self):
        pass

    # Waits until AngularJS screen is loaded. 
    # This keyword is useful when the page is built with angularJS
    # Example: Wait Until Angular Ready 60s

    def wait_until_angular_ready(self, timeout=None):
        timeout = int(self.get_timeout(timeout))
        _driver = self._get_current_driver()
        javaScriptToLoadAngular= ('var injector = window.angular.element(\'body\').injector();'
                                  'var $http = injector.get(\'$http\');'
                                  'return ($http.pendingRequests.length === 0)')  

        self._wait_for_no_exception(javaScriptToLoadAngular,timeout)
        self._wait_until_jscript_ready(timeout)
        self._wait_until_jquery_ready(timeout)
        

    # Waits until the JScript is ready
    # Example: Wait Until Jscript Ready 10s
      
    def wait_until_jscript_ready(self,timeout=None):
        self._wait_until_jscript_ready(timeout)

    # Waits until the Jquery is ready
    # Example: Wait Until Jquery Ready 10s
        
    def wait_until_jquery_ready(self,timeout=None):
        self._wait_until_jquery_ready(timeout)

    # Waits until new window is opened. This keyword comes handy when the second tab of the browser takes
    # time to open.
    # Example: Wait For New Window 10s

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
