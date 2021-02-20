# Installation

https://kivy.org/doc/stable/gettingstarted/installation.html

```
python -m pip install --upgrade pip setuptools wheel virtualenv
python -m virtualenv kivy_venv

```
For Windows default CMD, in the command line do:
```
kivy_venv\Scripts\activate
```
If you are in a bash terminal on Windows, instead do:
```
source kivy_venv/Scripts/activate
```
If you are in linux, instead do:
```
source kivy_venv/bin/activate
```
Install Kivy
```
python -m pip install kivy[base] kivy_examples --no-binary kivy
pip install kivy kivy_deps.sdl2
```

### to EXE
```
https://www.youtube.com/watch?v=NEko7jWYKiE&list=RDCMUCFB0dxMudkws1q8w5NJEAmw&start_radio=1&t=562
```



Step 1:

Ensure you have the correct files installed etc. (kivy, pip, pyinstaller)

Step 2:

Create a project folder, with your files in like so:

C:\Users\r00t\Desktop\py-project\kivy_designs\py2exe\kivy_test.py

Step 3:

Open a terminal in the project folder, (remember to activate your venv if you are using that).

Enter the following into the terminal, replacing 'kivy_demo' with a project name, and the path to your .py file:

python -m PyInstaller --name kivy_demo C:\Users\r00t\Desktop\py-project\kivy_designs\py2exe\kivy_test.py

Step 4 (optional):

Optional step to add a custom icon to your finished exe.

Replace details as above and add path to .ico file:

python -m PyInstaller --name kivy_demo --icon C:\Users\r00t\Desktop\py-project\kivy_designs\py2exe\myicon.ico C:\Users\r00t\Desktop\py-project\kivy_designs\py2exe\kivy_test.py

Step 5:

Now go into your project folder, for me its C:\Users\r00t\Desktop\py-project\kivy_designs\py2exe. Open the spec file and add
the below to the top:

from kivy_deps import sdl2, glew

Step 6:

Still in the spec file, add a path for your assets e.g. (.png / .kv). I wont be covering video imports in this video as there 
are additional steps required for that.

You will need to add the below with the path to your assets for your program:

Tree('assets\\'),

also add the below as is with no changes: 

*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],

So your spec file in the 'COLLECT' section should look similar to this, but using your path:

coll = COLLECT(exe, Tree('assets\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               name='kivy_test')

Step 7:

Finally we run the below command which includes all the necessary files and kivy hooks (additional files to compile exe):

python -m PyInstaller kivy_demo.spec

The compiled package will be in your specified directory, for me its C:\Users\r00t\Desktop\py-project\kivy_designs\py2exe\distTrack: Arc North - Catch Me When I Fall (ft  Sarah de Warren)
