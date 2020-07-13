import requests


class TuVi():
    def __init__(self):
        pass

    def con_giap(self, Cgiap=''):
        url = 'https://api.kma-chatbot.com/tuvi.php?tuoi={}'.format(Cgiap.strip())
        loi_phan = ''  # Lời phán

        try:
            r = requests.get(url)
            data_json = r.json()

            set_attributes = data_json.get('set_attributes')

            if set_attributes:
                loi_phan = '-----{}-----\n- {}\n- {}\n- {}\n- {}\n'.format(
                    set_attributes.get('tvcongiap'),
                    set_attributes.get('congviec'),
                    set_attributes.get('tinhcam'),
                    set_attributes.get('taivan'),
                    set_attributes.get('cantrong')
                )
        except:
            loi_phan = 'Có thể con giáp bạn nhập bị sai :('

        return loi_phan

    def cung_hoang_dao(self, cung_hd=''):
        url = 'https://api.kma-chatbot.com/cunghoangdao.php?cung={}'.format(cung_hd.strip())
        loi_phan = ''  # Lời phán
        try:
            r = requests.get(url)
            data_json = r.json()
            set_attributes = data_json.get('messages')

            if set_attributes:
                loi_phan = '{}'.format(
                    set_attributes[0].get('text')
                )
                
        except:
            loi_phan = 'Có thể con cung bạn nhập bị sai :( \n Bạch Dương (21/3-20/4) \n Kim Ngưu (21/4-20/5) \n Song Tử (21/5-21/6) \n Cự Giải (22/6-22/7) \n Sư tử (23/7-22/8) \n Xử Nữ (23/8-22/9) \n Thiên Bình (23/9-23/10) \n Bọ Cạp (24/10-22/11) \n Nhân Mã (23/11-21/12) \n Ma Kết (22/12-19/1) \n Bảo Bình (20/1-18/2) \n Song Ngư (19/2-20/3)'

        if loi_phan == '❌ Bạn đã nhập sai cung hoàng đạo !!':
            loi_phan = loi_phan + '\n Bạch Dương (21/3-20/4) \n Kim Ngưu (21/4-20/5) \n Song Tử (21/5-21/6) \n Cự Giải (22/6-22/7) \n Sư tử (23/7-22/8) \n Xử Nữ (23/8-22/9) \n Thiên Bình (23/9-23/10) \n Bọ Cạp (24/10-22/11) \n Nhân Mã (23/11-21/12) \n Ma Kết (22/12-19/1) \n Bảo Bình (20/1-18/2) \n Song Ngư (19/2-20/3)'
        return loi_phan



# loiphan = TuVi().con_giap(Cgiap='dan')
# loiphan = TuVi().cung_hoang_dao(cung_hd='Bạch Dương')
# print(loiphan)