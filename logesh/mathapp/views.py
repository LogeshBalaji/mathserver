from django.shortcuts import render 
def powerofbulb(request): 
    context={} 
    context['power'] = "0" 
    context['i'] = "0" 
    context['r'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        i = request.POST.get('I','0')
        r = request.POST.get('R','0')
        print('request=',request) 
        print('Intensity=',i) 
        print('Resistance=',r) 
        power = (int(i) ** 2)*int(r) 
        context['power'] = power 
        context['i'] = i
        context['r'] = r
        print('power=',power) 
    return render(request,'mathapp/math.html',context)

# Create your views here.
