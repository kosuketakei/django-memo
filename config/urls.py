from django.contrib import admin
from django.urls import path, include

# ルーティング設定
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

# 管理サイトの見出しを変更可能
#  タイトル；タイトルタグで使用
admin.site.site_title = 'タイトル'
#  サイト名：ログイン画面と管理画面上部の表示
admin.site.site_header = 'メモアプリ'
#  メニュー：管理画面の見出し表示
admin.site.index_title = 'メニュー'
