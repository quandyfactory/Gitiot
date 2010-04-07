# standard libraries
import os
import sys
import

# 3rd party libraries
import git

# initialize git config dictionary
config = {} 

# get config values
try:
    with open('gitiot.config', 'r') as file:
        contents = file.readall()
        lines = [line for line in contents if line.strip() != '' and ':']
        for line in lines:
            key, val = line.split(':')
            config[key.strip()] = val.strip()
except:
    config['repo_dir'] = raw_input('Enter repo directory: ')
    config['master'] = raw_input('Enter master alias: ')
    with open('gitiot.config', 'w') as file:
        for key, val in config.items():
            file.write('%s: %s\n' % (key, val))

try:
    repo_dir = config['repo_dir'].strip()
except KeyError:
    repo_dir = os.path.abspath(os.curdir)

try:
    master = config['master'].strip()
except KeyError:
    master = ''

repo = git.Repo(repo_dir)

commits = repo.commits()

tree = commits[0].tree

files = [item[0] for item in tree.items()]

for fi in files: 
    print fi
    

