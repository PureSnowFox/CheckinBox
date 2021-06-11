import os
import threading
import schedule
import time
from Checkin52pj.Checkin52pjForSCF import pjCheckin as pj
from Cloud189Checkin.C189CheckinForSCF import C189Checkin as c189
from Enshan.Enshan import main as enshan
from FF14Checkin.FF14CheckinForSCF import go as ff14
from NetEase_Music_daily.NetEase_Music_dailyForSCF import main as netease_music
from NoteyoudaoCheckin.NoteYoudaoForSCF import check as noteyoudao
from smzdmCheckin.smzdmCheckinForSCF import smzdm_pc as smzdm
from V2EX.v2ex import main as v2ex
from Zhiyou.zhiyou import main as zhiyou

username = os.environ.get("username")
password = os.environ.get("password")
fflogin_name = os.environ.get("fflogin_name")
fflogin_password = os.environ.get("fflogin_password")
area_name = os.environ.get("area_name")
server_name = os.environ.get("server_name")
role_name = os.environ.get("role_name")
cookie_pj = os.environ.get("cookie_52pj")
cookie_smzdm = os.environ.get("cookie_smzdm")
netease_username = os.environ.get("netease_username")
netease_password = os.environ.get("netease_password")
note_username = os.environ.get("note_username")
note_password = os.environ.get("note_password")
cookie_v2ex = os.environ.get("cookie_v2ex")
cookie_enshan = os.environ.get("cookie_enshan")
cookie_zhiyou = os.environ.get("cookie_zhiyou")

def job():
    print("run start")
    if username and password:
        c189()
    if fflogin_name and fflogin_password and area_name and server_name and role_name:
        ff14()
    if cookie_pj:
        pj()
    if cookie_smzdm:
        smzdm()
    if netease_username and netease_password:
        netease_music()
    if note_username and note_password:
        noteyoudao()
    if cookie_v2ex:
        v2ex()
    if cookie_enshan:
        enshan()
    if cookie_zhiyou:
        zhiyou()
    print("run end")

# 定时任务
def scheduleTask():
    # 任务执行时间，跟你服务器所在时区有关。北京时间:UTC+8
    schedule.every(3).minutes.do(job)
    while True:
        # 启动服务
        schedule.run_pending()
        time.sleep(5)

if __name__ == "__main__":
    threading.Thread(target=scheduleTask).start()
    
