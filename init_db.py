import os
import psycopg2

def init_dba():
    conn = psycopg2.connect(
            host="database",
            database="postgres",
            user="postgres",
            password="admin")
            
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS public.films;')
    cur.execute('CREATE TABLE public.films (id serial PRIMARY KEY,'
                                            'name varchar (50) NOT NULL,'
                                            'time varchar (50) NOT NULL);'
                                            )
                                            
    cur.execute('DROP TABLE IF EXISTS public.inf;')
    cur.execute('CREATE TABLE public.inf (id serial PRIMARY KEY,'
                                            'name varchar (80) NOT NULL,'
                                            'time varchar (90) NOT NULL,'
                                            'place varchar (80) NOT NULL);'
                                            )
                                            
    cur.execute('INSERT INTO public.films (name, time) VALUES (%s, %s)',
                ('все или ничего',
                '2 часа 1 минута')
                )
    cur.execute('INSERT INTO public.films (name, time) VALUES (%s, %s)',
                ('большой вопрос',
                '1 час 45 минут')
                )
    cur.execute('INSERT INTO public.films (name, time) VALUES (%s, %s)',
                ('трио',
                '3 часа 55 минут')
                )       
    cur.execute('INSERT INTO public.inf (name, time, place) VALUES (%s, %s, %s)',
                ('все или ничего',
                '14:20',
                '1 ряд, 5 место')
                )
    cur.execute('INSERT INTO public.inf (name, time, place) VALUES (%s, %s, %s)',
                ('трио',
                '11:00',
                '7 ряд, 7 место')
                )
    cur.execute('INSERT INTO public.inf (name, time, place) VALUES (%s, %s, %s)',
                ('трио',
                '11:00',
                '7 ряд, 6 место')
                )

    conn.commit()
    cur.close()
    conn.close()
init_dba()
