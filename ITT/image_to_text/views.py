from django.shortcuts import render
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import os
from PIL import Image
from .forms import ImageForm

def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = Image.open(request.FILES['image'])
            img.convert('RGB')
            text = tess.image_to_string(img)
            context = {'text': text}
            return render(request, 'index.html', context)
    else:
        form = ImageForm()

    context = {'form': form}
    return render(request, 'index.html', context)