from app import app
from flask.templating import render_template
from forms import LoginForm
from flask import flash

left_panel= {
             'Post Trade':{
                           'Failures':{'url':'failures','icon':'glyphicon glyphicon-envelope'},
                           'Incidents':{'url':'failures','icon':'glyphicon glyphicon-cog'},
                          'Closed':{'url':'failures','icon':'glyphicon glyphicon-comment'},
                          'Pending':{'url':'failures','icon':'glyphicon glyphicon-user'},
                          'Downgraded':{'url':'failures','icon':'glyphicon glyphicon-flag'}
                          },
             'Pre Trade':{
                           'Failures':{'url':'failures','icon':'glyphicon glyphicon-envelope'},
                           'Overrides':{'url':'failures','icon':'glyphicon glyphicon-cog'},
                          'Closed':{'url':'failures','icon':'glyphicon glyphicon-comment'},
                          'OnHold':{'url':'failures','icon':'glyphicon glyphicon-user'},
                          'Downgraded':{'url':'failures','icon':'glyphicon glyphicon-flag'}
                          }
             }

@app.route('/index')
def index():
    header = ['one'] * 10
    data = [['empty'] * 10 for i in range(50)]
    return render_template("bootply.html", title = 'Home', header=header, data=data)

@app.route('/')
def etsForm():
    return render_template("index.html", title = 'ETS', left_panel=left_panel)

   
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenId="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
    return render_template('login.html', title='Sign In', form=form)

class dfedit(object):
    def __init__(self, df):
        self.df = df
    def filter(self):
        pass
    