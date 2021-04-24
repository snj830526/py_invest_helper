import time

import conv
from slack import WebClient


def get_slack_client():
    bot_token = conv.get_slack_bot_token()
    return WebClient(bot_token)


def working():
    counter = 0
    client = get_slack_client()

    while True:
        bot_channel = conv.get_slack_bot_channel()
        if client is None:
            client = get_slack_client()
        response = client.conversations_history(channel=bot_channel)
        get_message = response['messages'][0]['text']
        print(f"""{get_message}""")
        if get_message in conv.get_sell_keywords():
            # 코인 전량 매도
            conv.sell_all()
            client.chat_meMessage(channel=bot_channel, text=":tada:")
            counter = 0
        else:
            if counter % 60 == 0:
                client.chat_meMessage(channel=bot_channel, text=":party_blob: $ 전량 매도 하고 싶으면 '1'을 입력 해라용.")
            print(f'reading... count : {counter}')
        time.sleep(5)
        counter = counter + 1


if __name__ == '__main__':
    working()
