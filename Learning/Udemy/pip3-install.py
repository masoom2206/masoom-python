# You can found the build-in module and packages in below URLs
# http://pypi.org/project

# pyjokes 0.5.0
# http://pypi.org/project/pyjokes

import pyjokes

joke = pyjokes.get_joke("en", "neutral")
print(joke)

