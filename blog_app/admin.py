from django.contrib import admin  # Django ning admin panel modulini import qilamiz
from .models import Post  # Shu app ichidagi Post modelini import qilamiz

# Post modelini admin panelga ro'yxatdan o'tkazamiz
# Bu decorator orqali Post modeli admin panelda ko'rinadi
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status','publish','created','author')
    search_fields = ('title', 'body')
    # Slug maydonini avtomatik to'ldirish
    # title yozilganda slug avtomatik generatsiya bo'ladi
    prepopulated_fields = {'slug': ('title',)}
    # Author tanlashni oddiy dropdown emas balki ID orqali qilish
    # Bu juda ko'p user bo'lsa adminni tezlashtiradi
    raw_id_fields = ('author',)
    # Sana bo'yicha navigatsiya (year → month → day)
    # publish field asosida ishlaydi
    date_hierarchy = 'publish'
    # Postlarni tartiblash
    # avval status bo'yicha, keyin publish sanasi bo'yicha
    ordering = ('status', 'publish')
