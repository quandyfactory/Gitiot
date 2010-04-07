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

Make some changes to your project files and then run `gitiot.py`. 

You'll see a basic GUI window with a comment box and a Commit button. Enter any comments on this commit into the comment box and push the Commit button to add your changed files, commit them to your local repository and, if applicable, push the commit out to the remote master. 

**Note**: the default name for the remote master is "origin". If you set your remote to a different name (say, "github"), you will need to open `gitiot.config` in a text editor and change this line:

    `master: origin`

Replace "origin" with either the [named remote](http://www.kernel.org/pub/software/scm/git/docs/git-push.html#REMOTES) or the [git URL]().
