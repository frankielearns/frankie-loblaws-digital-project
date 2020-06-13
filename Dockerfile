FROM python:3.8.3
WORKDIR /code
COPY compare.py /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD [ "python", "./compare.py" ]
