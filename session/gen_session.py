import json


user = '0335168790'
with open('./session_cookies_{}.json'.format(user), 'r') as f:
    session = json.load(f)

session_str = ''

for s in session:
    if s == session[0]:
        session_str += '{'
    session_str += '"' + s['name'] + '":'
    session_str += '"' + s['value'] + '"'
    if s == session[-1]:
        session_str += '}'
    else:
        session_str += ','
print(session_str)

with open('session_{}.json'.format(user), 'w') as f:
    f.write(session_str)