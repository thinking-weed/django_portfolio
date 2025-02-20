from typing import Annotated

#引数で渡された整数値が指定された範囲内にあるかをチェッする関数
#引数：数値型（Annotated）
#戻り値:None
def process_value(
    value: Annotated[int, '範囲内: 0 <= value <=100']
    ) -> None:
    #値が指定された範囲内にあるかチェックする
    if 0 <= value <= 100:
        #値が範囲内の場合の処理
        result = f"受け取った値は範囲内です: {value}"
        return result
    else:
        #値が範囲外の場合の処理
        raise ValueError(f"範囲外の値です。受け取った値：{value}")