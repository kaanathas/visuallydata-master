import pickle as pkl
from pprint import pprint
import numpy as np
import time
import urllib
import urllib.request
import os
import pandas as pd 
from collections import Counter
import matplotlib.pyplot as plt


infographicList = pkl.load(open("./infographics60K_metadata.pckl", "rb"))

print('We include meta-data obtained from Visual.ly for %d infographics. We call this the 63K dataset.\n'\
       'No additional filtering or annotations are provided beyond what is already found on Visual.ly.\n'\
       'This is the original, uncurated data.\n'\
      'Note: we do not provide the downloaded images themselves, only the URLs for download.'
      %(len(infographicList)))


pprint(infographicList[0].__dict__)