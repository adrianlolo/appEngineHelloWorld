"""A simple webapp2 server."""

from google.appengine.api import users

import webapp2
import SubPage
import MainPage

application = webapp2.WSGIApplication([
    ('/', MainPage.MainPage),
    ('/sub', SubPage.SubPage)
], debug=True)
