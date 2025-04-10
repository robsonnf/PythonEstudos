from requests import session

s = session()
x = s.get('https://www.google.com',headers={},data={})
