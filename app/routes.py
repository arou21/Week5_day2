from app import app
from flask import render_template, request, redirect, url_for
from .forms import PoknameForm
from .pok_API import get_pokemon


@app.route('/')
def homePage():
    people = ['name', "Brandt", "Aubrey","Nicole"]
    text = "SENDING THIS FROM PYTHON!!!"
    return render_template('index.html', people = people, my_text = text )



@app.route('/searchPage', methods=["GET", "POST"])
def searchPage():
    form = PoknameForm()
    pokname = ""
    print(request.method)
    if request.method == 'POST':
        if form.validate():
            pokname = form.pokname.data
    
            
            print(pokname)
            print('begin')
            name,ability, base_experience, image = get_pokemon(pokname)
            print('done')


            return render_template('search.html', form = form, name=name, ability=ability, base_experience=base_experience, image=image )


    return render_template('search.html', form = form )