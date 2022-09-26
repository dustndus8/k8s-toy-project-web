from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from script.forms import ScriptForm
from script.models import Script


def createScript(request):
    if request.method == "GET":
        scriptForm = ScriptForm(request.POST)
        context = {'scriptForm' : scriptForm}
        return render(request, 'script/create.html',context)
    if request.method == "POST":
        scriptForm = ScriptForm(request.POST)
        if scriptForm.is_valid():
            script = scriptForm.save(commit=False)
            script.save()

        return redirect('/script/readGet/'+str(script.id))


    return render(request, 'script/create.html')

def readScriptGet(request,sid):
    script = Script.objects.get(Q(id=sid))
    context = {
        'script' : script
    }

    return render(request, 'script/read.html',context)

