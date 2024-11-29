from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # 使用者'身分驗證'及'登入、登出'
from django.contrib import messages # 設置提示訊息，顯示狀態或錯誤通知，例如成功登入或錯誤訊息
from .form import SignUpForm
from .models import Record

def home(request):
    records = Record.objects.all() # objects.all() displays all the records in the database. <QuerySet [<Record: Record object (1)>]>
    # 前端form表單送出請求給後端
    if request.method == 'POST':   # 如果請求/request是 post 方法
        # do something in here
        username = request.POST['username'] 
        password = request.POST['password']
        # 從 request.POST（一個 QueryDict 對象）中提取前端表單的 username 和 password。這些鍵對應於表單中 <input> 元素的 name 屬性。 
        # <calss QueryDict> {'csrfmiddlewaretoken': ['O2iB6jWRcGha2ljj0hcMQPSUTv5lvylRTyoCi4rMqJdS316Veu3APaSXdpVCxh19'], 'username': ['Cathy'], 'password': ['16']}
        
        # Authenticate
        user = authenticate(request, username=username, password=password) 
        # authenticate(request, **keywords) 
        # 檢查使用者憑證是否正確(username 和 password )，返回 User 對象（如果正確）或 None。
        if user is not None:
            login(request,user)        # login(request,user) 使用 login 函數登入使用者
            messages.success(request, 'You have been logged in.')   # messages.success(request, message)
            return redirect('home')    # 使用 redirect('home') 重定向到首頁（避免重新提交表單的問題）。
        else:
            messages.success(request, 'There was an error logged in, please try again.')
            return redirect('home')
    else:   # 如果前端送出請求是 get 方法 畫面仍是 home.html 這時應該是已登入狀態...?
        return render(request, 'home.html', {'records':records})
    
def logout_user(request):
    logout(request)   # 使用 django 的登出方法 logout()    
    messages.success(request, 'You have been logged out ...')  # 提示訊息
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)     # request.POST（一個 QueryDict 對象）中提取前端表單的 username 和 password
        if form.is_valid(): # django 會幫我們根據 form(SignUpForm()) 內容作驗證(by 'is_valid()') 
        # 如果驗證為True表示通過。如果為False，會自動填充 form.errors
            form.save() 
            # Authentication and login
            username = form.cleaned_data['username']   # 來自用戶提交表單，包含經過驗證的數據存入cleaned_data from form(SignUpForm())的 'username'
            password = form.cleaned_data['password1']  # from form(SignUpForm())的 'password1'
            user = authenticate(username=username, password=password) # 第二個 'password'是上一行的'password'變數,源自於 'password1'
            # 檢查使用者憑證是否正確(username 和 password )，返回 User 對象（如果正確）或 None。
            login(request,user)
            messages.success(request, 'You have register successfully.')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})     # 確保無論什麼情況都能返回一個註冊頁面。

def customer_record(request, pk): # localhost:8000/record/1、localhost:8000/record/37, pk = 1 or 37
    if request.user.is_authenticated: # request.user(HttpRequest.user from From the AuthenticationMiddleware), An instance of AUTH_USER_MODEL，代表最近地使用者登入，如果使用者沒登入會得到 AnonymousUser物件實例
        # Do something for logged-in users. with is_authenticated
        customer_record = Record.objects.get(id=pk) # id is from migration models
        return render(request, 'record.html', {'customer_record': customer_record})  # send "customer_record" to record.html
    else:
        # Do something for anonymous users.
        messages.success(request, "You must be logged in to view that page.")
        return redirect('home')

def delete_record(request, pk): # pk is from customer_record.id of record.html
    if request.user.is_authenticated: # 防止有人沒登入直接輸入delete的url，那會直接觸發刪除的函式的所有動作! 所以要驗證
        delete_it = Record.objects.get(id=pk) # 建立一個delete_it物件實例
        delete_it.delete() # 調用裡面的delete方法
        messages.success(request, 'Record delete successfully.')
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to view that page.")
        return redirect('home')