import json

file = open('config.json')
config = json.load(file)


# 슬랙 채널명(채널)
def get_slack_channel():
    return config['slack_channel']


# access key
def get_access_key():
    return config['access_key']


# secret_key
def get_secret_key():
    return config['secret_key']


# site_url
def get_site_url():
    return config['site_url']


# slack token
def get_slack_token():
    return config['slack_token']


# 슬랙 채널명(봇)
def get_slack_name():
    return config['slack_name']


# slack token
def get_slack_bot_token():
    return config['slack_bot_token']


# main.py path
def get_script_path():
    return config['main_script_path']


# 중지 키워드 리스트
def get_sell_keywords():
    return ['stop', '1', '그만', '멈춰', '아아']


# 슬랙 봇 채널
def get_slack_bot_channel():
    return config['slack_bot_channel']
