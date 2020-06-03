FROM python:3.7

WORKDIR /usr/src/app

RUN apt-get install tzdata
ENV TZ Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


#COPY data.xlsx /var/lib/trade
COPY requirements.txt ./
RUN pip install -r requirements.txt
#RUN mkdir -p ./data

# Bundle app source
COPY . .
CMD [ "python", "main.py" ]