from django.contrib import admin
from .models import Question, Choice, User, UserProfileInfo

admin.site.site_header = "Admin"
admin.site.site_title = "Welcome to Admin Area"
admin.site.index_title = "Welcome to the Admin Area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter =  ['pub_date']


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserProfileInfo)
