import time

import conv
from slack import WebClient


def get_slack_client():
    bot_token = conv.get_slack_bot_token()
    slack_name = conv.get_slack_name()
    return WebClient(bot_token)


def working():
    counter = 0
    client = get_slack_client()

    while True:
        if client is None:
            client = get_slack_client()
        response = client.conversations_history(channel='D01VBGPL8LB')
        get_message = response['messages'][0]['text']
        print(f"""{get_message}""")
        if get_message in conv.get_sell_keywords():
            # 코인 전량 매도
            conv.sell_all()
            client.chat_meMessage(channel='D01VBGPL8LB', text=":tada:")
            counter = 0
        else:
            if counter % 10 == 0:
                client.chat_meMessage(channel='D01VBGPL8LB', text=":party_blob:")
            print(f'reading... count : {counter}')
        time.sleep(5)
        counter = counter + 1


if __name__ == '__main__':
    working()
