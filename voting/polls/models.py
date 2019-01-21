from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    public_key_x_0 = models.CharField(max_length=150, blank=True, null=True)
    public_key_y_0 = models.CharField(max_length=150, blank=True, null=True)
    private_key_0 = models.CharField(max_length=150, blank=True, null=True)
    public_key_x_1 = models.CharField(max_length=150, blank=True, null=True)
    public_key_y_1 = models.CharField(max_length=150, blank=True, null=True)
    private_key_1 = models.CharField(max_length=150, blank=True, null=True)
    ciphered_answer_0 = models.CharField(max_length=300, blank=True, null=True)
    ciphered_answer_1 = models.CharField(max_length=300, blank=True, null=True)
    chosen_answer = models.CharField(max_length=300, blank=True, null=True)
    chosen_key = models.CharField(max_length=150, blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)

class Vote(models.Model):
    question = models.ForeignKey(Question, models.DO_NOTHING, null=True)
    ciphered_answer = models.CharField(max_length=300, blank=True, null=True)
    public_key_x = models.CharField(max_length=150, blank=True, null=True)
    public_key_y = models.CharField(max_length=150, blank=True, null=True)
    private_key = models.CharField(max_length=150, blank=True, null=True)

class Receipt(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, null=True)
    chosen_answer = models.CharField(max_length=300, blank=True, null=True)

class ChosenDigits(models.Model):
    question = models.ForeignKey(Question, models.DO_NOTHING)
    Choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, null=True)
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, null=True)
    public_key_x = models.CharField(max_length=150, blank=True, null=True)
    public_key_y = models.CharField(max_length=150, blank=True, null=True)
    private_key = models.CharField(max_length=150, blank=True, null=True)
    chosen_answer = models.CharField(max_length=300, blank=True, null=True)