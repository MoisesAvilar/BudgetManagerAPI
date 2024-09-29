from django.contrib import admin
from planner.models import Planner


@admin.register(Planner)
class PlannerAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "description",
        "category",
        "spending_target",
        "total_items",
        "created_at",
        "updated_at",
    )
    model = Planner
