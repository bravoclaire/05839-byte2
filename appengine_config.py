<<<<<<< HEAD
"""
`appengine_config.py` is automatically loaded when Google App Engine
starts a new instance of your application. This runs before any
WSGI applications specified in app.yaml are loaded.
"""

from google.appengine.ext import vendor

# Third-party libraries are stored in "lib", vendoring will make
# sure that they are importable by the application.
=======
"""`appengine_config` gets loaded when starting a new application instance."""
import vendor
# insert `lib` as a site directory so our `main` module can load
# third-party libraries, and override built-ins with newer
# versions.
>>>>>>> 2c062edc8dd53b019a957e9fd3cf44e87c16123a
vendor.add('lib')
