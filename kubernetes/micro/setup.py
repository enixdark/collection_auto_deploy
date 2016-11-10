# -*- coding: utf-8 -*-
import sys, os
import yaml
import glob
import subprocess
from optparse import OptionParser
from jinja2 import (Environment, FileSystemLoader)
from config import CONFIG

env = Environment()
env.loader = FileSystemLoader('.')


"""
generate yaml file for kubernetes from jinja2 file
"""
def save(file):
  render = env.get_template(file).render(CONFIG)
  with open(file[:-3],'w') as f:
    yaml.safe_dump(yaml.load(render), f, 
      canonical=False, 
      default_flow_style=False, 
      allow_unicode=False)

"""
remove all yaml file in project
"""
def clean(file):
  os.remove(file)

"""
create service, pod, job, rc via kubectl
"""
def run(file):
  pass

if __name__ == '__main__':
  # opt_parse = OptionParser()
  # opt_parse.add_option('-g', '--generate', dest = '', 
  #   help = "command to generate yaml file")
  # opt_parse.add_option('-c', '--clean', dest = '', 
  #   help = "command to clean all yaml file")
  # params = opt_parse.parse_args()[0]
  if len(sys.argv) == 2:
    params = sys.argv[1]
    if params == "generate":
      save('example-secret.yaml.j2')
      regex_file = "%s/*.j2"
      func = save
    elif params == "clean":
      clean('example-secret.yaml')
      regex_file = "%s/*.yaml"
      func = clean
    for _, subdirs, files in os.walk('.'):
      for folder in subdirs:
        list_files = glob.glob(regex_file % folder)
        for file in list_files:
          func(file)
    