from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django import forms
import xlrd

from dijelovi.models import Part, Supplier, PartComments, PartCategory

def index(request):
    list_category = PartCategory.objects.all()
    latest_part = Part.objects.latest('name')
    next_part = Part.get_next_by_date_added(latest_part)
    part_by_date = Part.objects.order_by('-date_added')[:6]
    return render(request, 'dijelovi/index.html',
                  {'list_category': list_category,
                   'latest_part': latest_part,
                   'part_next_by_date_added': next_part,
                   'part_by_date': part_by_date })

def supplier(request):
    list_names = Supplier.objects.order_by('name')
    output = ', '.join(p.name for p in list_names)
    return HttpResponse(output)

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
    worksheet = workbook.sheet_by_name('Sheet1')
    num_rows = worksheet.nrows - 1
    curr_row = 0
    while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)
        print row
        name = worksheet.cell_value(row, 0)
        category = worksheet.cell_value(row, 1)
        year = worksheet.cell_value(row, 2)
        supplier = worksheet.cell_value(row, 3)
        number = worksheet.cell_value(row, 4)
        s = Supplier(name=supplier)
        pc = PartCategory(name=category)
        p = Part(name=name, year=year, supplier=s, part_category=pc, part_number=number)
        p.save()



class UploadFileForm(forms.Form):
    file = forms.FileField()

def bulk_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(request.FILES.items())
        if form.is_valid():
            # print('m')
            # print form.errors
            read_file = request.FILES['file'].name
            read_excel(read_file)
            return HttpResponseRedirect('/dijelovi/part')
        else:
         	form = UploadFileForm()
        return render_to_response('dijelovi/failed.html', RequestContext(request, {'form' : form}))

def search(request):
	if request.POST and request.POST['inquiry']:
		inquiry = request.POST['inquiry']
		parts = Part.objects.filter(name__icontains=inquiry)
		return render(request, 'dijelovi/index.html', {'parts': parts, 'inquiry': inquiry})
	else:
		message = "Please submit search term"
		return HttpResponse(message)

