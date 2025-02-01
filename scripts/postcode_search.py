import requests
import json
import sys

def postcode_search(zip_code):
    """郵便番号を指定して住所を検索する"""
    
    # 郵便番号APIのURL
    url = "https://zipcloud.ibsnet.co.jp/api/search"

    # APIに送るパラメータ
    params = {"zipcode": zip_code}

    # APIリクエストを送信
    res = requests.get(url, params)

    # レスポンスのデータをJSONに変換
    data = res.json()

    # 住所情報が取得できたかチェック
    if data.get("results"):
        address_info = data["results"][0]
        address = f"{address_info['address1']} {address_info['address2']} {address_info['address3']}"
        print(f"郵便番号: {zip_code}\n住所: {address}")
    else:
        print("住所情報が見つかりませんでした。")

# コマンドライン引数を受け取る
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("郵便番号を指定してください。例: python scripts/postcode_search.py 7830060")
    else:
        postcode_search(sys.argv[1])
