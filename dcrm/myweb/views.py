from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # 使用者'身分驗證'及'登入、登出'
from django.contrib import messages # 想要在註冊時、登入、登出時出現一個訊息告知你現在的狀態如你已登入、你登出等訊息

def home(request):
    # 前端form表單送出請求給後端，如果請求/request的方法是post 就 do something in here
    if request.method == 'POST':
        # do something in here
        username = request.POST['username'] # 'username'是前端form表單的<input>裡的'name'屬性帶有'username'
        password = request.POST['password']
        # print(username) # request.POST <calss QueryDict> {'csrfmiddlewaretoken': ['O2iB6jWRcGha2ljj0hcMQPSUTv5lvylRTyoCi4rMqJdS316Veu3APaSXdpVCxh19'], 'username': ['Cathy'], 'password': ['16']}
        # Authenticate
        user = authenticate(request, username=username, password=password) # authenticate(request, **keywords) return User object
        if user is not None:
            login(request,user) # login(request,user)
            messages.success(request, 'You have been logged in.') # messages.success(request, message)
            return redirect('home')
        else:
            messages.success(request, 'There was an error logged in, please try again.')
            return redirect('home')
    else: # 如果前端沒有送出請求 畫面仍是 home.html
        return render(request, 'home.html', {})