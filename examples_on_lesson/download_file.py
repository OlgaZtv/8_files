import os.path

import requests

r = requests.get('https://selenium.dev/images/selenium_logo_square_green.png')

f = open('../resources/selenium.png', 'wb')
f.write(r.content)
f.close()

print(os.path.getsize('../resources/selenium.png'))