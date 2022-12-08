#  This file conatins constants and import common utilised lib across project  


#  constants
api_request_url = "https://api.github.com/"
webdriver_path = 'input/chromedriver.exe'

# external libs
import requests
import os
import sys
import time

from os import path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from scripts.common_util.api_operation import *
from scripts.common_util.ui_helper.browser_helper import *
