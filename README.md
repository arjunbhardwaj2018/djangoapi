while development and to run this project, we did some commands
Terminal 1
[18/Feb/2026 20:47:26] "GET /static/admin/css/responsive.css HTTP/1.1" 304 0
[18/Feb/2026 20:47:26] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 304 0
[18/Feb/2026 20:47:26] "GET /static/admin/css/base.css HTTP/1.1" 304 0
[18/Feb/2026 20:47:26] "GET /static/admin/js/theme.js HTTP/1.1" 304 0
[18/Feb/2026 20:47:26] "GET /static/admin/css/dark_mode.css HTTP/1.1" 304 0
[18/Feb/2026 20:47:26] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 441
[18/Feb/2026 20:47:26] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 304 0
[18/Feb/2026 20:47:26] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
[18/Feb/2026 20:47:26] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
[18/Feb/2026 20:47:45] "GET /admin/auth/user/ HTTP/1.1" 200 10452
[18/Feb/2026 20:47:45] "GET /static/admin/css/changelists.css HTTP/1.1" 200 6566
[18/Feb/2026 20:47:45] "GET /static/admin/js/jquery.init.js HTTP/1.1" 200 347
[18/Feb/2026 20:47:45] "GET /static/admin/js/core.js HTTP/1.1" 200 5682
[18/Feb/2026 20:47:45] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 200 8943
[18/Feb/2026 20:47:45] "GET /static/admin/js/urlify.js HTTP/1.1" 200 7887
[18/Feb/2026 20:47:45] "GET /static/admin/js/prepopulate.js HTTP/1.1" 200 1531
[18/Feb/2026 20:47:45] "GET /static/admin/js/actions.js HTTP/1.1" 200 7872
[18/Feb/2026 20:47:45] "GET /admin/jsi18n/ HTTP/1.1" 200 3343
[18/Feb/2026 20:47:45] "GET /static/admin/img/icon-yes.svg HTTP/1.1" 200 436
[18/Feb/2026 20:47:45] "GET /static/admin/img/search.svg HTTP/1.1" 200 458
[18/Feb/2026 20:47:45] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 200 292458
[18/Feb/2026 20:47:45] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 200 232381
[18/Feb/2026 20:47:45] "GET /static/admin/js/filters.js HTTP/1.1" 200 978
[18/Feb/2026 20:47:45] "GET /static/admin/img/sorting-icons.svg HTTP/1.1" 200 1097
[18/Feb/2026 20:47:45] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 200 331
/Users/arjunbhardwaj/practice/djangoRestApi/djangoapi/djangoapi/urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 18, 2026 - 20:58:19
Django version 4.2.28, using settings 'djangoapi.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

/Users/arjunbhardwaj/practice/djangoRestApi/djangoapi/courses/urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 18, 2026 - 20:58:20
Django version 4.2.28, using settings 'djangoapi.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

^C%                                                                                                                                                                                                       
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % 
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % 
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % python3 manage.py makemigrations
No changes detected
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % python3 manage.py makemigrations
No changes detected
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % python manage.py makemigrations 
No changes detected
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  No migrations to apply.
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % deactivate 
arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % source venv/bin/activate              
source: no such file or directory: venv/bin/activate
arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % cd ..
arjunbhardwaj@Arjuns-MacBook-Pro djangoRestApi % source venv/bin/activate
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoRestApi % cd ..
(venv) arjunbhardwaj@Arjuns-MacBook-Pro practice % source venv/bin/activate
source: no such file or directory: venv/bin/activate
(venv) arjunbhardwaj@Arjuns-MacBook-Pro practice % cd django
(venv) arjunbhardwaj@Arjuns-MacBook-Pro django % ls
readme.txt      storefront
(venv) arjunbhardwaj@Arjuns-MacBook-Pro django % cd ..
(venv) arjunbhardwaj@Arjuns-MacBook-Pro practice % ls
django          djangoRestApi
(venv) arjunbhardwaj@Arjuns-MacBook-Pro practice % cd djangoRestApi 
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoRestApi % ls
djangoapi       venv
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoRestApi % cd djangoapi 
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % ls
courses         db.sqlite3      djangoapi       manage.py
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % cd djangoapi 
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % ls
__init__.py     asgi.py         settings.py     urls.py         wsgi.py
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % cd ..
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % ls
courses         db.sqlite3      djangoapi       manage.py
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 18, 2026 - 21:14:17
Django version 4.2.28, using settings 'djangoapi.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

