import os
import yaml
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

with open('/etc/config/config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
try:
    os.environ["username"] = data["username"]
    os.environ["password"] = data["password"]
except:
    print("未设置天翼云配置")
try:
    os.environ["fflogin_name"] = data["fflogin_name"]
    os.environ["fflogin_password"] = data["fflogin_password"]
    os.environ["area_name"] = data["area_name"]
    os.environ["server_name"] = data["server_name"]
    os.environ["role_name"] = data["role_name"]
except:
    print("未设置FF14配置")
try:
    os.environ["cookie_52pj"] = data["cookie_52pj"]
except:
    print("未设置52pojie配置")
try:
    os.environ["cookie_smzdm"] = data["cookie_smzdm"]
except:
    print("未设置什么值得买配置")
try:
    os.environ["netease_username"] = data["netease_username"]
    os.environ["netease_password"] = data["netease_password"]
except:
    print("未设置网易云音乐配置")
try:
    os.environ["note_username"] = data["note_username"]
    os.environ["note_password"] = data["note_password"]
except:
    print("未设置有道云笔记配置")
try:
    os.environ["cookie_v2ex"] = data["cookie_v2ex"]
except:
    print("未设置v2ex配置")
try:
    os.environ["cookie_enshan"] = data["cookie_enshan"]
except:
    print("未设置恩山论坛配置")
try:
    os.environ["cookie_zhiyou"] = data["cookie_zhiyou"]
except:
    print("未设置智友邦配置")

def job():
    print("run start")
    c189()
    ff14()
    pj()
    smzdm()
    netease_music()
    noteyoudao()
    v2ex()
    enshan()
    zhiyou()
    print("run end")

if __name__ == "__main__":
    scheduler = BlockingScheduler(timezone='Asia/Shanghai')
    scheduler.add_job(job, 'interval', id='job', seconds=30)
    print('Press Ctrl+C to exit')
    scheduler.start()
