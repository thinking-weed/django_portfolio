#formの内容を定義しておくファイル

from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.IntegerField(label='age')
    check = forms.BooleanField(label='Checkbox', required=False)
    #required=Trueだと、チェックをOFFにしたまま（未入力扱いになる）では送信ができない

#Bootstrapのform-controlを使うためのクラス
class BSForm(forms.Form):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.CharField(label='mail', widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(label='age', widget=forms.NumberInput(attrs={'class':'form-control'}))
    check = forms.BooleanField(label='Checkbox', required=False)


class PulldownForm(forms.Form):
    pulldown_data=[
        ('one', 'item1'),
        ('two', 'item2'),
        ('three', 'item3')
    ]
    choice = forms.ChoiceField(label='Choice',choices=pulldown_data)


class SessionForm(forms.Form):
    session = forms.CharField(label='session', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
#ここに入力して送信した値をセッションに保管
#Djangoにおけるセッションの値はアクセス時の処理を行う関数・メソッドの引数で渡されるHttpRequestインスタンスの
#「session」という属性に保管されている
#※SessionBaseというクラスを継承したものとして定義されている


