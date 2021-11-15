FROM python:3.9

COPY req.txt .

RUN pip install -r req.txt
COPY telegram_proxy.py .

CMD python telegram_proxy.py