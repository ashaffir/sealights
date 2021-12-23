from django.contrib import admin

from .models import Note, Report


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "created",
        "user",
        "content",
        "public",
    )

    ordered = ("-created",)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
    )

    ordered = ("-user",)
