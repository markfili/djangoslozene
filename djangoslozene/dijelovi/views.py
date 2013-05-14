from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response
from django import forms
from datetime import datetime
import datetime
from django.utils.timezone import utc
import xlrd

from dijelovi.models import *


def index(request):
    list_category = PartCategory.objects.all()
    latest_part = Part.objects.latest('name')
    # next_part = Part.get_next_by_date_added(latest_part)
    part_by_date = Part.objects.order_by('-date_added')[:4]
    if request.method == 'POST' and request.POST['inquiry']:
        inquiry = request.POST['inquiry']
        if inquiry:
            part = Part.objects.filter(name__icontains=inquiry)
            part_category = PartCategory.objects.filter(name__icontains=inquiry)
            list_parts = list(part) + list(part_category)
            if list_parts:
                parts = list_parts
                inquiry_text = 'Trazili ste: %s' % inquiry
            else:
                inquiry_text = 'Nema rezultata za %s' % inquiry
                parts = '0'
        else:
            parts = ''
            inquiry_text = 'Niste unijeli trazeni pojam'
        return render(request, 'dijelovi/index.html',
                  {'list_category': list_category,
                   'latest_part': latest_part,
                   'part_by_date': part_by_date,
                   'parts': parts,
                   'inquiry_text': inquiry_text,})
    return render(request, 'dijelovi/index.html',
                  {'list_category': list_category,
                   'latest_part': latest_part,
                   'part_by_date': part_by_date,})



def supplier(request, supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    return render(request, 'dijelovi/supplier.html', {'supplier': supplier}) 

# def part(request):
# 	list_parts = Part.objects.all()
# 	template = loader.get_template('dijelovi/index.html')
# 	context = Context({
# 		'list_parts': list_parts,
# 		})
# 	return HttpResponse(template.render(context))

def part(request):
    list_parts = Part.objects.all()
    context = {'list_parts': list_parts}
    return render(request, 'dijelovi/parts.html', context)


def part_details(request, part_id):
# try:
# details = Part.objects.get(id=part_id)
    # except Part.DoesNotExist:
    # 	raise Http404
    details = get_object_or_404(Part, id=part_id)
    return render(request, 'dijelovi/details.html', {'details': details})


def part_comments(request, part_id):
    list_comments = PartComments.objects.filter(part_id=part_id)
    return render(request, 'dijelovi/comments.html', {'list_comments': list_comments})


def part_category(request, category_id):
    part_category = get_object_or_404(PartCategory, id=category_id)
    parts_in_category = Part.objects.filter(part_category_id=category_id)
    return render(request, 'dijelovi/category.html', 
                  {'part_category': part_category,
                   'parts_in_category': parts_in_category})


def read_excel(file):
    workbook = xlrd.open_workbook(file)
    worksheet = workbook.sheet_by_index(0)
    num_rows = worksheet.nrows - 1
    curr_row = 0
    # print curr_row
    # return curr_row
    while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)
        print row
        name = worksheet.cell_value(curr_row, 0)
        category = worksheet.cell_value(curr_row, 1)
        year = worksheet.cell_value(curr_row, 2)
        supplier = worksheet.cell_value(curr_row, 3)
        number = worksheet.cell_value(curr_row, 4)
        colour = worksheet.cell_value(curr_row, 5)
        state = worksheet.cell_value(curr_row, 6)
        manufacturer = worksheet.cell_value(curr_row, 7)
        price = worksheet.cell_value(curr_row, 8)
        s = Supplier.objects.get_or_create(name=supplier)
        s = Supplier.objects.get(name=supplier)
        pc = PartCategory.objects.get_or_create(name=category)
        pc = PartCategory.objects.get(name=category)
        m = PartManufacturer.objects.get_or_create(name=manufacturer)
        m = PartManufacturer.objects.get(name=manufacturer)
        print s, pc
        p = Part(name=name, year=year, supplier=s, part_category=pc, part_num=number,
                 date_added=datetime.datetime.utcnow().replace(tzinfo=utc), colour=colour, manufacturer=m, state=state, price=price)
        print p
        p.save()
        # return p


class UploadFileForm(forms.Form):
    file = forms.FileField()


def bulk_upload(request):
    if request.method == 'POST' and request.FILES:
        form = UploadFileForm(request.POST, request.FILES)
        print(request.FILES.items())
        if form.is_valid():
            # print('m')
            # print form.errors
            read_file = request.FILES['file'].name
            print read_file
            if '.xls' in read_file:
                print read_excel(read_file)
                status = 'success'
            else:
                status = 'not_xls'
            return render(request, 'dijelovi/upload_pricelist.html', RequestContext(request, {'status': status, 'form': form}))
        else:
            status = 'failed'
            return render(request, 'dijelovi/upload_pricelist.html', RequestContext(request, {'status': status, 'form': form}))
    else:
        status = ''
        return render(request, 'dijelovi/upload_pricelist.html')



def search(request):
    if request.POST and request.POST['inquiry']:
        inquiry = request.POST['inquiry']
        parts = Part.objects.filter(name__icontains=inquiry)
        part_category = PartCategory.objects.filter(name__icontains=inquiry)
        return render(request, 'dijelovi/index.html', {'parts': inquiry, 'result': inquiry})
    else:
        message = "Please submit search term"
        return HttpResponse(message)


@csrf_exempt
def gps(request):
    if request.method == "POST":
        mess = request.read()
        print mess
        return HttpResponse(200)
    else:
        return HttpResponse("nema")