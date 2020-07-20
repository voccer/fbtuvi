
from datetime import datetime  
import pytz  

IST = pytz.timezone('Asia/Ho_Chi_Minh')  

print(datetime.now(IST).month)