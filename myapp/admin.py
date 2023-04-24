from django.contrib import admin

# Register your models here.
from .models import Komentar, Betara
# Register your models here.

class BetaraAdmin(admin.ModelAdmin):
    '''Admin View for Product'''
    def change_category_to_default(self,request,queryset):
        queryset.update(catagory="dafault")
        
    change_category_to_default.short_description = 'Default category' #untuk memendekkan function
    
    list_display = ('nomor','nama', 'penjelasan',)
    # list_filter = ('',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('title','catagory',) #untuk membuat cari di admin panel
    # date_hierarchy = ''
    # ordering = ('',)
    # actions = ('change_category_to_default',)
    # fields = ('title','price',) # saat buka objectnya hanya menampilkan 2 field terdaftar
    # list_editable = ('price',) # untuk dapat mengedit di list
admin.site.register(Komentar)
admin.site.register(Betara, BetaraAdmin)