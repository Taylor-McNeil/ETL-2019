<h1>Guide to the frontend</h1>
<p>In order to run the current version, you need to run these cmds.</p>

<code> Terminal 1

    cd Team4/
    pip install pipenv 
    pipenv shell 
    pipenv install django djangorestframework
    cd ETLFlex/
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
   
</code>

<hr

<code> Terminal 2
    
    cd Team4/
    npm install
    npm run dev

</code>

<hr

<code> File Structure 

    Team 4 (Contains our project)
        ETLFlex (Contain Django Project + Frontend)
            ETLFlex (django project settings)
                __init__.py
                settings.py
                urls.py
                wsgi.py
            frontend (django app also conatins React frontend)
                migrations (worthless)
                src (contains all the code for the frontend)
                    actions
                        rules.js (this is code for posting to the API)
                        types.js  
                    components (contains the pages for web app)
                        layout (each page will contain theses components)
                            Dashboard.js (contains Header and will be called on every other page except Landing)
                            Header.js
                        App.js (Where we load all components)
                        Home.js (Home page of web app after login in)
                        Landing.js (Where non-auth users will be redirected)
                        Rules.js (Page where user will add new rules)
                        RulesForm.js (Contains a form to add new columns / is called in Rules.js)
                    reducers (something to do with Redux)
                        index.js
                        rules.js
                    index.js (calls App.js)
                    store.js ( redux shit cba to explain )
                static (where we have css files and compile main.js for django)
                    css
                        bootstrap.min.css
                    main.js (when you run npm run dev it writes to this file)
                templates (holds our html file that calls loads main.js)
                ---- everything else in directory is configs -----
            rules (this dir is what allows us to send new rules to our djangorestframework)
                migrations (contains the format in which our data will be posted to API)
                only import .py files are:
                models.py   (contains the specification for each field ex. charField(max_length=100)
                serializers.py  (something about chaning to json format)
                urls.py     (just allows us to create a place called /api/rules/ where we also access the rules posted)
                views.py    (where our admin system will be placed)
                
                
        ------ Everything below are just config files for frontend and pipenv -----------
        /node_modules/ 
        .babelrc
        package.json (dependencies listed here)
        package-lock.json
        Pipfile
        Pipfile.lock
        webpack.config.js
    
</code>
