# standard libraries
import os
import sys
import subprocess

def make_process(command):

def get_config(repo_dir='', master='', config_file = 'gitiot.config'):
    """
    Returns a config dictionary with repo_dir and master and manages values in a config file.
    """
    config = {} # initialize config dict

    try:
        with open(config_file, 'r') as file:
            contents = file.readall()
            lines = [line for line in contents if line.strip() != '' and ':']
            for line in lines:
                key, val = line.split(':')
                config[key.strip()] = val.strip()
        if repo_dir != '':
            config['repo_dir'] = repo_dir
        if master != '':
            config['master'] = master
            
    except:
        # add repo_dir to config
        if repo_dir == '':
            repo_dir = raw_input('Enter repo directory: ')
        config['repo_dir'] = raw_input.strip()
        
        # add master to config
        if master == '':
            master = raw_input('Enter master alias: ')
        config['master'] = master.strip()

    # try to save the config values for next time
    try:
        with open(config_file, 'w') as file:
            for key, val in config.items():
                file.write('%s: %s\n' % (key, val))
    except:
        print 'Could not save config values.'
        
    return config

def git_add():
    """
    Recursively adds all the 
    """
    

