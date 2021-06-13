import os
from apscheduler.schedulers.blocking import BlockingScheduler
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
        print("1")
        c189()
    if fflogin_name and fflogin_password and area_name and server_name and role_name:
        print("2")
        ff14()
    if cookie_pj:
        print("3")
        pj()
    if cookie_smzdm:
        print("4")
        smzdm()
    if netease_username and netease_password:
        print("5")
        netease_music()
    if note_username and note_password:
        print("6")
        noteyoudao()
    if cookie_v2ex:
        print("7")
        v2ex()
    if cookie_enshan:
        print("8")
        enshan()
    if cookie_zhiyou:
        print("9")
        zhiyou()
    print("run end")

if __name__ == "__main__":
    scheduler = BlockingScheduler(timezone='Asia/Shanghai')
    scheduler.add_job(job, 'interval', id='job', seconds=30)
    print('Press Ctrl+C to exit')
    scheduler.start()
