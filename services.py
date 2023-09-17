#!/usr/bin/env python 
#*** DO NOT EDIT - GENERATED FROM notebooks/services.ipynb ****

import sys, os,  glob, logging, json
from  mangorest.mango import webapi

MBASE  = "/opt/data/data/kanban/"
logger = logging.getLogger( "kanban" )
#---------------------------------------------------------------------------------    
@webapi("/kanban/save")
def save( request, name, contents,**kwargs):
    name = name or "default"
    if (name.endswith(".json")):
        name = name[:-5]
        
    dst = f"{MBASE}{name}.json"
    dstd= os.path.dirname(dst)
    if not os.path.exists(dstd ):
        os.makedirs(dstd)

    with open(dst, "w") as f:
        f.write(contents.strip().replace("\r", ""))

    return f"Saved {dst}"    
#---------------------------------------------------------------------------------    
@webapi("/kanban/get")
def get( name, **kwargs):
    if (name.endswith(".json")):
        name = name[:-5]
    dst = f"{MBASE}{name}.json"
    if not os.path.exists(dst):
        ret = "{}"
    else:
        ret = open(dst, "r").read()
    return ret  
#------------------------------------------------------------------------------
@webapi("/kanban/delete")
def delete(name="", **kwargs):
    dst = f"{MBASE}/{name}.json"
    if ( not os.path.exists(dst) ):
        return "OK {dst} does not exist!!"
    os.remove(dst)
    return f"Deleted {dst}."
#------------------------------------------------------------------------------
@webapi("/kanban/getall")
def getAllDashboards( nrows=10000, patt='*.json', **kwargs):
    files = glob.glob(f"{MBASE}{patt}")
    files.sort(key=os.path.getmtime, reverse=True)
    ret = {
        "name": "dashboards",
        "columns": ["name"],
        "values": [[f[len(MBASE):]] for f in files][0:nrows]
    }
    return ret
