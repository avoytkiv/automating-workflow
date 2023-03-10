FROM python:3.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

# Bundle app source
COPY . .
CMD [ "python", "main.py" ]