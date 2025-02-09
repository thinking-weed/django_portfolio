#整数型の「型ヒント」
#引数：整数型、戻り値：文字列型
def add(num1: int, num2: int) -> str:
    #変数に「型ヒント」
    result:str = '足し算結果=>'
    return result + str(num1 + num2)


