#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
        generate a tgz archive for the web_static
    """    
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    local("sudo tar -cvzf {} web_static".format(file))
    print("web_static packed: {} -> {}Bytes".format(file, os.path.getsize(file)))
