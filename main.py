import os
import sys
import pandas as pd
import logging
import traceback
import time

from httplib2 import Http
from json import dumps


logging.basicConfig(format='%(asctime)-15s [%(levelname)s]: %(message)s', level=logging.INFO)
logger = logging.getLogger('main')

logger.info('start of script')
# data_dir = os.getcwd()
# fpath = os.path.join(data_dir, 'data.xlsx')
fpath = '/data/data.xlsx'


last_time = os.path.getmtime(fpath) # last update time

logger.info('file path {}'.format(fpath))

def hangout_send_message(url, text):
    bot_message = {
        'text': text
    }

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )


def read_excel_file(path):
    df = pd.read_excel(path, dtype={'Entry': str, 'Stop': str, 'Target': str, 'Lot': str})
    data = dict()
    data['name'] = df['Name'][0]
    data['type'] = df['Type'][0]
    data['direction'] = df['Direction'][0]
    data['ticker'] = df['Ticker'][0]
    data['entry'] = df['Entry'][0]
    data['SL'] = df['Stop'][0]
    data['TP'] = df['Target'][0]

    return data


if __name__ == '__main__':
    logger.info('data dir = {}'.format(fpath))

    try:
        while True:
            logger.info('Wait for file to be updated. Last update: {}'.format(last_time))
            if os.path.getmtime(fpath) != last_time:
                last_time = os.path.getmtime(fpath)
                print('File was updated. Lets execute script\n')

                # Read excel file and return dictionary
                data = read_excel_file(path=fpath)

                # Create message
                greetings = 'Доброе утро, коллеги! \n\n' \
                            'Торговый сигнал по Libertex show на сегодня. \n\n' \
                            '{0} {1} {2} ({3}) от уровня {4}. Take-profit – {5}.  Stop-loss – {6}. \n\n' \
                            'Детали можно найти в трансляции Libertex show по ссылке https://webinarfx.wistia.com/projects/r0epw9hi88' \
                    .format(data['direction'], data['type'], data['name'], data['ticker'], data['entry'], data['TP'],
                            data['SL'])

                # Send messages to google chats

                hangout_send_message('https://chat.googleapis.com/v1/spaces/AAAAPSJiFkU/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=VHttKk09UGbghrm99U0NJAAkeYfsmKYGWlX7V0wQuFY%3D', greetings)
                # urls = ['https://chat.googleapis.com/v1/spaces/AAAApIkp_5s/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=4fr0hWu-wH1ezCG8l83OjQEWg18pn_gGUKc1hBsEdIM%3D',
                #         'https://chat.googleapis.com/v1/spaces/AAAAIzUh4TQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=7Xy5SGWXEEGYtj7kS5GXyj4LGrp2ETFOdBWNM_UtIVI%3D',
                #         'https://chat.googleapis.com/v1/spaces/AAAA4CAHCY4/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=KXpBS2xPHRwsmgqW4WYZjxR9QOoOIkpCxE7V0tSaF1g%3D']
                #
                # for url in urls:
                #     hangout_send_message(url=url, text=greetings)
            time.sleep(5)

    except:
        traceback.print_exc()
        time.sleep(3)
