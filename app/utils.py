import os
from urllib.request import urlretrieve

def download_file(source_url, target_filepath):
    if not os.path.exists(target_filepath):
        print('downloading {}'.format(target_filepath))
        urlretrieve(source_url, target_filepath)
    else:
        print('{} exists. skipping download'.format(target_filepath))
