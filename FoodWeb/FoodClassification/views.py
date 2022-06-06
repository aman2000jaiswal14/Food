from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image as pillow
import numpy as np
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
# Create your views here.


from .forms import ImageForms
from .models import Image

def index(request):
    return HttpResponse("Food Classification Index Page")




def uploadimagepage(request):

    return render(request,'FoodClassification/getimage.html',{'form':ImageForms()})

from datetime import datetime
def uploadedimage(request):

    if(request.method=='POST' ):
        print(request)
        print(request.FILES['img'])
        form = ImageForms(request.POST, request.FILES)
        print(form,"true")
        if(form.is_valid()):
            img = form.cleaned_data.get("img")
            key =len(Image.objects.all())+1
            obj =Image.objects.create(imgid=key,img = img)
            newimg = pillow.open(obj.img.path)

            tofit = newimg.resize((224,224))
            print(tofit.size)
            tofit.thumbnail((300, 300))
            print(tofit.size)
            tofit = np.array(tofit)
            print(tofit.shape)
            tofit = tofit/255.
            tofit = np.expand_dims(tofit, axis=0)

            newimg.thumbnail((300,300))
            print(obj.img.width)
            obj.save()
            newimg.save(obj.img.path)
            # print(obj.img.url)
            ans = {0: "Spring Roll", 1: "Samosa", 2: "Pizza", 3: " Fried Rice", 4: "Burger"}
            tfmodel = tf.keras.models.load_model('FoodClassification/vggmodelweight.h5')


            output = list(tfmodel.predict(tofit)[0])
            output = output.index(max(output))
            output = ans[output]

            print(output)

        return render(request,'FoodClassification/showclass.html',{'file_url':obj.img.url,'foodname' : output})
        # return HttpResponse("file Uploaded")
    else:
        return HttpResponse('File Not Uploaded')
