from django.shortcuts import render, get_object_or_404
# render → template ni ochib brauzerga chiqarish uchun
from .models import Post
from django.views.generic import ListView
# Django ning tayyor class-based view (ro'yxat ko'rsatish uchun)

# Barcha postlarni ro'yxat qilib chiqaradigan class-based view
class PostListView(ListView):
    queryset = Post.published.all()
    # Ma'lumotlar bazasidan faqat published statusdagi postlarni oladi
    # published → biz modelda yozgan custom manager
    context_object_name = 'posts'
    # Template ichida ma'lumot nomi
    # HTML da biz posts orqali postlarga murojaat qilamiz
    paginate_by = 2
    # Pagination (sahifalash)
    # Har sahifada 2 ta post chiqadi
    template_name = 'blog/post/list.html'
    # Qaysi HTML template ishlatilishini ko'rsatadi


# Bu eski usul (function-based view)
# Yuqoridagi class-based view bilan bir xil ish qiladi
# def post_list(request):
#     posts = Post.published.all()
#     return render(request, 'blog/post/list.html', {'posts': posts})


# Bitta postning to'liq sahifasini ko'rsatadigan view
def post_detail(request, year, month, day, slug):

    post = get_object_or_404(
        Post,
        slug=slug,                 # URL dan kelgan slug
        status='published',        # Faqat published post
        publish__year=year,        # publish yilini tekshiradi
        publish__month=month,      # publish oyini tekshiradi
        publish__day=day           # publish kunini tekshiradi
    )

    # Agar post topilsa detail sahifani ochadi
    return render(request, 'blog/post/detail.html', {'post': post})