import json
from bot import VoccerBot
import datetime
from lunarcalendar import Converter, Solar, Lunar
from datetime import datetime  
import pytz  

IST = pytz.timezone('Asia/Ho_Chi_Minh')  


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
        client = VoccerBot("user", "password", user_agent=user_agent, session_cookies=session_cookies)
        user = client.searchForUsers('tra', limit=5)
        for i in user:
            if i.is_friend:
                print(i)
    # Lắng nghe phản hồi từ messager
        # client.listen()
    else:
        print('not found cookies, please insert them')
if __name__ == '__main__':
    print('server hoat dong nhe')
    user = 'nduc'
    main(user)
    


