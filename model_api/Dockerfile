FROM python:3.9

COPY req.txt .

RUN pip install -r req.txt
COPY model_api.py .

CMD python model.api.py