##Gitiot - The one-click git commit GUI.

Gitiot is a really simple cross-platform GUI wrapper for the most minimal useful subset of git's awesome power; i.e. one-button commit and push-to-master for people who want revision control but don't want to learn the command line.

###Author

* Author: Ryan McGreal
* Email: ryan@quandyfactory.com
* Homepage: http://quandyfactory.com/projects/49/gitiot
* Repository: http://github.com/quandyfactory/gitiot

###This Version

* Version: 0.1
* Release Date: 2010-04-06

###Revision History

####Version 0.1

* Release Date: 2010-04-06
* Changes:
    * First commit

##Using Gitiot

The easiest way to use `gitiot.py` is to save it inside the root folder of your project (*nix users, remember to set execute permissions). This way, the config file will Just Work.

Make some changes to your project files and then run `gitiot.py`. You'll see a basic GUI window with a comment box and a Commit button. 

Enter any comments on this commit into the comment box and push the Commit button to add your changed files, commit them to your local repository and, if applicable, push the commit out to the remote master. 

**Note:** The default named remote is "origin". See Config, below, on how to change it.

###Config

####Repository Directory

You might not want `gitiot.py` in the same folder as the project. In that case, you will need to open `gitiot.config` in a text editor and change this line:

    repo_dir = /path/to/repository

replace `/path/to/repository` with the actual path to your repository.

####Named Remote

Likewise, you might not use "origin" as the named remote for your repository. If you set your remote to a different name (say, "github"), you will need to open `gitiot.config` in a text editor and change this line:

    master = origin

Replace "origin" with either the [named remote](http://www.kernel.org/pub/software/scm/git/docs/git-push.html#REMOTES) or the [git URL](http://www.kernel.org/pub/software/scm/git/docs/git-push.html#URLS).

If you have no remote master and only want to use the repository locally, remove "origin" and leave the line as:

    master = 

###Command Line

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

* Tkinter is kind of crappy. At least the tab button should move focus from the comment box to the Commit button. There's probably some way to set this behaviour that I should look into.

* Still need to test whether this works on Windows with msysgit.

##Credits

Special thanks for [@adr](http://twitter.adr) for inspiring me to write this in his [cri du coeur](http://twitter.com/adr/status/11716000425) regarding making git accessible to non-techies.

