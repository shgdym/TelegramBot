#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from const import const
import requests
import json


class TgBot:
    def __init__(self, apikey=const.API_KEY, chat_id=const.CHAT_ID):
        # self.apikey = apikey
        self.chat_id = chat_id
        self.base_url = f'https://api.telegram.org/bot{apikey}'

    def sendMediaGroup(self, paths, caption='caption', send_type='photo'):
        """
        :param send_type:[photo,audio,video,document]
        :param caption: caption
        :param paths:
        :return: http response
        """
        params = {
            'chat_id': self.chat_id,
            'media': [],
        }

        for path in paths:
            params['media'].append(
                {
                    'type': send_type,
                    'media': path,
                    'caption': caption
                }
            )

        params['media'] = json.dumps(params['media'])
        url = f'{self.base_url}/sendMediaGroup'

        return requests.post(url, data=params, timeout=120)

    def sendMessage(self, text):
        """
        :param text: str
        :return: http response
        """
        params = {
            'chat_id': self.chat_id,
            'text': text,
        }
        url = f'{self.base_url}/sendMessage?'

        return requests.post(url, data=params)
