from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages

import receipes
from .models import Recipe, Ingredients

# Create your views here.
def add_recipe(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                body = request.POST
                if 'recipe_name' in body and 'description' in body:
                    recipe_name = body['recipe_name']
                    description = body['description']
                    image = request.FILES.get('image')
                    video = request.FILES.get('video')
                    preparation_time = body['preparation_time']
                    ingredient_names = body.getlist('ingredient_name')
                    ingredient_amounts = body.getlist('ingredient_amount')

                    if image:
                        if image.size > 1*1024*1024 :
                            raise Exception('Image size should be less than 1MB')
                                
                    recipe_obj = Recipe.objects.create(recipe_name=recipe_name, description=description,image=image,
                                                       video=video,preparation_time=preparation_time,user=request.user)
                    if recipe_obj:
                        for name, amount in zip(ingredient_names, ingredient_amounts):
                            ingredient_obj = Ingredients.objects.create(recipe= recipe_obj, ingredient_name=name, amount=amount)
                            
                        messages.success(request, 'Recipe Added successfully')
                        return redirect('receipes:add_recipe')
                        
                    else:
                        raise Exception('There is some problem in adding recipe ')
                    
                else:
                    raise Exception('Provide sufficient details')
                        
            
            except Exception as e:
                print(e)
                messages.warning(request,str(e))
                return redirect('receipes:add_recipe')
        
        return render(request, 'recipes/addrecipe.html')
    
    else:
        messages.warning(request,'You must be logged in to access this page.')
        return redirect('accounts:login')
    
def get_recipe(request,slug):
    try:
        recipe = Recipe.objects.filter(slug=slug).first()
        context = {'recipe':recipe}
        return render(request,'recipes/recipe.html',context)
    
    except Exception as e:
        print(e)