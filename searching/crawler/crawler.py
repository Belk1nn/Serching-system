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
import variables as var
from additionally import color
import requests
import json
from hashlib import sha256
import time

from queue import Queue

from lxml.html import etree
from lxml.etree import XMLSyntaxError

from urllib.parse import urljoin, urlparse

# Возвращает текст из ответа HTTP
def get_html(http_response):
    return(http_response.text)

# Получает ответ HTTP, повторяя запрос при необходимости
def get_response(url):
    for i in range(var.MAX_RETRY):
        try:
            return requests.get(url, timeout=var.TIMEOUT)
        except Exception as ex:
            print(f'{color.RED}[Error]:{color.WHITE} Cannot crawl url {url} by reason {ex}. retry in 1 sec')
            time.sleep(1)
    return requests.Response()

# Получает HTML-код страницы по URL
def get(url):
    http_response = get_response(url)
    html = get_html(http_response)
    return html

# Сохраняет HTML в файл в формате JSON
def save_html(url, html, folder):
    urlhash = sha256(url.encode()).hexdigest()
    data = json.dumps({'url': url, 'text': html, 'res': None, 'tokens': None, 'stemmed':None})
    f = open(f'{folder}{urlhash}.json', 'w')
    f.write(data)
    f.close()

# Возвращает все ссылки из HTML-кода
def get_links(html):
    parser = etree.HTMLParser()
    try:
        tree = etree.fromstring(html, parser=parser)
    except XMLSyntaxError as ex:
        return []
    if tree is None:
        return []
    links = tree.xpath('//a/@href')
    return set(links)

# Нормализует все ссылки относительно текущего URL
def normalize_links(current_url, links):
    result = [normalize_link(current_url, link) for link in links]
    return result

# Нормализует отдельную ссылку относительно текущего URL
def normalize_link(current_url, link):
    url_with_tail = urljoin(current_url, link)
    normalized = remove_tail(url_with_tail)
    return normalized

# Удаляет параметры запроса из URL
def remove_tail(url):
    parsed = urlparse(url)
    # scheme://netloc/path;parameters?query#fragment
    result = parsed.scheme + '://' + parsed.netloc + parsed.path
    return result

# Проверяет, разрешен ли домен для сканирования
def link_domain_disallowed(url):
    parsed = urlparse(url)
    return parsed.netloc not in var.ALLOWED_DOMAINS

# Проверяет, является ли URL ссылкой на файл для скачивания
def is_file(url):
    file_suffixes = ['.png', '.jpg', 'jpeg', '.gif', 
    			'.pdf', '.doc', '.txt', '.docx', 
    			'.zip', '.rar', '.7zip', '.ppt', 
    			'.pptx', '.exe', '.xls', '.xlsx', 
    			'.mp3', '.mp4', '.wav', '.rtf', 
    			'.7z', '.msi', '.pkg', '.deb', 
    			'.apk', '.rpm', '.bin', '.webp', 
    			'.flac', '.alac', '.eps', '.svg', 
    			'.ai', '.webm', '.mov', '.wmv', 
    			'.avi', '.mkw', '.flv', 'f4v', 
    			'.swf', '.dot', '.dotx', '.xml', 
    			'.json', '.js', '.yaml', '.yml']
    for suffix in file_suffixes:
        if url.endswith(suffix):
            return False
    return True

# Применяет фильтры к  ссылкам
def get_filtered_links(url, html):
    links = get_links(html)
    normalized_urls = set(normalize_links(url, links))
    links_in_domain = list(filter(link_domain_disallowed, normalized_urls))
    links_without_files = list(filter(is_file, links_in_domain))
    return links_without_files

# Обходим граф сайта в ширину
def bfs(start_url, folder):
    queue = Queue()
    queue.put(start_url)
    seen_links = {start_url} 
    
    while not (queue.empty()): 
        try:   
            url = queue.get()
            print(f'{color.GREEN}[Processing url]:{color.WHITE} {url}')
            html = get(url)
            save_html(url, html, folder)
            for link in get_filtered_links(url, html):
                
                    if link not in seen_links:
                        queue.put(link)
                        seen_links.add(link)
        except:
            print(f'{color.RED}[Error link]:{color.WHITE} {queue.get()}')
            continue

