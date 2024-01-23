import requests
from xml.etree import cElementTree

def getFeed(topic):
    url = 'https://rss.nytimes.com/services/xml/rss/nyt/'+ topic + '.xml'
    response = requests.get(url)
    parsed_xml = cElementTree.fromstring(response.content)
    items = []
    for node in parsed_xml.iter():
        if node.tag == 'item':
            item = {}
            for item_node in list(node):
                if item_node.tag == 'title':
                    item['title'] = item_node.text
                if item_node.tag == 'link':
                    item['link'] = item_node.text
            items.append(item)
    result = ''
    for item in items:
        result += '[' + item['title'] + ']' + '(' + item['link'] + ')\n\n'
    return result