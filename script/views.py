from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from script.forms import ScriptForm
from script.models import Script

import os
import sys

def main(request):
    return render(request, 'script/main.html')

@login_required(login_url='/user/login')
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

    # 여기서 쉘 실행
    #os.system("쉘스크립트이름.sh")


    return render(request, 'script/read.html',context)

def listGet(request):
    scripts = Script.objects.all().order_by('id')
    context = {'scripts' : scripts}
    return render(request, 'script/list.html',context)
