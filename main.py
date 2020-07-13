import json

from bot import VoccerBot


def main():
    # Load session đăng nhập từ trước nếu co
    session_cookies = ''
    try:
        with open('session_0392571400.json') as f:
            session_cookies = json.load(f)
    except Exception as e:
        print(e)
    finally:
        pass

    client = VoccerBot("user", "password", session_cookies=session_cookies)
    # Lắng nghe phản hồi từ messager
    client.listen()
 
if __name__ == '__main__':
    print('server hoat dong nhe')
    main()



