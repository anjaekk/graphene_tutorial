SECRET_KEY = 'django-insecure-38tknk2kve)n*f-4i&(2pa^wwwvl=7&)ju(0)=kc6z0n7d#vdl'

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'graphqltutorial',
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': '3306',
	'OPTIONS': {'charset': 'utf8mb4'}
    }
}
