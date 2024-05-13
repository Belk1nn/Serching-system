"""
*********************************************************************
*                                                                   *
*                     Welcome to Soorel                             *
*                                                                   *
*   _________  ____  ____  ________                                 *
*  / ___/ __ \/ __ \/ __ \/ ____/ /                                 *
*  \__ \ / / / / / / /_/ / __/ / /                                  *
* ___/ / /_/ / /_/ / _, _/ /___/ /___                               *
* /____/\____/\____/_/ |_/_____/_____/                              *
*                                                                   *
*                                                                   *
*  Soorel is your go-to Python-based search engine.                 *
*  We aim to provide accurate and relevant search results.          *
*  Happy Searching!                                                 *
*                                                                   *
*********************************************************************
"""

name = 'Dict'

def set_defult_base(connection):
    """Created new base that named <name> <- (param) with default par."""
    try:
        cursor = connection.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {name} (
            id INTEGER PRIMARY KEY,
            word TEXT NOT NULL,
            url TEXT NOT NULL,
            ''')
        connection.commit()
    except:
        raise IOError('Ooops. DB Error')
    
def add_new_commit(connection, data: tuple):
    """[par]: (word, url)"""
    try:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO {name} (word, url) VALUES (?, ?)',  data)
        connection.commit()
    except:
        raise IOError("Ooops. Not added...")

def get__urls(connection, data: str):
    """[par]: word"""
    try:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {name} WHERE word=?', data)
        results = cursor.fetchall()
        return results
    except:
        raise IOError("Ooops. Not working...")