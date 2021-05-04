from django.shortcuts import render,redirect,get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import File,data
import json
from django.conf import settings

# Create your views here.

def upload(request):

    if request.method == 'POST':
        uploaded_file = request.FILES["file"]
        fs = FileSystemStorage()
        f = fs.save(uploaded_file.name,uploaded_file)

        fname = str(settings.BASE_DIR) + str(settings.MEDIA_URL) + f

        flag = 0

        with open(fname) as json_file:
            try:
                dataj = json.load(json_file)
            except Exception as e:
                flag = 1
        
        if flag:
            messages.info(request, "Invalid File type")
            fs1 = FileSystemStorage()
            fs1.delete(f)
        
        else:
            ch = ['userId','id','title','body']
            
            check = 0

            for d in dataj:
                if sorted(d.keys()) != sorted(ch):
                    check = 1
                    break
            
            if check:
                messages.info(request, "Invalid File content")
            else:
                for d in dataj:
                    dob = data.objects.create(userId=d['userId'], ids=d['id'],title=d['title'],body=d['body'])
                    dob.save()                    

                fl = File()
                fo = File.objects.create(js = f, user = request.user)
                fo.save()
                messages.info(request, "File uploaded")

        return render(request, 'upload.html')
    
    else:
        return render(request, 'upload.html')