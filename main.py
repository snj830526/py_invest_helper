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
        print(f'test :: {bot_channel}')
        response = client.conversations_history(channel=bot_channel)
        get_message = response['messages'][0]['text']
        print(f"""마지막 메시지 ::: {get_message}""")
        if get_message in conv.get_sell_keywords():
            # 코인 전량 매도
            res = conv.sell_all()
            client.chat_meMessage(channel=bot_channel, text=f":tada: {res}")
            counter = 0
        else:
            if counter % 60 == 0:
                myinfo_map = conv.get_my_coin_info()
                if myinfo_map is not None:
                    client.chat_meMessage(channel=bot_channel, text=":meow_party: $ 전량 매도 하고 싶으면 '1'을 입력 해라냥.")
            print(f'reading... count : {counter}')
        time.sleep(5)
        counter = counter + 1


if __name__ == '__main__':
    working()
