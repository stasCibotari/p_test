import requests
import json 
url = 'https://orar.usarb.md/api/getLessons'

data = {
    'gr' : '198',
    'grName' : 'IS21R',
    'day' : '2',
    'week' : '13',
    'sem' : '2'
}

session = requests.Session()
rs = session.get('http://orar.usarb.md', verify = False)
#session.headers.update({'connect.sid': json.loads(rs.content)['_csrf']})
#r = requests.post(url, data=data)

#print(rs.cookies['_csrf'])

data['_csrf'] = rs.cookies['_csrf']

session.headers.update({'Cookie': '_csrf' + rs.cookies['_csrf'] + '; connect.sid' + rs.cookies['connect.sid']})
div = session.post(url, json = data, verify = False)
print(div.content)
