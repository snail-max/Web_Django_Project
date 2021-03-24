from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# 分类
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Post(models.Model):
    # 文章标题
    title = models.CharField('标题', max_length=70)
    # 文章正文
    body = models.TextField('正文')

    # 文章创建时间，最后一次修改时间
    created_time = models.DateTimeField('创建时间',default=timezone.now())
    modified_time = models.DateTimeField('修改时间')

    # 文章摘要(charField默认必须存有数据，，摘要可以为空，所以要设置默认blank=True)
    excerpt = models.CharField('摘要', max_length=200, blank=True)

    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)

    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def save(self, *args,**kwargs):
        self.modified_time = timezone.now()
        super().save(*args,**kwargs)
