from . models import *
from . views import *



def count(requst):
    item_count=0
    if 'admin' in requst.path:
        return {}
    else:
        try:
            ct=cartlist.objects.filter(cart_id=c_id(requst))
            cti=items.objects.all().filter(cart=ct[:1])
            for c in cti:
                item_count +=c.quan
        
        except cartlist.DoesNotExist:
            item_count=0   
        
        return dict(itc=item_count)
