# Python development 
Please refer to the main Python documentation [here](https://docs.python-guide.org/) for a lot more good advice on Python development.


## Installing Python
Guides to installing Python on: [Mac](https://docs.python-guide.org/starting/install3/osx/#install3-osx
), [Windows](https://docs.python-guide.org/starting/install3/win/#install3-windows
), and [Linux](https://docs.python-guide.org/starting/install3/linux/#install3-linux
).

Once you have installed Python 3, you should be able to try a command like one of the following (depending on your shell) to see where the Python interpreter is located.

Bash:
```
which python3

> /usr/local/bin/python3
```

Command prompt:
```
where python3

...
```


## Virtual environments
Virtual environments help you manage dependencies and package installs on a per-project
basis. In general, it is a bad idea to do development without using a virtual 
environment. Many tools exist for creating virtual environments, some are documented 
[here](https://docs.python-guide.org/dev/virtualenvs/).

Below, I provide an example using `virtualenv`, which is now bundled with Python by default (meaning you shouldn't need to download anything extra). Here, I am using Python 3.9, but this may differ for your platform (you can also likely just do `python3` instead of `python3.9`).

Creates a new virtual environment in the current working directory:
```
python3.9 -m venv venv
```

From the same directory (since the command above created a new folder called `venv`), I should now be able to do:

Bash:
```
source venv/bin/activate
```
(not sure if the below is correct on Windows)
Command prompt:
```
venv\Scripts\activate
```

If this worked, you will likely see `(venv)` at the start of your
shell prompt now. You can also check for what interpreter the `python` command is now pointing to:
```
which python
```
Hopefully, this is now pointing to a file in the `venv` folder you just created.

With the virtual environment active, you can install some packages to use in this course. This command will update/install `pip` and some other packages that help us install other things.
```
pip install -U pip setuptools wheel
```

Finally, you can install the required packages. `graspologic` is a Python
package for network statistics which we'll use in the course. Conveniently, it
also depends on other packages we'll use, like `pandas`, `numpy`, `scipy`, `networkx`, `matplotlib`, and `seaborn`. `pip` is smart enough to also install
all of these dependencies for you.
```
pip install graspologic --pre
```

```{note}
The `--pre` flag in the above will install the latest `graspologic` pre-release, which will ensure you are getting the most up-to-date version of the package (although it will also be somewhat of a beta version).
```

During installations like these, pay attention to any error messages that
happen during installation. These would likely mean that packages (including
dependencies of the one you are trying to install) will not work properly down
the line.

```{warning}
If you are using a MacBook with an M1/M2 processor, or another ARM architecture chip, then the above may not work for you. Please discuss with Ben.
```

To see if this all worked, start a Python interpreter:
```
python
```
Within the Python interpreter, try importing `graspologic`:
```
import graspologic
```

If you would like to use Jupyter Notebook, you should also do
```
pip install jupyter
```

```{note}
If you are used to using Jupyter Notebooks by launching a terminal from the command,
line, then you will need to make sure that the right version of Jupyter Notebook is
connected to the virtual environment. Test this by doing ```which jupyter``` (bash) or ```where jupyter``` (Windows). The result should be a path *within* the virtual 
environment you just created, e.g. for me it looks like 
```/Users/bpedigo/JHU_code/networks-course-2023/.venv/bin/jupyter```. If you try 
```jupyter-notebook``` *with your virtual environment active* and you still cannot
import packages installed in the virtual environment (e.g. ```import graspologic```), then you made need to try the solution detailed [here](https://stackoverflow.com/a/42454615/15480487). Namely, the command ```ipython kernel install --user --name=venv```.
```

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
