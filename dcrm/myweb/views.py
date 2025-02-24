from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # 使用者'身分驗證'及'登入、登出'
from django.contrib import messages # 設置提示訊息，顯示狀態或錯誤通知，例如成功登入或錯誤訊息
from .form import SignUpForm, AddRecordFrom
from .models import Record
from django.db.models import Avg
import plotly.express as px

def home(request):
    records = Record.objects.all()
    # 前端form表單送出請求給後端
    if request.method == 'POST':   # 如果請求/request是 post 方法
        # do something in here
        username = request.POST['username'] 
        password = request.POST['password']        
        # Authenticate
        user = authenticate(request, username=username, password=password) # authenticate(request, **keywords) 檢查使用者憑證是否正確(username 和 password )
        if user is not None:
            login(request,user)        # login(request,user) 使用 login() 登入使用者
            messages.success(request, 'You have been logged in.')   # messages.success(request, message)
            return redirect('home')    # 使用 redirect('home') 重定向到首頁，避免重新提交表單。
        else:
            messages.success(request, 'There was an error logged in, please try again.')
            return redirect('home')
    else:   # 如果前端送出請求是 get 方法 畫面是 home.html 的 Login <Form>
        return render(request, 'home.html', {'records':records})
    
def logout_user(request):
    logout(request)   # 登出方法 logout()    
    messages.success(request, 'You have been logged out ...')  # 提示訊息
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)     # request.POST（一個 QueryDict 對象）中提取前端表單的 username 和 password
        if form.is_valid():                 
            # 根據 form(SignUpForm()) 內容作驗證(by 'is_valid()');如果驗證為True表示通過;如果為False，會自動填充 form.errors
            form.save() 
            # Authentication and login
            username = form.cleaned_data['username']   # 來自用戶提交表單，包含經過驗證的數據存入 cleaned_data 
            password = form.cleaned_data['password1']  
            user = authenticate(username=username, password=password)  
            login(request,user)
            messages.success(request, 'You have register successfully.')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})     # 確保無論什麼情況都能返回一個註冊頁面。

def customer_record(request, pk):       # Ex: localhost:8000/record/37, pk = 37
    if request.user.is_authenticated:   # HttpRequest.user from From the AuthenticationMiddleware 
        # Do something for logged-in users. with is_authenticated
        customer_record = Record.objects.get(id=pk) # id is from migration models
        return render(request, 'record.html', {'customer_record': customer_record})  # send "customer_record" to record.html
    else:
        # Do something for anonymous users.
        messages.success(request, "You must be logged in to view that page.")
        return redirect('home')

def delete_record(request, pk): # pk is from customer_record.id of record.html
    if request.user.is_authenticated: 
        delete_it = Record.objects.get(id=pk) # 建立一個delete_it物件實例
        delete_it.delete() 
        messages.success(request, 'Record delete successfully.')
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to view that page.")
        return redirect('home')

def add_record(request):
    form = AddRecordFrom(request.POST or None) 
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record Add Successfully...')
                return redirect('home')
        else:
            return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to view that page.")
        return redirect('home')

def update_record(request, pk): # 作法類似delete_record()
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordFrom(request.POST or None, instance = current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update the record successfully...')
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to view that page.")
        return redirect('home')
    
def dashboard(request):
    if request.user.is_authenticated: # 需要使用者登入(身分驗證)
        average = Record.objects.values('state').annotate(avg=Avg('zipcode'))
        # average <QuerySet [{'state': '台北市', 'avg': 310.5}, {'state': '台南市', 'avg': 731.0}, {'state': '台中市', 'avg': 406.0}]>
        x = average.values_list('state', flat=True) 
        y = average.values_list('avg', flat=True) 
        text = [f'{avg:.0f}' for avg in y]
        fig = px.bar(x=x, y=y, text=text, labels={x:'state', y:'avg'})
        fig.update_layout(title_text='State Distribution',
                          yaxis_range=[0,800])
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        chart = fig.to_html()
        return render(request, 'dashboard.html', {'chart':chart})
    else:
        # pass
        messages.success(request, "You must be logged in to view that page.")
        return redirect('home')