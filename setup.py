from setuptools import setup, find_packages

setup(

      name='Matplus',
      version='1.0',
      description='matplus dependency',
      author='Matplus',
      author_email='',
      scripts=['manage.py'],
      packages=find_packages(),
      install_requires=[
        'Django==4.2.9',
        'django-autoslug==1.9.9',
        'django-editorjs==0.2.1',
        'django-editorjs-fields==0.2.7',
        'django-extensions==3.2.3',
        'django-modeltranslation==0.18.11',
        'django-quill-editor==0.1.40',
        'django-taggit==5.0.1',
        'pillow==10.2.0',
        'python-dotenv==1.0.0',
        'sqlparse==0.4.4',
        'typing-extensions==4.9.0',
        'gunicorn==21.2.0',
    ],

    )
