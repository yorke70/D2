from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('post_rating'))
        pRat = 0
        if postRat.get('postRating'): pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.author_rating = pRat * 3 + cRat
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    news = 'NW'
    post = 'PT'

    POSITIONS = [
        (news, 'Новость'),
        (post, 'Статья')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    choice = models.CharField(max_length=2,
                              choices=POSITIONS,
                              default=post)
    time_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    post_name = models.CharField(max_length=255)
    text = models.TextField()
    post_rating = models.IntegerField(default=0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[:124]} ... Рейтинг {self.post_rating}'

    def __str__(self):
        return f'{self.text}\n' \
               f'Рейтинг статьи: {self.post_rating}\n' \
               f'Автор: {self.author.authorUser}'

class PostCategory(models.Model):
    post_name = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


