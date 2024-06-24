from django.db import models


class User(models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.email} {self.password} {self.nickname} {self.created_at} {self.updated_at}'


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    target_num = models.IntegerField()
    start_period = models.DateTimeField(auto_now_add=True)
    end_period = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} {self.name} {self.description} {self.price} {self.target_num} {self.start_period} {self.end_period} {self.created_at} {self.updated_at}'


class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.user} {self.item} {self.amount}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.user} {self.item} {self.content}'

class Category(models.Model):
    category = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.category}'