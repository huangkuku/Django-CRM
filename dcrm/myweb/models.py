from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50) # 地址 中正路100號1樓
    city = models.CharField(max_length=10) # 區 ex: 中山區
    state = models.CharField(max_length=10) # 縣市 ex:台北市
    zipcode = models.CharField(max_length=10) # 郵遞區號 # 100

    # 想要在前端畫面顯示的內容
    def __str__(self):
        return (f"Welcome! {self.first_name} {self.last_name} your stock info: {self.zipcode}")