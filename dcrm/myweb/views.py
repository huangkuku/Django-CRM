from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # 使用者'身分驗證'及'登入、登出'
from django.contrib import messages # 設置提示訊息，顯示狀態或錯誤通知，例如成功登入或錯誤訊息

def home(request):
    # 前端form表單送出請求給後端，如果請求/request是 post 方法,
    if request.method == 'POST':
        # do something in here
        username = request.POST['username'] 
        password = request.POST['password']
        # 從 request.POST（一個 QueryDict 對象）中提取前端表單的 username 和 password。這些鍵對應於表單中 <input> 元素的 name 屬性。 
        # <calss QueryDict> {'csrfmiddlewaretoken': ['O2iB6jWRcGha2ljj0hcMQPSUTv5lvylRTyoCi4rMqJdS316Veu3APaSXdpVCxh19'], 'username': ['Cathy'], 'password': ['16']}
        # Authenticate
        user = authenticate(request, username=username, password=password) 
        # authenticate(request, **keywords) 檢查使用者憑證是否正確，返回 User 對象（如果正確）或 None。
        # 檢查 username 和 password 是否正確。如果正確，返回對應的 User 對象；否則返回 None。
        if user is not None:
            login(request,user) 
            # login(request,user) 使用 login 函數登入使用者
            messages.success(request, 'You have been logged in.') 
            # messages.success(request, message)
            return redirect('home')
            # 使用 redirect('home') 重定向到首頁（避免重新提交表單的問題）。
        else:
            messages.success(request, 'There was an error logged in, please try again.')
            return redirect('home')
    else: # 如果前端送出請求是 get 方法 畫面仍是 home.html
        return render(request, 'home.html', {})
    
def logout_user(request):
    # 使用django的登出方法logout()
    logout(request)
    # 提示訊息
    messages.success(request, 'You have been logged out ...')
    return redirect('home')