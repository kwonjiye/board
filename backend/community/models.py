from django.utils import timezone
from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField


# # Create your models here.
# class Event(models.Model):
#     description=RichTextField()


# class Category(models.Models):
#     name=models.CharField(max_length=50, help_text="블로그 글의 분류를 입력하세요.(ex:일상)")

#     def __str__(self):
#         return self.name


# class Profile(models.Model):

#     like_posts = models.ManyToManyField('Post', blank=True, related_name='like_users')

#     def __str__(self):
#         return self.nickname

class Board(models.Model):
    """
    title: 제목
    content: 내용
    author: 작성자
    like_count: 좋아요 카운트
    pub_date: 배포일
    """

    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    like_count = models.PositiveIntegerField(default=0)
    pub_date = models.DateTimeField()
    update_counter = models.PositiveIntegerField(default=0)
    # category=models.ManyToManyField(Category, help_text="글의 분류를 설정하세요,")

    def __str__(self):
        return self.title

    def click(self):
        self.update_counter += 1
        self.save()


class Reply(models.Model):
    reply = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    rep_date = models.DateTimeField()

    def __str__(self):
        return self.comment


id = models.AutoField(primary_key=True)


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    like_count = models.PositiveIntegerField(default=0)
    pub_date = models.DateTimeField()
    update_counter = models.PositiveIntegerField(default=0)
    # n_hit = models.PositiveIntegerField(default=0)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title

    def click(self):
        self.update_counter += 1
        self.save()
    # def update_counter(self):
    #     self.n_hit = self.n_hit + 1
    #     self.save()

    # def update_counter(self):
    #     self.post_hit=self.post_hit+1
    #     self.save()

# class Notices(models.Model):
#     objects= models.Manager()
#     n_title = models.CharField(max_length=100)
#     n_body = models.TextField()
#
#     n_input_date = models.DateTimeField('date published', default=timezone.now)

#     def __str__(self):
#         return self.n_title

#     @property
# #

# class Memo(models.Model):
#     content=models.TextField()
