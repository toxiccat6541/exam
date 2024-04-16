from flask import Flask, render_template, send_from_directory, request
import os
import psycopg2
from init_db import init_dba


app = Flask(__name__)
init_dba()
def get_db_connection():
    conn = psycopg2.connect(host='database',
                            database='postgres',
                            user="postgres",
                            password="admin")
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM public.films;')
    films = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', films=films)


@app.route('/auth', methods=['post', 'get'])
def auth():
    message =''
    if request.method == 'POST':
        id_ = request.form.get('id') 
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute('SELECT inf.id, inf.name, inf.time, inf.place, films.time FROM inf join films on inf.name = films.name where inf.id = ' + id_ + ';')
            inf = cur.fetchall()
            cur.close()
            conn.close()
            #egor
            print(int(inf[0][0]))
            print(int(id_))
            if int(inf[0][0])==int(id_):
                print('sucsess')
                return render_template('auth.html', inf=inf)
            else:
                print('unsucsess')
                return render_template('auth.html')
        except:
            message='такого пользователя нет'
            print('такого пользователя нет')
            return render_template('auth.html')
        
        
    return render_template('auth.html')
if __name__=='__main__':
    app.run(host='0.0.0.0')

# @app.route('/media/<path:filename>')
# def media(filename):
    # return send_from_directory(app.config['UPLOAD_FOLDER'], filename, mimetype='image/jpeg')
