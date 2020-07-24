import json
import config  # 標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session  # OAuthのライブラリの読み込み

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)  # 認証処理

getUrl = "https://api.twitter.com/1.1/statuses/user_timeline.json"  # タイムライン取得エンドポイント

params = {'count': 1, 'include_rts': 'false'}  # 取得数, RTを含むか
res = twitter.get(getUrl, params=params)

if res.status_code == 200:
    timelines = json.loads(res.text)
else:
    print("Failed: %d" % res.status_code)

delUrl = "https://api.twitter.com/1.1/statuses/destroy/" + timelines[0]["id_str"] + ".json"
res = twitter.post(delUrl)

if res.status_code == 200:
    print("Success.")
else:
    print("Failed: %d" % res.status_code)