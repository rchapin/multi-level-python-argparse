# A Multi-Level Python Argparse Example

The following is an example of a multiple level Python argparse implementation.

There are branches and targets and arguments.  

**Branches** are levels in the argparse tree that do not have a target function that enable you to organize functionality under them.

**Targets** are levels in the argparse tree that are wired up to target functions.

Following is an outline of the parsing tree that we are going to build.
- **deploy** (*branch*: Organizes all of the deployment related functionality)
  - **myappone** (*branch* and *target*: Calling "deploy myappone" will execute the complete deployment of myappone, calling the MyAppOne.deploy function)
    - **setup** (*target*: Only executes the setup for MyAppOne)
    - **configs** (*target*: Only executes the deployment of the configurations for MyAppOne)
  - **myapptwo** (*branch* and *target*: Calling "deploy myapptwo" will execute the complete deployment of myapptwo, calling the MyAppOne.deploy function)
    - **setup** (*target*: Only executes the setup for MyAppTwo)
    - **configs** (*target*: Only executes the deployment of the configurations for MyAppTwo)
  - **system** (*branch*: Organizes all of the system related deployment targets)
    - **basesetup** (*target*: Executes a function that will do some basic setup tasks against some hosts in the sytem)
    - **installjava** (*target*: Executes the installation of a JDK on some hosts in the system)
- **utils** (*branch*: Organizes any number of utility programs)
  - **dns** (*branch*: A branch that organizes all of the DNS utility functions)
    - **dnsthing1** (*target*: Some DNS utility)
    - **dnsthing2** (*target*: Some DNS utility)

With the example provided you can build an infinitely (there probably is some limitation to the framework but I do not know what it is) deep set of arguments for a multi-faceted program.

The code is commented/self-explanatory.

To "run" it and see it in action:

1. Clone the repository and cd into the repo directory.

1. Create a Python 3.8.5 or greater virtual environment and pip install the multilevelargparse code from the cloned repo.
```
python3.8 -mvenv ~/.virtualenvs/multilevelargparse
. ~/.virtualenvs/multilevelargparse/bin/activate
pip install -e .
```

1. Then you can try it out by entering
```
multilevelargparse
```

1. And then any of the sub-commands; for example:
```
multilevelargparse deploy --version
```

1. Or:
```
multilevelargparse deploy myappone --version 123
```

If you have any questions you can [contact me via my website](https://www.ryanchapin.com/contact/).
