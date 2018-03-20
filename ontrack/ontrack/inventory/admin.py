from django.contrib import admin

# Register your models here.


from .models import Feedback
 
 
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email', 'date', 'happy',)
    list_filter = ( 'date',)
    search_fields = ('details',)
 
    class Meta:
        model = Feedback
 
 
admin.site.register(Feedback, FeedbackAdmin)
