# -*- coding: UTF-8 -*-
from fbchat.models import *
from fbchat import log, Client

from tu_vi import TuVi


class VoccerBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        # log.info("hello")
        if author_id != self.uid:
            if message_object.text:
                if message_object.text == '/Getid' or message_object.text == '/getid':
                    self.send(Message(text=message_object.author), thread_id=thread_id, thread_type=thread_type)

                elif '/tuvi' in message_object.text:
                    tuoi = message_object.text[message_object.text.index('/tuvi') + len('/tuvi'):]
                    tuvi = TuVi()
                    loi_phan = tuvi.con_giap(Cgiap=tuoi)
                    self.send(Message(text=loi_phan), thread_id=thread_id, thread_type=thread_type)
                elif '/hoangdao' in message_object.text:
                    cung = message_object.text[message_object.text.index('/hoangdao') + len('/hoangdao'):]
                    tuvi = TuVi()
                    loi_phan = tuvi.cung_hoang_dao(cung_hd=cung)
                    # print('loi phan cua toi la {}'.format(loi_phan))
                    self.send(Message(text=loi_phan), thread_id=thread_id, thread_type=thread_type)
                else:
                    self.send(Message(
                        text='\n \n🙂 Tôi là Bot chat của Trong Duc. \n- Hiện tại anh ấy không thể rep tin nhắn ngay được. \n- Nếu xem tử vi gõ /tuvi <tuổi>; ví dụ: /tuvi sửu. \n-Nếu xem cung hoàng đạo gõ /hoangdao <cung>; \n ví dụ: /hoangdao song ngư\n- Tin nhắn của bạn: {0}'.format(
                            message_object.text)),
                        thread_id=thread_id,
                        thread_type=thread_type
                    )
                
                
