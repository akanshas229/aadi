from django.contrib import admin
from .models import User, AuthToken, UserActivity, PasswordResetToken
# Register your models here.

admin.site.register(User)
admin.site.register(AuthToken)
admin.site.register(UserActivity)
admin.site.register(PasswordResetToken)