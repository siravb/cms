from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel,TreeForeignKey



class Category(MPTTModel):
    """Модель категорий статей"""
    name = models.CharField("Название", max_length=150)
    slug = models.SlugField("url", max_length=160)
    active = models.BooleanField("Опубликовать", default=True)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    """Модель тегов к статьям"""
    name = models.CharField("Название", max_length=50)
    slug = models.SlugField("url", max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Post(models.Model):
    """Модель статей"""
    title = models.CharField("Заголовок", max_length=150)
    sub_title = models.CharField("Подзаголовок", max_length=150)
    mini_text = models.TextField("Превью статьи",max_length=500)
    text = models.TextField("Текст статьи")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    publish_date = models.DateTimeField("Дата публикации", default=timezone.now)
    active = models.BooleanField("Опубликовать", default=True)
    sort = models.PositiveIntegerField("Порядок", default=0, unique=True)
    view = models.PositiveIntegerField("Просмотры", default=0)
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    slug = models.SlugField("url", max_length=100, unique=True)
    category = models.ForeignKey(Category, verbose_name="Категория",on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"category":self.category.slug, "slug": self.slug})

    def comment_all(self):
        return Comment.objects.filter(post_id=self.id, moderation=True)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-created"]


class Comment(models.Model):
    """Модель комментариев к статьям"""
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="Статья", on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created = models.DateTimeField("Дата написания", auto_now_add=True)
    moderation = models.BooleanField("Разрешено к публикации", default=False)


    def __str__(self):
        return "{}".format(self.post.title)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

