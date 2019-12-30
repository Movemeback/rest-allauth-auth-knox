from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.db import models


class Question(models.Model):
    """
    Question model for storing all questions on the forum.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=124, verbose_name='Subject')
    body = models.TextField(validators=(MaxLengthValidator(50000),), verbose_name='Question')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    PUBLIC, TO_BE_APPROVED = 0, 1
    STATUSES = (
        (PUBLIC, 'Public'),
        (TO_BE_APPROVED, 'To be approved'),
    )
    status = models.PositiveSmallIntegerField(choices=STATUSES, default=PUBLIC)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    """
    Answer model for storing all answers to questions.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    body = models.TextField(validators=(MaxLengthValidator(50000),), verbose_name='Question')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
