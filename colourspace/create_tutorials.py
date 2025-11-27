# -*- coding: utf-8 -*-
"Put the ipython tutorias from tutorials in a accessible directory "

try:
    from importlib.resources import files as import_pack_files
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    # For Py<3.9 files is not available
    from importlib_resources import files as import_pack_files


import os
import colourspace

def main():
    current_directory = os.getcwd()
    tutorials = ['1. convert.ipynb', '2. sRGB gamut.ipynb',
        '3. full gamut.ipynb', '4. slices.ipynb', '5.1 cmaps helix.ipynb',
        '5. cmaps.ipynb']
    resources = import_pack_files('colourspace.tutorials')
    if not os.path.exists(f'{current_directory}/colourspace_tutorials'):
        os.mkdir(f'{current_directory}/colourspace_tutorials') 
    writedir = f'{current_directory}/colourspace_tutorials/'   
    for file in tutorials:
        data = (resources / file).read_bytes()
        with open(writedir+file,'w+b') as tmp:
            tmp.write(data)