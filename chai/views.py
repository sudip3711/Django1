from django.shortcuts import render
from .models import ChaiFirstModel
from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(req):
    chais = ChaiFirstModel.objects.all()
    return render(req,'all_chai.html',{'chais': chais})

def chai_desc(req,chaiId):
    chai = get_object_or_404(ChaiFirstModel,pk=chaiId)
    return render(req,'chai_detail.html',{'chai': chai})
