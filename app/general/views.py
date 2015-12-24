from app import app
from flask import render_template, Blueprint, g, request, redirect, current_app
from urlparse import urlparse

mod = Blueprint('general', __name__, url_prefix='/<lang_code>')

@app.before_request
def before_request():

    url = urlparse(request.url)

    lang_code = url.path.split('/')[1]

    supported_languages = current_app.config['LANGUAGES'].keys()

    if request.endpoint != 'static':
        if lang_code in supported_languages:
            g.lang_code = lang_code
        else:
            g.lang_code = 'pt'
            if url.query:
                new_url= "{}://{}/{}{}?{}".format(url.scheme, url.netloc, g.lang_code, url.path, url.query)
            else:
                new_url= "{}://{}/{}{}".format(url.scheme, url.netloc, g.lang_code, url.path)
            return redirect(new_url)



@mod.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)

@mod.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')

@mod.route('/')
def home():
    return render_template('general/home.html')

@mod.route('/about')
def about():
    return render_template('general/about.html')
