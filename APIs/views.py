from django.http import JsonResponse,HttpResponse # type: ignore
import json
from itertools import islice
# 別ファイルの関数をインポート
from APIs.functions import get_address_from_zipcode
from APIs.typehints_sample1 import (
    add,
    greet,
    divide,
    get_first_three_elements,
    get_value,
    process_items,
    count_characters,
    )
from APIs.typehints_sample2 import get_profile

def postcode_search(request):
    """郵便番号を元に住所を検索するAPIビュー"""
    
    zip_code = request.GET.get("zipcode")
    if not zip_code:
        return JsonResponse(
                            {"error": "郵便番号を指定してください"},
                            status=400
                            )

    response_data = get_address_from_zipcode(zip_code)
    return JsonResponse(response_data,
                        json_dumps_params={"ensure_ascii": False}
                        )

# --------------------------------------------------------------------------------------------

def typehints_sample1(request):
    num1 = 10
    num2 = 20
    add_result = add(num1,num2)
    dividend = 10.0
    divisor = 2.0
    divide(dividend, divisor)
    sample_list1 = [1,2,3,4,5]
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    key_at_index_1 = next(islice(sample_dict.keys(), 2, 3))
    #islice(data.keys(), 1, 2) は、キーのリストからインデックス 2 から 3 の範囲をスライス
    sample_list2 = ('apple', "amazon", 'google')
    params = [
        f"{num1}+{num2}の{add_result}",
        greet("hogehoge"),
        f"{dividend}÷{divisor}={divide(10.0, 2.0)}",
        f"{sample_list1}の最初から３つの要素を取り出すと、{get_first_three_elements(sample_list1)}",
        f"{sample_dict}の {key_at_index_1} に対応する値は、{get_value(sample_dict, 'c')}",
        process_items(["リンゴ", "ゴリラ", "ラッパ"]),
        f"({', '.join(sample_list2)})の文字数はそれぞれ("
        f"{'、'.join(f'{key}: {value}' for key, value in count_characters(sample_list2).items())})"]
    # 各要素を個別に文字列化し、改行（<br>）で結合
    results = "<br>".join(str(param) for param in params)
    #paramsの後ろに if param is not Noneを追記すると
    return HttpResponse(results)

# ---------------------------------------------------------------------------------------------------

def typehints_sample2(request):
    user_profile = get_profile(email= 'user@example.com')
    return HttpResponse(json.dumps(user_profile), content_type="application/json")








