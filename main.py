import json

from bot import VoccerBot


def main():
    # Load session đăng nhập từ trước nếu co
    session_cookies = ''
    try:
        with open('session.json') as f:
            session_cookies = json.load(f)
    except Exception as e:
        print(e)
    finally:
        pass

    client = VoccerBot("0392571400", "ducquang", session_cookies='')

    # Lấy session và lưu vào file để lần sau dùng cho đăng nhập
    session_cookies_new = client.getSession()
    with open('session.json', 'w') as outfile:
        json.dump(session_cookies_new, outfile)

    # Lắng nghe phản hồi từ messager
    client.listen()
 
if __name__ == '__main__':
    print('server hoat dong nhe')
    main()



