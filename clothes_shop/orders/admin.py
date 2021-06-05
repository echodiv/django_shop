import csv
import datetime

from django.contrib import admin
from django.http import HttpResponse

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """
    Представление товаров в заказе для панели администрирования
    """
    model = OrderItem
    raw_id_fields = ['product']


def export_to_csv(modeladmin, request, queryset):
    """
    Создание CSV отчёта о совершенном заказе
    """
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
        opts.verbose_name
    )
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields()
              if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = 'Export to CSV'


def export_to_pdf(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(
        opts.verbose_name
    )

    data = [['Action Time', 'Priority', 'username', 'Source Address', 'Subject', 'Details']]
    for d in queryset.all():
        datetime_str = str(d.action_time).split('.')[0]
        item = [datetime_str, d.priority, d.username, d.source_address, d.subject, d.details]
        data.append(item)

    doc = SimpleDocTemplate(response, pagesize=(21*inch, 29*inch))
    elements = []

    table_data = Table(data)
    table_data.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                                    ("FONTSIZE",  (0, 0), (-1, -1), 13)]))
    elements.append(table_data)
    doc.build(elements)

    return response


export_to_pdf = 'Export to PDF'


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]


admin.site.register(Order, OrderAdmin)
