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


import copy
import lxml.etree as etree
from io import StringIO

# Функция, которая преобразует дочерние элементы узла в строку
def stringify_children(node):
    # Если тег узла - script или style, возвращаем пустой список
    if str(node.tag).lower() in {'script', 'style'}:
        return []
    
    # Создаем список, состоящий из текста узла
    parts = [node.text]
    # Добавляем в список текст дочерних элементов
    for element in node.getchildren():
        parts += stringify_children(element)
    # Возвращаем объединенный список, преобразованный в строку, в нижнем регистре
    return ''.join(filter(None, parts)).lower()

# Функция, которая преобразует HTML в дерево элементов
def get_tree(html):
    # Создаем парсер HTML
    parser = etree.HTMLParser()
    # Преобразуем HTML в дерево и возвращаем корневой элемент
    tree = etree.parse(StringIO(html), parser)
    return tree.getroot()

# Функция, которая удаляет теги из HTML
def remove_tags(html):
    # Получаем дерево элементов из HTML
    tree = get_tree(html)
    # Возвращаем текст, удаляя теги
    return stringify_children(tree)

# Функция, которая преобразует документ в текст
def get_text(doc):
    try:
        # Создаем копию документа
        res = copy.deepcopy(doc)
        # Удаляем теги из HTML и сохраняем результат в тексте
        res['res'] = remove_tags(res['text'])
        # Возвращаем результат
        return res
    except:
        return doc
