from django.contrib import admin
from .models import Question, Choice, SubmittedIP


# Register your models here.


# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Text", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    # 分页
    list_per_page = 50
    inlines = [ChoiceInline]
    # 默认情况下，Django 显示每个对象的 str() 返回的值。但有时如果我们能够显示单个字段，它会更有帮助。为此，使用 list_display 后台选项，它是一个包含要显示的字段名的元组，在更改列表页中以列的形式展示这个对象：


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(SubmittedIP)
