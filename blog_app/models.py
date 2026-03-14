from django.db import models  # Django’da ma’lumotlar bazasi modellarini yaratish uchun kerak
from django.utils import timezone  # Sana va vaqt bilan ishlash uchun modul
from django.contrib.auth.models import User  # Django foydalanuvchi modelini olib kelamiz
from django.urls import reverse  # URL’ni olish uchun yordamchi funksiya

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status="published")

class Post(models.Model):
    STATUS_CHOICES = (
    ("draft","Draft"),
    ("published","Published"),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts")
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="draft")

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        # Har bir postning URL manzilini olish uchun
        # blogapp:post_detail → URL pattern nomi
        # args → URL uchun parametrlar: yil, oy, kun, slug
        return reverse('blogapp:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])