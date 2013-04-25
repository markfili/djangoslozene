from dijelovi.models import Supplier

def supp():
    for s in Supplier.objects.all():
        if(s.name=="Novi"):
            print s.name
        else:
            print "nema"