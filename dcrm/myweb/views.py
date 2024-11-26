from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout # 使用者'身分驗證'及'登入、登出'
from django.contrib import messages # 想要在註冊時、登入、登出時出現一個訊息告知你現在的狀態如你已登入、你登出等訊息

# Create your views here.
def home(request):
    # 如果請求的方法是post 就 do something in here
    if request.method == 'POST':
        # do something in here
        return
    return render(request, 'home.html', {})


# def logout_user(request):
#     pass