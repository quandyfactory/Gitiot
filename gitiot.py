#!/usr/bin/env python

__title__ = 'Gitiot - The one-button git commit GUI'
__version__ = 0.1
__author__ = "Ryan McGreal ryan@quandyfactory.com"
__homepage__ = "http://quandyfactory.com/projects/49/gitiot"
__copyright__ = "(C) 2009 by Ryan McGreal. Licenced under GNU GPL 2.0\nhttp://www.gnu.org/licenses/old-licenses/gpl-2.0.html"

"""
Gitiot is a really simple cross-platform GUI wrapper for the most minimal useful subset of git's awesome power; i.e. one-button commit and push-to-master for people who want revision control but don't want to learn the command line.
"""

# standard libraries
import os
import shelve
import subprocess
from Tkinter import *
import tkMessageBox 

commit_comment = 'Commit performed by gitiot v. %s' % __version__

def make_process(command, repo_dir):
    """
    Executes a command
    """
    pipe = subprocess.Popen(command, shell=True, cwd=repo_dir)
    pipe.wait()
    return

def get_config(repo_dir=os.path.abspath(os.curdir), master='origin', config_file = 'gitiot.config'):
    """
    Returns a config dictionary with repo_dir and master and manages values in a config file.
    """
    config = {} # initialize config dict

    try:
        with open(config_file, 'r') as file:
            contents = file.readall()
            lines = [line for line in contents if line.strip() != '' and ':' in line and line.strip()[0] != '#']
            for line in lines:
                key, val = line.split(':')
                config[key.strip()] = val.strip()
        if repo_dir != '':
            config['repo_dir'] = repo_dir
        if master != '':
            config['master'] = master
            
    except:
        config['repo_dir'] = repo_dir.strip()
        config['master'] = master.strip()

    # try to save the config values for next time
    try:
        with open(config_file, 'w') as file:
            for key, val in config.items():
                file.write('%s: %s\n' % (key, val))
    except:
        print 'Could not save config values.'
    
    # try to add config_file to the git exclude
    exclude_file = '%s/.git/info/exclude' % (repo_dir)
    try:
        with open(exclude_file, 'r') as file:
            contents = file.readall()
        if config_file in contents:
            with open(exclude_file, 'a') as file:
                file.write('%s\n' % config_file)
    except:
        # hey, it was worth a shot
        pass
    
    return config

def git_add(repo_dir):
    """
    Recursively adds all the files that have changed
    """
    return make_process('git add .', repo_dir)

def git_commit(repo_dir, comment=commit_comment):
    """
    Commits changed files to the repository
    """
    return make_process('git commit -m \'%s\'' % (comment.replace("'", "\'")), repo_dir)

def git_push_master(repo_dir, master):
    """
    Pushes a commit to a remote master
    """
    return make_process('git push %s master' % (master), repo_dir)

class App:
    def __init__(self,parent):

        f = Frame(parent)
        f.pack(padx=15, pady=15)

        self.comment_label = Label(f, text="Comment")
        self.comment_label.pack(side=TOP, padx=10, pady=0)
        
        self.comment = Text(f, width=60, height=6)
        self.comment.pack(side=TOP, padx=10, pady=0)
        self.comment.insert(1.0, commit_comment)
        
        self.button = Button(f, text="Commit", command=self.execute_commit)
        self.button.pack(side=BOTTOM, padx=20, pady=20)
    
    def execute_commit(self):
        """
        Commits the changes to the repository
        """
        config = get_config()
        repo_dir = config['repo_dir']
        master = config['master']
        git_add(repo_dir)
        git_commit(repo_dir, comment=self.comment.get(1.0, END))
        extra_message = ''
        if master != '':
            git_push_master(repo_dir, master)
            extra_message = ' and pushed to the remote master repository'
            
        tkMessageBox.showinfo('Changes Committed', 'Your changes were committed%s.' % (extra_message))

if __name__ == '__main__':
    root = Tk()
    root.title(__title__)
    app = App(root)
    root.mainloop()
