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

# Начальный URL для краулинга
START_URL = 'http://www.vsu.ru/'

# Домены, которые разрешено сканировать
ALLOWED_DOMAINS = {'vsu.ru'}

# Таймаут для запросов
TIMEOUT = 1.0

# Максимальное количество попыток повторного подключения
MAX_RETRY = 3

# путь к папке хранения сырых файлов
import os

currPath = os.path.dirname(os.path.realpath(__file__))
FOLDER = '/'.join(currPath.split('/')[:-1]) + '/assets'