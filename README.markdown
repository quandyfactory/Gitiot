##Gitiot - The one-click git commit GUI.

Gitiot is a really simple cross-platform GUI wrapper for the most minimal useful subset of git's awesome power; i.e. one-button commit and push-to-master for people who want revision control but don't want to learn the command line.

###Author

* Author: Ryan McGreal
* Email: [ryan@quandyfactory.com](mailto:ryan@quandyfactory.com)
* Homepage: [http://quandyfactory.com/projects/49/gitiot](http://quandyfactory.com/projects/49/gitiot)
* Repository: [http://github.com/quandyfactory/gitiot](http://github.com/quandyfactory/gitiot)

###This Version

* Version: 0.12
* Release Date: 2010-04-07

###Revision History

####Version 0.12

* Release Date: 2010-04-07
* Changes:
    * Fixed tab on Comment so it actually tabs to next control as per [this article](http://stackoverflow.com/questions/1450180/how-can-i-change-the-focus-from-one-text-box-to-another-in-python-tkinter)
    
####Version 0.11

* Release Date: 2010-04-07
* Changes:
    * Split config functions into get_config() and set_config()    
    * Created global default variables for repo_dir, config file and named remote (master)
    * Fixed get_config() bug that wasn't splitting config file contents into a list of lines
    * Added an icon that apparently only works in Windows

####Version 0.1

* Release Date: 2010-04-06
* Changes:
    * First commit

##Requirements

You need to have the following installed to run this program:

* [Python](http://www.python.org/download) 2.5.x or 2.6.x
    * **Note:** On some Linux distros, you may need to install python-tk - just install it using your system's package manager.
* [Git]() (POSIX) or [Msysgit](http://code.google.com/p/msysgit/) (Windows)
    * **Note:** If using Msysgit on Windows, you must select the "Run Git from the Windows Command Prompt" option under *Adjusting your PATH environment* during installation. 

Otherwise, Gitiot has no additional dependencies.

##Using Gitiot

The easiest way to use `gitiot.py` is to save it inside the root folder of your project (*nix users, remember to set execute permissions). This way, the config file will Just Work.

Make some changes to your project files and then run `gitiot.py`. You'll see a basic GUI window with a comment box and a Commit button. 

Enter any comments on this commit into the comment box and push the Commit button to add your changed files, commit them to your local repository and, if applicable, push the commit out to the remote master. 

**Note:** The default named remote is "origin". See Config, below, on how to change it.

##Configuring Gitiot

###Repository Directory

You might not want `gitiot.py` in the same folder as the project. In that case, you will need to open `gitiot.config` in a text editor and change this line:

    repo_dir = /path/to/repository

replace `/path/to/repository` with the actual path to your repository.

###Named Remote

Likewise, you might not use "origin" as the named remote for your repository. If you set your remote to a different name (say, "github"), you will need to open `gitiot.config` in a text editor and change this line:

    master = origin

Replace "origin" with either the [named remote](http://www.kernel.org/pub/software/scm/git/docs/git-push.html#REMOTES) or the [git URL](http://www.kernel.org/pub/software/scm/git/docs/git-push.html#URLS).

If you have no remote master and only want to use the repository locally, remove "origin" and leave the line as:

    master = 

##Python Command Line

Gitiot is designed to be used by people who don't want to use the command line, but you can still use it in a Python REPL if the mood strikes you. Just save `gitiot.py` somewhere in your PATH and then import it as a module:

    >>> import gitiot
    >>> config = gitiot.get_config()
    >>> repo_dir = config['repo_dir']
    >>> master = config['master']
    >>> comment = 'I stubbornly insist on using git on a command line without just, you know, using git'
    >>> gitiot.git_add(repo_dir)
    >>> gitiot.git_commit(repo_dir, comment)
    >>> if master != '': gitiot.git_push_master(repo_dir, master)

##Planned Enhancements

* Add command line arguments for executing `gitiot.py` so you can run in non-interactive mode and pass in arguments.

##Credits

Special thanks for [@adr](http://twitter.adr) for inspiring me to write this in his [cri du coeur](http://twitter.com/adr/status/11716000425) regarding making git accessible to non-techies.

