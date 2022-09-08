#CONSTANTS

import inspect

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"

def whoami():
    return inspect.stack()[1][3]