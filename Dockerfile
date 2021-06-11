FROM python:3.8.10

RUN python3 -m pip config set global.index-url https://mirrors.aliyun.com/pypi/simple

COPY . /checkinbox

WORKDIR /checkinbox

RUN python3 -m pip install -r requirements.txt

CMD python3 ./Cloud189Checkin/C189CheckinForSCF.py \
    && python3 ./FF14Checkin/FF14CheckinForSCF.py \
    && python3 ./smzdmCheckin/smzdmCheckinForSCF.py \
    && python3 ./NetEase_Music_daily/NetEase_Music_dailyForSCF.py \
    && python3 ./NoteyoudaoCheckin/NoteYoudaoForSCF.py \
    && python3 ./V2EX/v2ex.py \
    && python3 ./Enshan/Enshan.py \
    && python3 ./Zhiyou/zhiyou.py \
    && python3 ./Checkin52pj/Checkin52pjForSCF.py