[18/Feb/2026 21:14:19] "GET / HTTP/1.1" 200 10664
[18/Feb/2026 21:14:33] "GET /admin/ HTTP/1.1" 200 5556
[18/Feb/2026 21:14:33] "GET /static/admin/css/base.css HTTP/1.1" 304 0
[18/Feb/2026 21:14:33] "GET /static/admin/css/dark_mode.css HTTP/1.1" 304 0
[18/Feb/2026 21:14:33] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 304 0
[18/Feb/2026 21:14:33] "GET /static/admin/css/dashboard.css HTTP/1.1" 304 0
[18/Feb/2026 21:14:33] "GET /static/admin/css/responsive.css HTTP/1.1" 304 0
[18/Feb/2026 21:14:33] "GET /static/admin/js/theme.js HTTP/1.1" 304 0
[18/Feb/2026 21:14:33] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 304 0
[18/Feb/2026 21:14:33] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 304 0
[18/Feb/2026 21:14:33] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 304 0
Not Found: /plugins/asset-index/rdmacluster/1/
[18/Feb/2026 21:58:57] "GET /plugins/asset-index/rdmacluster/1/ HTTP/1.1" 404 2182
Not Found: /apple-touch-icon-precomposed.png
[18/Feb/2026 21:58:57] "GET /apple-touch-icon-precomposed.png HTTP/1.1" 404 2176
Not Found: /favicon.ico
[18/Feb/2026 21:58:57] "GET /favicon.ico HTTP/1.1" 404 2113
Not Found: /apple-touch-icon.png
[18/Feb/2026 21:58:57] "GET /apple-touch-icon.png HTTP/1.1" 404 2140
[18/Feb/2026 22:14:02,814] - Broken pipe from ('127.0.0.1', 51341)
Not Found: /plugins/asset-index/rdmacluster/1/
[19/Feb/2026 06:34:10] "GET /plugins/asset-index/rdmacluster/1/ HTTP/1.1" 404 2182
Not Found: /plugins/asset-index/rdmacluster/1/
[19/Feb/2026 06:34:11] "GET /plugins/asset-index/rdmacluster/1/ HTTP/1.1" 404 2182
[19/Feb/2026 06:34:23] "GET / HTTP/1.1" 200 10664
^C%                                                                                                                                                                         
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % 
 *  History restored 

arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % source /Users/arjunbhardwaj/practic
e/djangoRestApi/venv/bin/activate
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % 

========================================================================================================================================
Terminal 2

id_ed25519                      id_ed25519_new_personal.pub     known_hosts
(venv) arjunbhardwaj@Arjuns-MacBook-Pro .ssh % ls -lhrt
total 56
-rw-------  1 arjunbhardwaj  staff   444B Dec  9 17:42 id_ed25519
-rw-r--r--  1 arjunbhardwaj  staff   120B Dec  9 17:42 id_ed25519.pub
-rw-r--r--  1 arjunbhardwaj  staff   176B Feb  3 11:58 known_hosts.old
-rw-------  1 arjunbhardwaj  staff   668B Feb  3 11:59 known_hosts
-rw-r--r--  1 arjunbhardwaj  staff   327B Feb 10 11:44 config
-rw-------@ 1 arjunbhardwaj  staff   419B Feb 19 16:26 id_ed25519_new_personal
-rw-r--r--@ 1 arjunbhardwaj  staff   109B Feb 19 16:26 id_ed25519_new_personal.pub
(venv) arjunbhardwaj@Arjuns-MacBook-Pro .ssh % cat id_ed25519_new_personal.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDmDMuiSx5ZVDltJNvuRSnbGcBnke3cbMVn86FHYt/Hq arjunbhardwaj2018@gmail.com
(venv) arjunbhardwaj@Arjuns-MacBook-Pro .ssh % 
(venv) arjunbhardwaj@Arjuns-MacBook-Pro .ssh % 
(venv) arjunbhardwaj@Arjuns-MacBook-Pro .ssh % 
(venv) arjunbhardwaj@Arjuns-MacBook-Pro .ssh % cd
(venv) arjunbhardwaj@Arjuns-MacBook-Pro ~ % ls
22jan_netbox.diff                                       netbox__init__bkp.py
22jan.diff                                              pi_changes_local
Applications                                            Pictures
asset_index_data                                        platform-inventory
asset-index                                             Postman
asset-index_bkp                                         practice
Cisco Packet Tracer 9.0.0                               pre_prod
cron_preprod.log                                        pre_prod_ims_netbox_differentiator_working_setup
cron_prod.log                                           prod
dcim-helm-deploy                                        Public
description_changes.diff                                run_netbox_preprod.sh
Desktop                                                 run_netbox_prod.sh
Documents                                               system-bringup-queue
Downloads                                               system-bringup-release
dump.rdb                                                temp
ims_netbox_differentiator_working_setup                 temp_data
Library                                                 temp1.diff
migrations_copy                                         test_cron.log
Movies                                                  Workspace_server_diff
Music                                                   Workspace1
netbox
(venv) arjunbhardwaj@Arjuns-MacBook-Pro ~ % cd practice 
(venv) arjunbhardwaj@Arjuns-MacBook-Pro practice % ls
django          djangoRestApi
(venv) arjunbhardwaj@Arjuns-MacBook-Pro practice % cd djangoRestApi 
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoRestApi % ls
djangoapi       venv
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoRestApi % cd djangoapi 
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   courses/__init__.py
        new file:   courses/admin.py
        new file:   courses/apps.py
        new file:   courses/migrations/0001_initial.py
        new file:   courses/migrations/__init__.py
        new file:   courses/models.py
        new file:   courses/serializers.py
        new file:   courses/tests.py
        new file:   courses/urls.py
        new file:   courses/views.py
        new file:   db.sqlite3
        new file:   djangoapi/__init__.py
        new file:   djangoapi/asgi.py
        new file:   djangoapi/settings.py
        new file:   djangoapi/urls.py
        new file:   djangoapi/wsgi.py
        new file:   manage.py

