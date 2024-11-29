from django.contrib.auth.forms import UserCreationForm # https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms
from django.contrib.auth.models import User
from django import forms        # Django validation and HTML form handling.

class SignUpForm(UserCreationForm): # UserCreationForm為django內建的用戶表單，能快速處理用戶註冊基本功能，包含用戶名(username)和密碼password(password1和password2，後者用於確認是否和前者相同)
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))      
    # label="" 空字串表示欄位不顯示標籤(label) attrs 允許添加不同css屬性傳遞到前端畫面上來設置表單

    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    # widget：定義欄位在前端的樣式與屬性，透過 attrs 傳遞 CSS 類別與 placeholder
    
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    # 讓表單在前端有更一致的樣式 如attrs的class 方便bootstrap的form-control placeholder有提示功能
    class Meta:
        model = User    # 指定model基於django的 User model (from django.contrib.auth.models)
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2'] # 定義哪些欄位會包含在表單中

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        # help_text：為欄位提供說明性文字，採用 HTML 格式進一步美化

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	