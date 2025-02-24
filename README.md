## A CRM (顧客管理關係) App 
此為簡易的顧客管理關係CRM(Customer Relationship Management)平台，
收集客戶的相關資訊，如姓名、電話、Email，地址、購買量等資訊，
以增進企業與客路之間的關係，增加企業銷售收入和提高客戶留存
具有數據儀表板功能，展示簡易長條圖。
## 目錄
- [專案介紹](#專案介紹)
- [功能](#功能)
- [安裝](#安裝)
- [使用技術](#使用技術)
- [如何使用](#如何使用)
- [貢獻](#貢獻)
- [授權](#授權)

## 專案介紹
Django-CRM 是一個基於 Django 的客戶關係管理系統，旨在提供用戶一個方便的工具來管理客戶資料和查看相關數據。

## 功能
- 客戶資料管理
- 數據儀表板
- 簡易長條圖展示
### View Records
![image](https://github.com/huangkuku/Django-CRM/blob/main/png/view_record%20%E9%A6%96%E9%A0%81.png)

### Register
![image](https://github.com/huangkuku/Django-CRM/blob/main/png/register%E8%A8%BB%E5%86%8A.png)

### Log In, Log Out
![image](https://github.com/huangkuku/Django-CRM/blob/main/png/login%E7%99%BB%E5%85%A5.png)
![image](https://github.com/huangkuku/Django-CRM/blob/main/png/logout%E7%99%BB%E5%87%BA.png)

### Add Records
![image](https://github.com/huangkuku/Django-CRM/blob/main/png/add_record%20%E6%96%B0%E5%A2%9E.png)
![image](https://github.com/huangkuku/Django-CRM/blob/main/png/add_record%20%E6%96%B0%E5%A2%9E2.png)
![image](https://github.com/huangkuku/Django-CRM/blob/main/png/add_record%20%E6%96%B0%E5%A2%9E3.png)

### Update Records
![image](https://github.com/huangkuku/Django-CRM/blob/main/png/update_0.png)
![image](https://github.com/huangkuku/Django-CRM/blob/main/png/update_1.png)
![image](https://github.com/huangkuku/Django-CRM/blob/main/png/update_2.png)
![image](https://github.com/huangkuku/Django-CRM/blob/main/png/update_3.png)

### Delete Records 
![image](https://github.com/huangkuku/Django-CRM/blob/main/png/delete%20%E5%88%AA%E9%99%A4.png)
### Dachborad
![image](https://github.com/huangkuku/Django-CRM/blob/main/png/dashboard%20%E5%84%80%E9%8C%B6%E6%9D%BF.png)

## 安裝
1. 克隆此專案到本地：
    ```bash
    git clone https://github.com/huangkuku/Django-CRM.git
    ```
2. 安裝依賴：
    ```bash
    pip install -r requirements.txt
    ```

## 使用技術
- Frontend:
  * Bootstrap5
- Backend:
  * Django 5.1
  * MySQL 
        - mysqlclient 2.2.6
  * Plotly express 5.24
  * Pandas
  * Numpy

## 如何使用
1. 設置資料庫：
    ```plaintext
    配置你的 MySQL 資料庫資訊在 .env 文件中
    ```
2. 遷移資料庫：
    ```bash
    python manage.py migrate
    ```
3. 啟動 Django 伺服器：
    ```bash
    python manage.py runserver
    ```
4. 開啟瀏覽器，訪問 `http://127.0.0.1:8000` 查看應用程式。

## 貢獻
歡迎任何形式的貢獻！請閱讀 [CONTRIBUTING.md](CONTRIBUTING.md) 了解更多資訊。

## 授權
此專案採用 MIT 授權，詳情請參閱 [LICENSE](LICENSE) 文件。
