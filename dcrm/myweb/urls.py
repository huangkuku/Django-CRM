from django.urls import path
from . import views # 從同一個資料夾(myweb)匯入其他檔案: views.py

urlpatterns = [
    path('', views.home, name='home'),  
    # path('login/', views.login_user, name='login'),  # name='login' 可以讓我們html的 href="/login/"寫成href="{% url 'login' %}" 方便指認url裡的哪一個path(靠的就是'name'參數)
    path('logout/', views.logout_user, name='logout'),  
    path('register/', views.register_user, name='register'),  
    path('record/<int:pk>', views.customer_record, name='record'),  # 這裡的pk是primary key 因為id 本身是primary key 你也可以直接寫 id，localhost:8000/record/1、localhost:8000/record/37 pk = 1 or 37
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),  
    path('add_record', views.add_record, name='add_record'),  
    path('update_record/<int:pk>', views.update_record, name='update_record'),  
]
# views.home > views.py裡有 'home' function