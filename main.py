
import webapp2
import jinja2
import os
from google.appengine.api import mail


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/base.html')
        self.response.write(template.render())

    def post(self):
    	name = self.request.get('name')
        email = self.request.get('email')
        message = self.request.get('message')
        mail.send_mail(
            sender = name + ' <trevercullen@gmail.com>',
            reply_to = name + ' <' + email + '>',
            to = 'Trever Cullen <trevercullen@gmail.com>',
            subject = 'Correspondence between ' + name + ' and Trever',
            body = message)
        template = JINJA_ENVIRONMENT.get_template('templates/base.html')
        self.response.write(template.render({'message':'Message Sent!'}))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
