from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms        # Django validation and HTML form handling.
from .models import Record

class SignUpForm(UserCreationForm): # UserCreationForm為django內建的用戶表單，能快速處理用戶註冊基本功能，包含用戶名(username)和密碼password(password1和password2，後者用於確認是否和前者相同)
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))      
    # label="" 空字串表示欄位不顯示標籤(label) 

    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    # widget：定義欄位在前端的樣式與屬性，forms.TextInput表示前端顯示為form表單的<Input> type='text'
    
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    # 透過 attrs 傳遞 CSS 類別與 placeholder，attrs的class是bootstrap的form-control樣式、 placeholder有提示功能
    class Meta: # 指定表單的應該使用的model和欄位fields，不用我們再手動逐一指定欄位
        model = User    # model填入對應之Model; 指定model基於django的 User model (from django.contrib.auth.models)
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2'] # 定義哪些欄位會包含在表單中

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 

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


# Create Add Record Form
class AddRecordFrom(forms.ModelForm): # 繼承 forms.ModelForm
    # 根據 models.py內提到的內容去寫html的格式
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),label='')
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),label='')
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),label='')
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),label='')
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),label='')
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),label='')
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'State'}),label='')
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Stock'}),label='')

    class Meta:
        model = Record # 指定我們要的model: Record
        exclude = ("user",) # exclude()忽略某個欄位
        # 指定包含的字段(field)fields=['username', '...', ...] or 我們除了哪個其他都要?('不要的user', (逗號後空白是指上面的那些變數))