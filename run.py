import os
import yaml
import time
#from apscheduler.schedulers.blocking import BlockingScheduler
from Checkin52pj.Checkin52pjForSCF import pjCheckin as pj
from Cloud189Checkin.C189CheckinForSCF import C189Checkin as c189
from Enshan.Enshan import main as enshan
from FF14Checkin.FF14CheckinForSCF import go as ff14
from NetEase_Music_daily.NetEase_Music_dailyForSCF import main as netease_music
from NoteyoudaoCheckin.NoteYoudaoForSCF import main as noteyoudao
from smzdmCheckin.smzdmCheckinForSCF import smzdm_pc as smzdm
from V2EX.v2ex import main as v2ex
from Zhiyou.zhiyou import main as zhiyou

with open('/etc/config/config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

def job():
    print("run start")
    try:
        c189(data["username"], data["password"])
    except:
        print("未设置天翼云配置")
    try:
        ff14(data["fflogin_name"], data["fflogin_password"], data["area_name"], data["server_name"], data["role_name"])
    except:
        print("未设置FF14配置")
    try:
        pj(data["cookie_52pj"])
    except:
        print("未设置52pojie配置")
    try:
        smzdm(data["cookie_smzdm"])
    except:
        print("未设置什么值得买配置")
    try:
        netease_music(data["netease_username"], data["netease_password"])
    except:
        print("未设置网易云音乐配置")
    try:
        noteyoudao(data["note_username"], data["note_password"])
    except:
        print("未设置有道云笔记配置")
    try:
        v2ex(data["cookie_v2ex"])
    except:
        print("未设置v2ex配置")
    try:
        enshan(data["cookie_enshan"])
    except:
        print("未设置恩山论坛配置")
    try:
        zhiyou(data["cookie_zhiyou"])
    except:
        print("未设置智友邦配置")
    print("run end")

if __name__ == "__main__":
    # scheduler = BlockingScheduler()
    # scheduler.add_job(job, 'interval', id='job', hours=8)
    print('Press Ctrl+C to exit')
    # scheduler.start()
    while 1:
        job()
        time.sleep(28800)
