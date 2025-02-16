#Pythonのタイプヒントの記述方法
#関数のパラメータの後ろに:（コロン）を付けて、その後に型名を書く
#戻り値については、閉じ括弧の後ろに矢印（->）を付けて、その後ろに型名を書いて示す

#整数型の「型ヒント」
#引数：整数型、戻り値：文字列型
def add(num1: int, num2: int) -> str:
    #変数に「型ヒント」
    result:str = '足し算結果=>'
    return result + str(num1 + num2)

#文字列型の「型ヒント」
#引数：文字列型、戻り値：文字列型
def greet(name:str) ->str:
    return f"おはよう!{name}!"

#浮動小数点型の「型ヒント」
#引数：浮動小数点型、戻り値：浮動小数点型
def divide(dividend: float, divisor: float) -> float:
    return dividend / divisor

#リスト型の「型ヒント」
#3.8以前の書き方
from typing import List
# 引数：リスト「整数型」、戻り値：リスト「整数型」
def get_first_three_elements(elements: List[int]) -> List[int]:
    return elements[:3]  #リストの最初から３個の要素を取り出す

#辞書型の「型ヒント」
#3.8以前の書き方
from typing import Dict
# 引数：辞書「文字列型、整数型」、文字列型、戻り値：整数型
def get_value(dictionary: Dict[str, int], key: str) -> int:
    return dictionary[key]

#Python3.9からは、「型ヒント」でのリストや辞書などの
#標準コレクションの指定方法が簡略化されました。
#リストの「型ヒント」
#引数：リスト「文字列型」、戻り値：なし
def process_items(items: list[str]) -> None:
    for item in items:
        print(item)

#辞書の「型ヒント」
#引数：リスト「文字列型」、戻り値：辞書「文字列型、整数型」
def count_characters(word_list: list[str]) -> dict[str, int]:
    #変数に「型ヒント」
    count_map: dict[str, int] = {}
    for word in word_list:
        #キー：文字列、値：文字列に対応する文字数
        count_map[word] = len(word)
    return count_map



