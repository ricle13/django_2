from django.db import models
from django.urls import reverse

class Author(models.Model):
    author_rating = models.IntegerField(default = 0)

    user = models.OneToOneField('auth.User', on_delete = models.CASCADE)

    def update_rating(self):
        posts = Post.objects.filter(author = self.pk)
        comments = Comment.objects.filter(user = self.pk)
        auhor_rating = 0
        comment_rating = 0
        post_comm_rating = 0
        for post in posts:
            post_comms = Comment.objects.filter(post = post.pk)
            for com in post_comms:
                if com.pk != self.pk:
                    post_comm_rating += com.comment_rating
            auhor_rating += post.post_rating * 3
        for com in comments:
            comment_rating += com.comment_rating
        self.author_rating = auhor_rating + comment_rating + post_comm_rating
        self.save()

class Category(models.Model):
    category_name = models.CharField(max_length = 32, unique = True)

articles = 'articles'
news = 'news'
chois = [(articles, 'Статья'), (news, 'Новость')]

class Post(models.Model):
    post_var = models.CharField(max_length = 8, choices = chois, default = articles)
    post_time = models.DateTimeField(auto_now_add = True)
    header = models.CharField(max_length = 64)
    text = models.TextField()
    post_rating = models.IntegerField(default = 0)

    author = models.ForeignKey('Author', on_delete = models.CASCADE)
    category = models.ManyToManyField('Category', through = 'PostCategory')
    def get_absolute_url(self):
        print(self.id)
        return reverse('news_detail', args=[self.post_var, str(self.id)])
    def preview(self):
        prev = self.text[0:125] + '...'
        return prev
    def like(self):
        self.post_rating += 1
        self.save()
    def dislike(self):
        self.post_rating -= 1
        self.save()
    

class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete = models.CASCADE)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete = models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    text = models.CharField(max_length = 248)
    post_time = models.DateTimeField(auto_now_add = True)
    comment_rating = models.IntegerField(default = 0)
    def like(self):
        self.comment_rating += 1
        self.save()
    def dislike(self):
        self.comment_rating -= 1
        self.save()