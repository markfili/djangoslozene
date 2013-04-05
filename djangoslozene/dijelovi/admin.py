from django.contrib import admin
from dijelovi.models import Part, Supplier, PartComments, User, PartCategory

class CommentsOnParts(admin.TabularInline):
	model = PartComments
	extra = 1

class PartAdmin(admin.ModelAdmin):
    # fieldsets = [(Naziv polja, {'fields': ['vrijednost']}),]
        fieldsets = [
        		(None, {'fields': ['name']}),
        		('Part description', {'fields': ['year', 'supplier', 'date_added', 'part_num']}), # 'classes': ['collapse']}),
        		# ('Part comments'), {'fields': ['']}]
        ]
        inlines = [CommentsOnParts]
        list_display = ('name', 'part_num', 'date_added', 'was_added_recently')
        list_filter = ['date_added']
        search_fields = ['name', 'part_num']
admin.site.register(Part, PartAdmin)

class SupplierAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['name']}),
	]
	search_fields = ['name']

admin.site.register(Supplier, SupplierAdmin)

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['name']}),
    ]
    search_fields = ['name']
admin.site.register(User, UserAdmin)

class PartCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields' : ['name']}),
            ]
    search_fields = ['name']
admin.site.register(PartCategory, PartCategoryAdmin)
