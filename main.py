from fbchat import Client
from fbchat.models import *
import json
import time

def main(user):
    session_cookies = ''
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    try:
        with open('./session/session_{}.json'.format(user)) as f:
            session_cookies = json.load(f)
    except Exception as e:
        print(e)
    finally:
        pass
    if session_cookies:
        client = Client("user", "password", user_agent=user_agent, session_cookies=session_cookies)
        #send message:
        while True:
            time.sleep(300)
            client.send(Message(text='get activate'), thread_id='100038437520170', thread_type=ThreadType.USER)
    else:
        print('not found cookies, please insert them')
if __name__ == '__main__':
    print('server hoat dong nhe')
    user = 'voccer37'
    main(user)


