import requests

def get_address_from_zipcode(zip_code):
    """郵便番号を元に住所を取得する関数"""
    url = "https://zipcloud.ibsnet.co.jp/api/search"
    params = {"zipcode": zip_code}
    # サーバー起動時、以下のような感じでつけるクエリパラメータ
    # http://127.0.0.1:8000/apis/postcode_search/?zipcode=5140061

    try:
        res = requests.get(url, params)
        data = res.json()

        if data.get("results"):
            address_info = data["results"][0]
            return {
                "郵便番号": address_info["zipcode"],
                "住所": f"{address_info['address1']} {address_info['address2']} {address_info['address3']}"
            }
        else:
            return {"error": "住所情報が見つかりませんでした"}
    except requests.RequestException:
        return {"error": "APIリクエストに失敗しました"}
