from app import app
from flask import render_template
from datetime import datetime
@app.route('/', methods=['GET'])
@app.route('/index')
def index ():
    now=datetime.now()
    cur_time=now.strftime('сегодня %D : %T')
    string = '''
    <html>
    <head>
    <title>Maspanova</title>
    </head>
    <body>
    <h1>Вы зашли на сайт дата, время:</h1> 
    ''' + cur_time + '''
    </body>
    </html>
    '''
 
    return string
#now=datetime.now()
#cur_time=now.strftime('%D:%T')