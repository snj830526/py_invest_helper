import conv
import uuid
import jwt
import requests
import hashlib
from urllib.parse import urlencode


# 내 계좌에 있는 코인 전부 매도(수익률에 따라 전량 매도 할지 결정하도록 변경)
def sell_all():
    myinfo_map = get_my_coin_info()

    if myinfo_map is not None:
        # 코인명
        market = get_my_coin_name(myinfo_map)
        # 내가 구매 한 코인 수
        my_coin_amount = get_my_coin_total_amount(myinfo_map)
        # 분단위 캔들
        coin_info = view_candle_min(market)
        # 코인의 현재 단가(분단위 캔들로 조회)
        current_my_coin_price = get_current_coin_price(coin_info)

        order_price = current_my_coin_price
        order_volume = my_coin_amount
        order_type = 'ask'

        # 전량 매도!
        order_coin(
            market_name=market,
            order_money=order_price,
            order_volume=order_volume,
            type=order_type
        )


# 내가 가진 코인 요약 정보 조회
def get_my_coin_info():
    account = get_my_account()
    if len(account) > 1:
        krw_balance = account[0]['balance']
        market_name = account[1]['unit_currency'] + '-' + account[1]['currency']
        buy_price = account[1]['avg_buy_price']
        balance = account[1]['balance']
        result = {market_name: [buy_price, balance, krw_balance]}
        return result
    else:
        return None


# 내가 소유 한 코인 이름
def get_my_coin_name(myinfo_map={}):
    return list(myinfo_map.keys())[0]


# 내가 소유 한 코인 수
def get_my_coin_total_amount(myinfo_map={}):
    return float(myinfo_map[get_my_coin_name(myinfo_map)][1])


# 내 계좌 정보 조회
def get_my_account():
    pay_load = {
        'access_key': conv.get_access_key(),
        'nonce': str(uuid.uuid4())
    }

    jwt_token = jwt.encode(pay_load, conv.get_secret_key())
    authorized_token = 'Bearer {}'.format(jwt_token)
    headers = {'Authorization': authorized_token}

    response = requests.request("GET", conv.get_site_url() + '/v1/accounts', headers=headers)

    return response.json()


def view_candle_min(market="KRW-BTC"):
    url = f"{conv.get_site_url()}/v1/candles/minutes/1"
    query_string = {"market": market, "count": "1", "convertingPriceUnit": "KRW"}
    response = requests.request("GET", url, params=query_string)
    return response.json()


# 일 캔들에서 값 추출(현재 코인 단가)
def get_current_coin_price(candle):
    return view_candle_min(candle[0]['market'])[0]['trade_price']


# 코인 주문(매수, 매도)
def order_coin(market_name="KRW-BTC", order_money=0, order_volume=0, type='bid'):
    query = {
        'market': market_name,
        'side': type,
        'volume': order_volume,
        'price': order_money,
        'ord_type': 'limit',
    }
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': conv.get_access_key(),
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, conv.get_secret_key())
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.post(conv.get_site_url() + "/v1/orders", params=query, headers=headers)
    return res