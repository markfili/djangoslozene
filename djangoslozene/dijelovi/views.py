from django.http import HttpResponse, Http404 
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader

from dijelovi.models import Part, Supplier, PartComments

def index(request):
	return render(request, 'dijelovi/index.html')

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