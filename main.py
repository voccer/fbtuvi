import json

from bot import VoccerBot


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



