from django.shortcuts import render, redirect
from start.models import Die, DiceBag, Tray
from start.forms import DieCreationForm, BagCreationForm, TrayCreationForm

def welcome(request):
    return render(request, 'start/start.html', {})

def dice(request):
    search=request.GET.get('faces')
    if search:
        dice_list=Die.objects.filter(faces=search)
    else:
        dice_list=Die.objects.all()
    
    return render(request, 'start/die.html', {'dice_list':dice_list})

def dice_bag(request):
    search=request.GET.get('material')
    if search:
        bag_list=DiceBag.objects.filter(material=search)
    else:
        bag_list=DiceBag.objects.all()
    return render(request, 'start/dice_bag.html', {'bag_list':bag_list})

def tray(request):
    search=request.GET.get('color')
    if search:
        tray_list=Tray.objects.filter(color=search)
    else:
        tray_list=Tray.objects.all()
    return render(request, 'start/tray.html', {'tray_list':tray_list})

def make_dice(request):
    if request.method=='POST':
        form=DieCreationForm(request.POST)
        if form.is_valid():
            clean_info=form.cleaned_data
            
            style=clean_info.get('Estilo')
            faces=clean_info.get('Caras')
            numbering=clean_info.get('Numeros') 
            
            die=Die(style=style, faces=faces, numbering=numbering)
            die.save()
            return redirect('dice')
        else:
            return render(request, 'start/make_dice.html', {'form':form})
    form=DieCreationForm()
    return render(request, 'start/make_dice.html', {'form':form})

def make_bag(request):
    if request.method=='POST':
        form=BagCreationForm(request.POST)
        if form.is_valid():
            clean_info=form.cleaned_data
            
            material=clean_info.get('Material')
            capacity=clean_info.get('Capacidad')
            color=clean_info.get('Color') 
            
            bag=DiceBag(material=material, color=color, capacity=capacity)
            bag.save()
            return redirect('bags')
        else:
            return render(request, 'start/make_bag.html', {'form':form})
    form=BagCreationForm()
    return render(request, 'start/make_bag.html', {'form':form})

def make_tray(request):
    if request.method=='POST':
        form=TrayCreationForm(request.POST)
        if form.is_valid():
            clean_info=form.cleaned_data
            
            material=clean_info.get('Material')
            size=clean_info.get('Tamaño')
            color=clean_info.get('Color') 
            
            tray=Tray(material=material, size=size, color=color)
            tray.save()
            return redirect('trays')
        else:
            return render(request, 'start/make_tray.html', {'form':form})
    form=TrayCreationForm()
    return render(request, 'start/make_tray.html', {'form':form})