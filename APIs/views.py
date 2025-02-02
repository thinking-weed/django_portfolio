from django.shortcuts import render
from django.http import JsonResponse
from APIs.functions import get_address_from_zipcode  # 別ファイルの関数をインポート
from fastapi import FastAPI

def postcode_search(request):
    """郵便番号を元に住所を検索するAPIビュー"""
    
    zip_code = request.GET.get("zipcode")
    if not zip_code:
        return JsonResponse({"error": "郵便番号を指定してください"}, status=400)

    response_data = get_address_from_zipcode(zip_code)
    return JsonResponse(response_data,
                        json_dumps_params={"ensure_ascii": False}
                        )

#------------------------------以下 FASTAPIの処理---------------------------------------

# FastAPIのインスタンスを作成
app = FastAPI()

#GETかつエンドポイント