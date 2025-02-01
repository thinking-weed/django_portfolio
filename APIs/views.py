from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

def postcode_search(request):
    """郵便番号を元に住所を検索するAPIビュー"""
    
    # クエリパラメータから郵便番号を取得
    zip_code = request.GET.get("zipcode")

    # 郵便番号が指定されていない場合、エラーレスポンスを返す
    if not zip_code:
        return JsonResponse({"error": "郵便番号を指定してください"}, status=400)

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
        response_data = {
            "郵便番号": address_info["zipcode"],
            "住所": f"{address_info['address1']} {address_info['address2']} {address_info['address3']}"
        }
    else:
        response_data = {"error": "住所情報が見つかりませんでした"}

    # JSONレスポンスを返す
    return JsonResponse(response_data,json_dumps_params={"ensure_ascii": False})
