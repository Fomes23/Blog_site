from django.urls import path  # URL patternlarini yaratish uchun path funksiyasini import qilamiz
from . import views          # Shu app ichidagi views.py faylini import qilamiz


app_name = 'blogapp'  # URL’larni nomlash uchun namespace
# Masalan: 'blogapp:post_list' yoki 'blogapp:post_detail' kabi ishlatish mumkin


urlpatterns = [
    # Postlar bilan ishlash uchun URL’lar
    # Barcha postlar ro'yxatini ko'rsatadigan view
    # class-based view ishlatilgan: PostListView
    path('', views.PostListView.as_view(), name='post_list'),
    # URL bo'sh bo'lsa (masalan, /blog/), barcha postlar ro'yxati ko'rinadi

    # Post detalini ko'rsatadigan view
    # URL format: /yil/oy/kun/slug/
    # Masalan: /2026/03/12/my-first-post/
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.post_detail,  # views.py ichidagi post_detail funksiyasi chaqiriladi
         name='post_detail'),  # URL nomi, template va reverse() da ishlatiladi
]