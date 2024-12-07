# Ex.05 Design a Website for Server Side Processing
# Date:
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
math.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Power Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            background-color: white;
            max-width: 600px;
            margin: 50px auto;
            padding: 30px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        label {
            font-size: 16px;
            margin-bottom: 8px;
            display: block;
        }
        input[type="number"] {
            width: 100%;
            padding: 8px;
            margin: 10px 0 20px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 4px;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Power Calculator for Lamp Filament</h1>
        <form align="center" method="POST">
            {% csrf_token %}
            Intensity <input name="I" value="{{i}}">
            <br>
            <br>
            Resistance <input name="R" value="{{r}}">
            <br>
            <br>
            <input type="submit" value="calculate">
            <br>
            <br>
            Power <input name="power"value={{power}}>
        </form>
    </div>

</body>
</html>
```
views.py
```
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
```
urls.py
```
from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('powerofbulb/',views.powerofbulb,name="powerofbulb"),
    path('',views.powerofbulb,name="powerofbulbroot")
]
```
# SERVER SIDE PROCESSING:
![alt text](<Screenshot 2024-12-07 114006.png>)
# HOMEPAGE:
![Screenshot 2024-12-07 113952](https://github.com/user-attachments/assets/788f160b-5d58-4aab-aedd-6579971598f9)

# RESULT:
The program for performing server side processing is completed successfully.