(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % ls
courses         db.sqlite3      djangoapi       manage.py
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % git branch
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % git remote add origin https://github.com/arjunbhardwaj2018/djangoapi.git
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % git branch
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % git branch -M main
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % git branch
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/arjunbhardwaj2018/djangoapi.git'
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % git log
fatal: your current branch 'main' does not have any commits yet
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % git branch
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % 
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % git diff  
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % git add .
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % git commit -m "initial commit"
[main (root-commit) 5188870] initial commit
 17 files changed, 273 insertions(+)
 create mode 100644 courses/__init__.py
 create mode 100644 courses/admin.py
 create mode 100644 courses/apps.py
 create mode 100644 courses/migrations/0001_initial.py
 create mode 100644 courses/migrations/__init__.py
 create mode 100644 courses/models.py
 create mode 100644 courses/serializers.py
 create mode 100644 courses/tests.py
 create mode 100644 courses/urls.py
 create mode 100644 courses/views.py
 create mode 100644 db.sqlite3
 create mode 100644 djangoapi/__init__.py
 create mode 100644 djangoapi/asgi.py
 create mode 100644 djangoapi/settings.py
 create mode 100644 djangoapi/urls.py
 create mode 100644 djangoapi/wsgi.py
 create mode 100755 manage.py
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % git remote add origin https://github.com/arjunbhardwaj2018/djangoapi.git
error: remote origin already exists.
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % git branch
* main
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % git push -u origin main                                                 
Enumerating objects: 20, done.
Counting objects: 100% (20/20), done.
Delta compression using up to 12 threads
Compressing objects: 100% (19/19), done.
Writing objects: 100% (20/20), 8.82 KiB | 2.94 MiB/s, done.
Total 20 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/arjunbhardwaj2018/djangoapi.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % history
 1106  git status
 1107  ls
 1108  git branch
 1109  git remote add origin https://github.com/arjunbhardwaj2018/djangoapi.git
 1110  git branch
 1111  git branch -M main
 1112  git branch
 1113  git push -u origin main
 1114  git log
 1115  git branch
 1116  git diff
 1117  git add .
 1118  git commit -m "initial commit"
 1119  git remote add origin https://github.com/arjunbhardwaj2018/djangoapi.git
 1120  git branch
 1121  git push -u origin main
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi %     
 *  History restored 

arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % source /Users/arjunbhardwaj/practice/djangoRestApi/venv/bin/activate
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % 
====================================================================================================================================
Terminal 3

System check identified no issues (0 silenced).
February 19, 2026 - 09:55:33
Django version 4.2.28, using settings 'djangoapi.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

/Users/arjunbhardwaj/practice/djangoRestApi/djangoapi/courses/urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 19, 2026 - 09:59:14
Django version 4.2.28, using settings 'djangoapi.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

[19/Feb/2026 09:59:57] "GET /admin/ HTTP/1.1" 200 7132
[19/Feb/2026 09:59:58] "GET / HTTP/1.1" 200 5266
[19/Feb/2026 09:59:58] "GET /static/rest_framework/css/prettify.css HTTP/1.1" 200 817
[19/Feb/2026 09:59:58] "GET /static/rest_framework/css/bootstrap-tweaks.css HTTP/1.1" 200 3426
[19/Feb/2026 09:59:58] "GET /static/rest_framework/js/ajax-form.js HTTP/1.1" 200 3796
[19/Feb/2026 09:59:58] "GET /static/rest_framework/css/default.css HTTP/1.1" 200 1152
[19/Feb/2026 09:59:58] "GET /static/rest_framework/js/csrf.js HTTP/1.1" 200 1793
[19/Feb/2026 09:59:58] "GET /static/rest_framework/js/prettify-min.js HTTP/1.1" 200 13632
[19/Feb/2026 09:59:58] "GET /static/rest_framework/js/default.js HTTP/1.1" 200 1268
[19/Feb/2026 09:59:58] "GET /static/rest_framework/js/bootstrap.min.js HTTP/1.1" 200 39680
[19/Feb/2026 09:59:58] "GET /static/rest_framework/js/jquery-3.7.1.min.js HTTP/1.1" 200 87533
[19/Feb/2026 09:59:58] "GET /static/rest_framework/js/load-ajax-form.js HTTP/1.1" 200 59
[19/Feb/2026 09:59:58] "GET /static/rest_framework/css/bootstrap.min.css HTTP/1.1" 200 121457
[19/Feb/2026 09:59:58] "GET /static/rest_framework/img/grid.png HTTP/1.1" 200 1458
[19/Feb/2026 10:00:24] "GET /courses/ HTTP/1.1" 200 9596
[19/Feb/2026 10:00:31] "GET / HTTP/1.1" 200 5266
[19/Feb/2026 10:00:56] "GET /courses/ HTTP/1.1" 200 9596
[19/Feb/2026 10:04:36] "GET /courses/1 HTTP/1.1" 301 0
[19/Feb/2026 10:04:36] "GET /courses/1/ HTTP/1.1" 200 10567
[19/Feb/2026 10:05:21] "GET /courses/ HTTP/1.1" 200 9596
/Users/arjunbhardwaj/practice/djangoRestApi/djangoapi/courses/serializers.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/threading.py", line 973, in _bootstrap_inner
    self.run()
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/threading.py", line 910, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/arjunbhardwaj/practice/djangoRestApi/venv/lib/python3.9/site-packages/django/utils/autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "/Users/arjunbhardwaj/practice/djangoRestApi/venv/lib/python3.9/site-packages/django/core/management/commands/runserver.py", line 133, in inner_run
    self.check(display_num_errors=True)
  File "/Users/arjunbhardwaj/practice/djangoRestApi/venv/lib/python3.9/site-packages/django/core/management/base.py", line 485, in check
    all_issues = checks.run_checks(
  File "/Users/arjunbhardwaj/practice/djangoRestApi/venv/lib/python3.9/site-packages/django/core/checks/registry.py", line 88, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
  File "/Users/arjunbhardwaj/practice/djangoRestApi/venv/lib/python3.9/site-packages/django/core/checks/urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "/Users/arjunbhardwaj/practice/djangoRestApi/venv/lib/python3.9/site-packages/django/core/checks/urls.py", line 24, in check_resolver
    return check_method()
  File "/Users/arjunbhardwaj/practice/djangoRestApi/venv/lib/python3.9/site-packages/django/urls/resolvers.py", line 494, in check
    for pattern in self.url_patterns:
  File "/Users/arjunbhardwaj/practice/djangoRestApi/venv/lib/python3.9/site-packages/django/utils/functional.py", line 57, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/arjunbhardwaj/practice/djangoRestApi/venv/lib/python3.9/site-packages/django/urls/resolvers.py", line 715, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/Users/arjunbhardwaj/practice/djangoRestApi/venv/lib/python3.9/site-packages/django/utils/functional.py", line 57, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/arjunbhardwaj/practice/djangoRestApi/venv/lib/python3.9/site-packages/django/urls/resolvers.py", line 708, in urlconf_module
    return import_module(self.urlconf_name)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 850, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/Users/arjunbhardwaj/practice/djangoRestApi/djangoapi/djangoapi/urls.py", line 22, in <module>
    path('', include('courses.urls')),
  File "/Users/arjunbhardwaj/practice/djangoRestApi/venv/lib/python3.9/site-packages/django/urls/conf.py", line 38, in include
    urlconf_module = import_module(urlconf_module)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 850, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/Users/arjunbhardwaj/practice/djangoRestApi/djangoapi/courses/urls.py", line 2, in <module>
    from . import views
  File "/Users/arjunbhardwaj/practice/djangoRestApi/djangoapi/courses/views.py", line 3, in <module>
    from .serializers import CourseSerializer
  File "/Users/arjunbhardwaj/practice/djangoRestApi/djangoapi/courses/serializers.py", line 4, in <module>
    class CourseSerializer(serializers.HyperlinkModelSerializer):
AttributeError: module 'rest_framework.serializers' has no attribute 'HyperlinkModelSerializer'
/Users/arjunbhardwaj/practice/djangoRestApi/djangoapi/courses/serializers.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 19, 2026 - 10:11:31
Django version 4.2.28, using settings 'djangoapi.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

[19/Feb/2026 10:11:39] "GET /courses/ HTTP/1.1" 200 9999
[19/Feb/2026 10:11:42] "GET /courses/1/ HTTP/1.1" 200 10767
[19/Feb/2026 10:43:42] "GET /courses/ HTTP/1.1" 200 325

 *  History restored 

arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % source /Users/arjunbhardwaj/practic
e/djangoRestApi/venv/bin/activate
(venv) arjunbhardwaj@Arjuns-MacBook-Pro djangoapi % 
