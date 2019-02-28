### Prerequisites

.env file to load environment variables. See example .env.defaults.

### Installing

1. Create a virtual environment
2. Install dependencies using pip install -r requirements.txt
3. Add a .env file using .env.defaults as a guide
4. Install Postgresql in your local Machine
	
	### Installation in Ubuntu

		- 	sudo apt update
		-	sudo apt install postgresql postgresql-contrib

	### Installation in Windows

		- https://www.postgresql.org/download 

		Follow that Link and Install the Postgesql by following all the steps and create the DB



5. Configure your database in settings.py as follow:

	DATABASES = {
    'default': {
        'ENGINE'        :   'django.db.backends.postgresql_psycopg2',
        'NAME'          :   'quizapp',
        'USER'          :   'admin',
        'PASSWORD'      :   'admin123',
        'HOST'          :   'localhost',
        'PORT'          :   '5432',
    }
}

6. Copy the Following Lines at the End of Your Settings.py File

	* STATIC_URL = '/static/'
	
	* MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
	* MEDIA_URL = '/media/'

		#django-crispy-forms
	* CRISPY_TEMPLATE_PACK = 'bootstrap4'
	* LOGIN_REDIRECT_URL = 'accounts:index'

	# ALL THIS NEXT STEPS ARE OPTIONAL, THE APP CAN STILL RUN WITHOUT THEM.
	
	*	EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
	*	EMAIL_HOST = 'smtp.gmail.com'
	* 	EMAIL_PORT = 587
	* 	EMAIL_USE_TLS = True

		# Create Enviroment Variable for this to work.
		# Go to the Link bellow and follow the instruction on Allowing your app to communicate with your account:  https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=13&cad=rja&uact=8&ved=2ahUKEwjssZbnmd7gAhXCz4UKHdu3A3EQFjAMegQICxAB&url=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&usg=AOvVaw1rVibBR6kQTiUjqa0l_f8W


	* EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
	* EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')

##  Authors.

- Jason OKOKA - 