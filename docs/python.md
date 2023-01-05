# Python development 
https://docs.python-guide.org/

## Installing Python
Guides to installing Python on [Mac](https://docs.python-guide.org/starting/install3/osx/#install3-osx
), [Windows](https://docs.python-guide.org/starting/install3/win/#install3-windows
), and [Linux](https://docs.python-guide.org/starting/install3/linux/#install3-linux
).

## Virtual environments
Virtual environments help you manage dependencies and package installs on a per-project
basis. In general, it is a bad idea to do development without using a virtual 
environment. Many tools exist for creating virtual environments, some are documented 
[here](https://docs.python-guide.org/dev/virtualenvs/).

python3.9 -m venv my-venv
source my-venv/bin/activate
pip install -U pip setuptools
pip install graspologic

## Using an IDE
- I highly recommend using [VS Code](https://code.visualstudio.com/) for 
Python development, as it has lots of nice features for working with GitHub and Jupyter 
Book. It will also make it easier for me to help you debug if using VS Code. 
- There is a
nice article on [*Getting Started with Python in VS Code*](https://code.visualstudio.com/docs/python/python-tutorial), which also includes instructions on getting a Python interpreter.
- Make sure you are always using some kind of virtual environment for developing in Python. This is described further for VS Code in the same article above [here](https://code.visualstudio.com/docs/python/python-tutorial#_install-and-use-packages).

```{note}
If you have a lot of experience using Python/developing some other way and you are 
welcome to stick with it, just note that it may be harder for me to provide feedback for
other IDEs or Python setups.
```

