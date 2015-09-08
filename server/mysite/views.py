import pdb;
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404

from polls.models import Poll
from polls.zjuOCR import image2int
# Create your views here.

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

def info(request):
    
    response=HttpResponse()
    response['X-DJANGO'] = "It's the best."
    response['Access-Control-Allow-Origin']='*'
    response.write("<p>Here's another paragraph.</p>")
    return response
def runcode(request):
    code='0'
    #try:
    #pdb.set_trace()
    if 1:
        img = request.GET.get('img')
           
        #os.system('echo '+img+'>img.txt')
        
        code=image2int.OCR_Return_Verifycode(str(img))
    
    
        #output='code:%s'%code #+img+br+str(len(img))+br+str(type(img))
        
        
    #except:
        pass
    reTurnHttpResponse=HttpResponse()
    reTurnHttpResponse.write(code)
    reTurnHttpResponse['X-DJANGO'] = "It's the best."
    reTurnHttpResponse['Access-Control-Allow-Origin']='*'
    reTurnHttpResponse['Access-Control-Allow-Methods']='GET,POST,OPTIONS'
    reTurnHttpResponse['Access-Control-Allow-Headers']='X-Requested-With'
    return reTurnHttpResponse
    
    
    
    
	