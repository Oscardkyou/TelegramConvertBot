from django.contrib import admin
from .models import TelegramUser

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
  list_display = ["user_id", "username", "first_name", "last_name", "created_at", "admin"]
  lsit_filter = ["admin", "created_at"]
  search_fields = ["user_id", "username", "first_name", "last_name"]
  ordering = ["-created_at"]

