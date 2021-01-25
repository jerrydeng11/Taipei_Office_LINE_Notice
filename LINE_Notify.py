
# 檢查是否需要通知 整合
#####################################################################
# 載入模組
import pandas as pd
import time
import requests

# 重要變數
path = r'D:\Task_Scheduler\辦公室_LINE通知\LINE Notify2.txt'

# 函數
def lineNotify(token, msg):
    """Line Notify (LENE通知)
    
    Attributes (屬性)
    -----------------
    token : str
    Get token
    https://notify-bot.line.me/zh_TW/
    
    msg : str
    Enter notification content
    
    references (引用)
    -----------------
    http://pythonorz.blogspot.com/2017/12/python-line-notify-line-notify-line.html
    """
    url = "https://notify-api.line.me/api/notify"
    headers = {
       "Authorization": "Bearer " + token,
       "Content-Type" : "application/x-www-form-urlencoded"}
    payload = {'message': msg}
    r = requests.post(url, headers = headers, params = payload)
    return r.status_code

# 讀檔
df = pd.read_csv(path, encoding='utf8')
df['date'] = pd.to_datetime(df['date'])

# 現在時間
date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()+86400*0))
print('現在時間 : {}'.format(date))

# (bool == Fales) & (date < 現在時間) 符合條件，則通知
df2 = df[df.date<date].values
for i in range(len(df2)):
    if df2[i][1] == False:
        print(df2[i][0], df2[i][2])
#         lineNotify("5Q6LYypI0LarQISvpSitg2daxYuH6CKm21NYrZkCfuU", df2[i][2])  # 測試用令牌
        lineNotify("POuifz2jxPDszLZLpy6VThR8o40Yf0xTw6MlkPU9hp5", df2[i][2])  # 正是用令牌

# (date < 現在時間) 符合條件，則把 bool 改成 True
df.loc[df.date<date, 'bool'] = True

# 存檔
df.to_csv(path, index=False, encoding='utf8')
#####################################################################
