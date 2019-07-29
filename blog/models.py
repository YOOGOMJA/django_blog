from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')
    body = models.TextField()
    user = models.ManyToManyField(User, blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    def title_summary(self):
        if len(self.title) > 30:
            return self.title[:30] + '...'
        else:
            return self.title

class Comment(models.Model):
    writer = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField('Date published', auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

# 이미지 관리 모델
class Asset(models.Model):
    # 이미지를 업로드한 회원
    upload_user = models.ForeignKey(User , on_delete=models.CASCADE)
    # 이미지를 업로드한 게시글
    post = models.ForeignKey(Post , on_delete=models.CASCADE , default=None)
    # 업로드된 날짜
    upload_date = models.DateTimeField('Date published', auto_now=True)
    # 실제 이미지
    image = models.ImageField(blank=True , upload_to="blog/%y/%m/%d/%H%M%S")


