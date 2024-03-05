from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Tweet(models.Model):
    associated_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)
    email_notified = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class SearchTerm(models.Model):
    associated_user = models.ForeignKey(User, on_delete=models.CASCADE)
    term = models.CharField(max_length=50)

    def __str__(self):
        return self.associated_user.__str__() + ": " + self.term