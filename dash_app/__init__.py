import functools
import json
import os
from typing import Dict

import pandas as pd

OG_DESCRIPTION = "Glass explore calculates thermal and optic properties of double-glazing, using coating are substrates in the IGDB database. Currently the app is only set up to run the NFRC 100-2010 environment."

PATH_DATA = os.path.join('data')

DEVTEMP = os.path.join(os.getcwd(),'temp') 

class LayoutID:

    MODAL_ABOUT = "modal-splash"
    MODAL_ABOUT_CLOSE = "modal-splash-close"

    MODAL_SETTINGS = "modal-settings"
    MODAL_SETTINGS_CLOSE = "modal-settings-close"

    DIV_OUTERLITE_PRODUCT = "div-outerlite-product"
    DIV_BUILDUP_SVG_CONTAINER = "div-buildup-svg-container"

    
    NAVLINK_ABOUT = "navlink_about"
    NAVLINK_SETTINGS = "navlink_settings"

    
    TABS = "tabs"
    TAB_CONTENT = "tab-content"

    URL = "url"




DEFAULT_OPTICAL_STANDARD = "W5_NFRC_2003.std"

@functools.cache    
def standards():

    fpath = os.path.join(PATH_DATA,'standards.json')
    with open(fpath) as f:
        s = json.load(f)
    return s
    