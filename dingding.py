import requests
import json
import time
import hmac
import hashlib
import base64
import urllib

def jiaqian():
    timestamp = round(time.time() * 1000)
    secret = 'SECbac23d08f7a83bc1786d68582edc5ba4e2511c1ef96aa32ffff56c932370f02e'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    url = "https://oapi.dingtalk.com/robot/send?access_token=1dc6bb15a0896102b561283cd7cbf76871f32a7721280baf6de4e168e609b2b8&timestamp="+str(timestamp)+"&sign="+str(sign)
    print(url)
    return url

def jian():
    obj = {
        "msgtype": "markdown",
        "markdown": {
        "title":"杭州天气",
        "text": "#### 杭州天气 @150XXXXXXXX \n> 9度，西北风1级，空气良89，相对温度73%\n> ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n> ###### 10点20分发布 [天气](https://www.dingtalk.com) \n"
        },
        "at": {
            "atMobiles": [
                "150XXXXXXXX"
            ],
            "isAtAll": False
        }
    }
    return obj

def latext():
    requests.post(
        url=jiaqian(),
        headers={'Content-Type': 'application/json'},
        data=json.dumps(obj=jian())
    )


def main():
    latext()

if __name__ == "__main__":
    main()
