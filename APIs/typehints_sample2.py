from typing import Optional
#Optional戻り値にNoneを戻り値として許容する

#ユーザー情報を持つプロフィール返却する関数
#引数：文字列型、文字列型/Optional、数値型/Optional
#戻り値：辞書型
def get_profile(
        email: str,
        username: Optional[str] = None,
        age: Optional[int] = None
    ) -> dict:
    profile = {"email": email}
    if username:
        # usernameが引数に存在すれば、格納
        profile["username"] = username
    if age:
        # ageが引数に存在すれば、辞書型へ追加
        profile["age"] = age
    return profile








