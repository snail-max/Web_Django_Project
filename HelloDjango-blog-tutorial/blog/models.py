from django.db import models
from django.contrib.auth.models import User


# 分类
class Category(models.Model):
    name = models.CharField(max_length=100)


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100)


# 文章
class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文
    body = models.TextField()

    # 文章创建时间，最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要(charField默认必须存有数据，，摘要可以为空，所以要设置默认blank=True)
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)