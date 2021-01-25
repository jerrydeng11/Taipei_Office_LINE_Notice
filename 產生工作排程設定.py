import os
import getpass

path_0 = os.getcwd()  # 當前工作目錄
path_1 = os.path.join(path_0, '..')
os.chdir(path_1)  # 改變當前工作目錄到指定路徑
path_2 = os.getcwd()
os.chdir(path_0)  # 改變當前工作目錄到指定路徑

# 重要變數
RP=getpass.getpass("輸入使用者密碼 : ")

# 產生工作排程指令
path_00 = os.path.join(path_2, 'Task_Scheduler_env', 'Scripts', 'python.exe')
path_01 = os.path.join(path_0, 'LINE_Notify.py')
TN = 'Taipei_office_LINE_notice'
SC = r'minute' # 分鐘
MO = '1'  # 間隔
TR = r'{} {}'.format(path_00, path_01)  # 執行指令
COMPUTERNAME = os.getenv("COMPUTERNAME")
USERNAME = os.environ['USERNAME']
RU = r'{}\{}'.format(COMPUTERNAME, USERNAME)  # COMPUTERNAME\USERNAME
# RP = '密碼'  # 密碼
RL = 'HIGHEST'  # 權限
t_0 = r'SCHTASKS /Create /TN "{TN}" /SC {SC} /MO {MO} /TR "{TR}" /RU {RU} /RP {RP} /RL {RL}'.format(TN=TN, SC=SC, MO=MO, TR=TR, RU=RU, RP=RP, RL=RL)

# 產生批次檔
t_all = r'''@echo off
set t_0={t_0}
cmd /k "%t_0%"'''.format(t_0=t_0)
print(t_all)

# 存檔
with open('產生工作排程設定.bat', 'w', encoding='big5') as f:
    f.write(t_all)
