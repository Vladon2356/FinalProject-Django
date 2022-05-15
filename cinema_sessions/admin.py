from django.contrib import admin
from cinema_sessions.models import Sessions, Tickets


class SessionsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "movie",
        "hall",
        "date",
        "start_at",
        "end_at",
        "ticket_price",
        "is_active",
    )
    list_display_links = ("id", "movie", "hall", "date", "ticket_price")
    search_fields = ("movie", "hall", "date", "start_at", "end_at", "ticket_price")
    list_filter = ("movie", "hall")
    list_editable = ("is_active",)


class TicketsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "session",
        "owner",
        "row",
        "column",
        "sold",
        "ticket_price",
        "is_active",
    )
    list_display_links = ("id",)
    search_fields = ("id", "session", "owner", "sold", "ticket_price", "is_active")
    list_filter = ("session", "sold")
    list_editable = ("is_active",)


admin.site.register(Sessions, SessionsAdmin)
admin.site.register(Tickets, TicketsAdmin)
