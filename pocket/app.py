import os 

from flask import Flask
from django.apps import apps
from django.conf import settings


from utils import configure

apps.populate(settings.INSTALLED_APPS)

from services.auth.models import User

app = Flask(__name__)

@app.route("/")
def index():
    u, c = User.objects.get_or_create(username='Mike', password='PaSsWoRd1@3')
    return f'{u.username} {c}'
    # return 'Ass'

if __name__=='__main__':
    app.run(debug=True)