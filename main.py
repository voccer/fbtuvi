import json
import request
from bot import VoccerBot
import datetime
from lunarcalendar import Converter, Solar, Lunar

def get_birthday():
    r = requests.get('https://docs.google.com/document/u/0/export?format=txt&id=1b2aQMfZvhLhqs5bnGrdNZUnOSmCGsuNZeSH8Qk6ndrg&token=AC4w5VjlljBzAvNU8CtCSnvvFwe52p-2-w%3A1589941528767&ouid=102939292131381354747&includes_info_params=true&inspectorResult=%7B%22pc%22%3A1%2C%22lplc%22%3A20%7D')
    b = r.text

def main(user):
    session_cookies = ''
    try:
        with open('./session/session_{}.json'.format(user)) as f:
            session_cookies = json.load(f)
    except Exception as e:
        print(e)
    finally:
        pass
    
    if session_cookies:
        client = VoccerBot("user", "password", session_cookies=session_cookies)
    # Lắng nghe phản hồi từ messager
        client.listen()
    else:
        print('not found cookies, please insert them')
if __name__ == '__main__':
    print('server hoat dong nhe')
    user = '0392571400'
    main(user)


