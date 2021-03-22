# 外部文件创建数据

import os

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogproject.settings')
    import django

    django.setup()

    from blog.models import Tag, Category, Post
    from django.utils import timezone
    from django.contrib.auth.models import User

    user = User.objects.get(username='myuser')
    c = Category.objects.get(name='category test')

    p = Post(title='title test',body='body test',created_time = timezone.now(),modified_time = timezone.now(),category=c,author=user)
    p.save()

    # c = Category(name='category test')
    # c.save()
    #
    # t = Tag(name='tag test')
    # t.save()
