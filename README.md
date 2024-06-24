# funny-funding-django

> 2024 Django 수행평가 &lt;퍼니펀딩> : 모의 크라우드 펀딩 서비스

# 가계부 (Household Account Book)

1. startproject funny_funding
   1. `python -m pip install django~=4.2`
   2. `django-admin startproject funny_funding .`
   3. File > Settings... > Language & Frameworks > Django > [v] Enable Django Support
   4. Run > Edit Configurations... > +Django Server > Name: runserver
   5. VCS > Enable Version Control Integration... > git > ok
3. startapp funfun
   1. `python manage.py startapp funfun`
   2. settings.py > INSTALLED_APPS > 'funfun',
4. funfun/
   1. models
      1. Category
         1. name, bgcolor
      2. AccountBook
         1. type(0: 지출, 1: 소비), price, category, time, contents, created_at, updated_at
         2. ~~photo~~
      3. `python manage.py makemigrations accountbook`
      4. `python manage.py migrate`
   2. admin
      1. Category
      2. AccountBook
      3. `python manage.py createsuperuser`
   3. views
      1. CategoryListView
      2. AccountBookListView
      3. AccountBookCreateView
      4. AccountBookUpdateView
      5. AccountBookDeleteView
   4. templates
      1. category_list.html
      2. accountbook_list.html
      3. accountbook_create.html
      4. accountbook_update.html
      5. accountbook_confirm_delete.html
   5. urls
      1. accountbook:category_list
      2. accountbook:accountbook_list
      3. accountbook:accountbook_create
      4. accountbook:accountbook_update
      5. accountbook:accountbook_delete


