from django.shortcuts import render,redirect
from .forms import Uploadform
from .models import Uploader 






def upload_file(request):
	if request.method == 'POST':
		form = Uploadform(request.POST,request.FILES)
		if form.is_valid():
			newdoc = Uploader(filename = request.POST['filename'],docfile = request.FILES['docfile'])
			newdoc.save(form)
			return redirect('upload')

	else:
		form = Uploadform()
	return render(request, 'upload.html',{'form':form})

