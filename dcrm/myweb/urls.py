from django.urls import path
from . import views # 從同一個資料夾(myweb)匯入其他檔案: views.py

urlpatterns = [
    path('', views.home, name='home'),  
    # path('login/', views.login_user, name='login'),  # name='login' 可以讓我們html的 href="/login/"寫成href="{% url 'login' %}" 方便指認url裡的哪一個path(靠的就是'name'參數)
    path('logout/', views.logout_user, name='logout'),  
    
]
# views.home > views.py裡有 'home' function