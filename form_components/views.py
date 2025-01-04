from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from form_components.forms import HelloForm,BSForm,PulldownForm,SessionForm


#prefixのURLは「form_components/」

#requestはHttpRequestクラスのインスタンス
def sample1(request, id, nickname):
    result = 'your id: ' + str(id) + ', name: ' + nickname + '.'
    return HttpResponse(result)

def sample2(request, nickname, age):
    result = 'your account: ' + nickname + '(' + str(age) + ').'
    return HttpResponse(result)

def sample3(request):
    params = {
        'title':'Hello/home',
        'msg':'これは、サンプルで作ったページです。',
        'goto':'next_sample3'
    }
    return render(request, 'form_components/sample.html', params)

def next_sample3(request):
    params = {
        'title':'Hello/Next',
        'msg':'これは、もう1つのページです。',
        'goto':'sample3'
    }
    return render(request, 'form_components/sample.html', params)

def form_input(request):
    params = {
        'title':'Hello/Form',
        'msg':'お名前は？',
    }
    return render(request, 'form_components/form.html', params)

def form_response(request):
    msg = request.POST['msg']
    params = {
        'title':'Hello/Form',
        'msg':'こんにちは、' + msg + 'さん。'
    }
    return render(request, 'form_components/form.html', params)

def form_by_FormClass(request):
    params = {
        'title':'Hello',
        'message':'your data:',
        'form':HelloForm()#フォームの値を元にHelloFormインスタンスを設定
    }
    if (request.method == 'POST'):
        params['message'] = '名前：' + request.POST['name'] + \
            '<br>メール：' + request.POST['mail'] + \
            '<br>年齢：' + request.POST['age']
        params['form'] = HelloForm(request.POST)
    return render(request, 'form_components/classform.html', params)

def bs_form(request):
    params = {
        'title':'Hello',
        'message':'your data:',
        'form':BSForm()#フォームの値を元にHelloFormインスタンスを設定
    }
    if (request.method == 'POST'):
        params['message'] = '名前：' + request.POST['name'] + \
            '<br>メール：' + request.POST['mail'] + \
            '<br>年齢：' + request.POST['age']
        params['form'] = BSForm(request.POST)
    return render(request, 'form_components/BS_form.html', params)

class BSFormview(TemplateView):

    def __init__(self):
        self.params = {
            'title':'Hello',
            'message':'your data:',
            'form':BSForm(),
        }
    
    def get(self, request):
        return render(request, 'form_components/BS_form_by_class.html', self.params)
    
    def post(self, request):
        msg = 'あなたは、<b>' + request.POST['name'] + '（' + request.POST['age'] + \
                '）</b>さんです。<br>メールアドレスは <b>' + request.POST['mail'] + '</b>ですね。'
        self.params['message'] = msg
        self.params['form'] = BSForm(request.POST)
        return render(request, 'form_components/BS_form_by_class.html', self.params)

class Checkboxform(TemplateView):

    def __init__(self):
        self.params = {
            'title':'Hello',
            # 'message':'your data:',
            'form':BSForm(),
            'result':None
        }

    def get(self, request):
        return render(request, 'form_components/BS_checkbox.html', self.params)

    def post(self, request):
        # msg = 'あなたは、<b>' + request.POST['name'] + '（' + request.POST['age'] + \
        #     '）</b>さんです。<br>メールアドレスは <b>' + request.POST['mail'] + '</b>ですね。'
        if ('check' in request.POST):
            self.params['result'] = 'Checked!!'
        else:
            self.params['result'] = 'not checked...'
        self.params['form'] = BSForm(request.POST)
        # self.params['message'] = msg
        return render(request, 'form_components/BS_checkbox.html', self.params)
    

class Pulldown(TemplateView):

    def __init__(self):
        self.params = {
            'title':'Hello',
            'form':PulldownForm(),
            'result':None
        }
    
    def get(self, request):
        return render(request, 'form_components/pulldown_menu.html', self.params)
    
    def post(self, request):
        ch = request.POST['choice']
        self.params['result'] = 'selected: "' + ch + '".'
        self.params['form'] = PulldownForm(request.POST)
        return render(request, 'form_components/pulldown_menu.html', self.params)


class SessionView(TemplateView):
#Sessionを使う場合はあらかじめアプリ内にmigrationファイルを作りmigrateを実行する必要がある
    def __init__(self):
        self.params = {
            'title':'Hello',
            'form':SessionForm(),
            'result':None
        }
    
    def get(self, request):
        self.params['result'] = request.session.get('last_msg', 'No message.')
        #Httprequest.session.get(key,default_value)
        #指定したキーの値が存在しない場合は、代わりにデフォルト値を値として返す
        #getの代わりにpopを使うと、値を取り出したら、その値をセッションから消去する
        return render(request, 'form_components/session.html', self.params)
    
    def post(self, request):
        ses = request.POST['session']
        self.params['result'] = 'send: "' + ses + '".'
        request.session['last_msg'] = ses
        self.params['form'] = SessionForm(request.POST)
        return render(request, 'form_components/session.html', self.params)

# def sample_middleware(get_response):

#     def middleware(request):
#         counter = request.session.get('counter', 0)
#         request.session['counter'] = counter + 1
#         response = get_response(request)
#         #get_response：リクエストからレスポンスを取得するための関数
#         #get_responseより前に記述したものは、views.pyの処理が呼び出される前に実行される
#         #get_responseの後に記述したものは、views.pyの処理が実行されてrenderなどでHttpResponseが返された後で実行される
#         print("count: " + str(counter))
#         return response
    
#     return middleware

# #ミドルウェアは上記のようにクラス（または関数）の中に、関数が入っているという形になる
# #中身の関数がミドルウェアの本体部分

# #ミドルウェアは作成後、settings.pyでアプリ同様登録しないといけない

