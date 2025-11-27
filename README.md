# 24th_to_29th-november
Database and project start

                MONDAY
- Start with sql using maria database folder
- discussing crud operations (create,read, updata and delete)
- THE APPLYING USE OF DATA IN THE PROJECT. IN THE SETTING TO ACCESS
THE TEMPLATES CORRECTLY THE DIRS SHOLD NOT BE TEMPLATES ONLY BUT BASE_DIR TEMPLATES.
- INCLUDING MODELS FRUITS.
- NOW THIS TIME WE WILL INCLUDE THE CREATED AT AND THE UPDATED AT
- AFTER WORDS USE CLASS META FOR THE ORDERING OF THE TWO CREATED
- INCLUDING VIEWS FRUITS WITH AN IMPORTATION OF MODEL FRUITS
- YOU WILL NOTICE IT WILL APPERAR AT THE SITE
- ![img.png](img.png)
- ![img_1.png](img_1.png)
  - at first it will not work because we had not done the changes in the index but after doing the double calibrace 
  and inputing the fruits in the  personal htmml the changes will be seen in the web
  ''''
      class Fruits(models.Model):
          name = models.CharField(max_length=100)
          description = models.CharField()
          price = models.FloatField()
          created_at = models.DateField(auto_now_add=True)
          updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
            return self.name
''''

''''
        def two(request):
            fruits = Fruits.objects.all()
            # {"name" : "mango",
            #           "description" : "apple mango",
            #           "price" : 20.38}
            context = {"fruits" : fruits}
        
            return render(request, 'firstApp/personal.html', context)
''''

''''
         <div class="fs-6">{{ fruits }}</div>
''''

      finaly add the model to the admin file
''''
        admin.site.register(models.Fruits)

''''

-we start the crud operations
''''
    def createFruit(request):
            return render(request, )
    def readAllFruits(request):
        return render(request, )
    def readOneFruits(request):
        return render(request, )
    def update(request):
        return render(request, )
    def delete(request):
        return render(request, )
''''

-To handle operations go to the urls create the def of the operations
-go to the urls and create the paths with view of the same templates
this will be read on the data

- now we create the total readall page
- we go to the urls and add some information then to the vies add some information then finally to the 
page and add the information. the informations are below respectively
''''
path('readAll/', views.two, name='readAll'),

def readAllFruits(request):
    fruits = Fruits.objects.all()
    context = {"fruits" : fruits}
    return render(request, 'firstApp/personal.html', context )

    <div class="fs-6">{{ fruits }}</div>
    <div class="display-4"> {{fruit.name}} </div>
    <p class="lead"> {{fruit.description}}</p>
    <span class="badge bg-info"> ksh {{fruit.price}}</span>

''''

- next we create the readone page.
- start by creting a readone.html file then repeat the steps for read all
    ''''
        path('readOne/<str:pk>', views.two, name='readOne'),

  
def readOneFruits(request):
    fruits = Fruits.objects.get(id = pk)
    context = {"fruits" : fruits}
    return render(request, 'firstApp/fruitdetails.html.html', context )
        
    ''''

- pk stands for primary key
# next create a model form
- create a forms
- from djano.form import mmodeform
- form.models import fruit

-give a class and target the modl and the field
''''
class FruitsForm(ModelForm):
    class Meta:
        model = Fruits
        fields = '__all__'
''''

-update the view function to create the new record

- next in views go and check if th form is valid and redirect to th ehomepage
- adding  to test
- this is the end of the lesson


            TUESDAY
Create - Create Read Update Delete(CRUD) placeholder functions:
Preparing the functions to enable CRUD operarions
def createFruit(request):
    return render(request)

def readAllFruits(request):
    return render(request)

def readOneFruit(request):
    return render(request)

def updateFruit(request):
    return render(request)

def deletFruit(request):
    return render(request)

Update the urls.py with the routes:
from django.urls import path # helps us import the method path for our endpoints from . import views # import veiws from the current root directory

endpoints + target view functions:
```
    path('readAll', views.marketSector, name ='readAll'),
    path('readOne/<str:pk>', views.readOneFruit, name ='readOne'),

```
Create Data Operation:
Create a Form(ModelForm):

create a file under the app folder called forms.py
create model form:
from django.forms import ModelForm
from .models import Fruit

class FruitForm(ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__' # or target specific columns eg ['name', 'description', 'price]
navigate to urls.py and import the FruitForm, from .forms import FruitForm

update the view function to create the new record:

    def createFruit(request):
    form = FruitForm()
    context = {"form":form}

    if request.method == "POST":
        form = FruitForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("market")            

    return render(request, "firstApp/form.html", context )

create form.html:
    {% extends 'main.html' %}

    {% block content %}

    <div class="container my-5">
        <form action="" method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="submit">
        </form>
    </div>

    {% endblock %}

Read Data operations:
key important bits:

Fruit.objects.all(): fetched all the data under the Fruits tables
Fruit.objects.get(id=pk): fetched the fruit data where id was pk(primary key)
read all data from DB, update our views.py file:

def readAllFruits(request):
    fruits = Fruit.objects.all() # ORM helps us not write sQL syntax here => transalates to SELECT * FROM fruits;
    context = {"fruits":fruits}
    return render(request,"firstApp/market.html", context)

def readOneFruit(request,pk):
    fruit = Fruit.objects.get(id = pk)
    context ={"fruit":fruit}
    return render(request,"firstApp/fruit_details.html", context)
Update template( app level):
```
{% extends 'main.html' %}

{% block content %}

<div class="container my-5">
    <div class="display-3"> Welcome to the Market SPACE!! </div>
    <hr>
    <!-- <div class="fs-6"> {{ fruits }} </div> -->
    {% for fruit in fruits %}
        <div class="display-5">{{fruit.name}}</div>
        <p class="lead">{{fruit.description}}</p>
        <div class="badge bg-dark">ksh. {{fruit.price}}</div> 
    <hr>
    {% endfor %}
</div>

{% endblock %}
```
- In a short summary we have covered the read the create and the update part. 
Remaining part is the delete part which we will wind up tommorrow 
END OF TUESDAY

                WEDNESDAY
