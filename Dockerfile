FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD auto_restart_xiaomi_vacuum.py /
ADD token_extractor.py /
CMD [ "python", "./auto_restart_xiaomi_vacuum.py" ]
