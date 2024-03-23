from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        return (
            timezone.now()
            >= self.pub_date
            >= timezone.now() - datetime.timedelta(days=1)
            # 计算了当前时间减去一天的时间间隔后的结果，即当前时间的前一天。
            # 又不大于当前实际
        )


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text


class SubmittedIP(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=45)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("question", "ip_address")
        # 在数据库层面，将检查确保每个 Question 对象和 ip_address 组合都是唯一的。这样可以确保同一个问题下的不同 IP 地址只能提交一次，而同一个 IP 地址在同一个问题下也只能提交一次。

    def __str__(self):
        return f"{self.ip_address} - {self.question}"


# 要在Django模型中建立多对一关系，你可以使用ForeignKey字段。默认情况下，ForeignKey会指向相关模型的主键（pk）。
# 但是，如果你想要指向相关模型的其他字段，你可以使用to_field参数。
