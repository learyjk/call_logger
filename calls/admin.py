from django.contrib import admin
from .models import Call, Callee


class CallAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'caller', 'callee', 'notes')


class CalleeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')


admin.site.register(Call, CallAdmin)
admin.site.register(Callee, CalleeAdmin)
