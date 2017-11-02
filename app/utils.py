from urllib.request import urlretrieve
import zipfile
import os, requests, shutil
import tarfile

def download_file(source_url, target_filepath):
    if not os.path.exists(target_filepath):
        print('downloading {}'.format(target_filepath))
        urlretrieve(source_url, target_filepath)
    else:
        print('{} exists. skipping download'.format(target_filepath))

def unzip_file(zipfilepath, target_dir):
    if os.path.isfile(zipfilepath):
        print("Unzipping {}".format(zipfilepath))
        zipfile.ZipFile(zipfilepath, 'r').extractall(path=target_dir)
    else:
        print('{} does not exist'.format(zipfilepath))

def untar_file(tarfilepath, target_dir):
    if os.path.isfile(tarfilepath):
        print("Untarring {}".format(tarfilepath))
        tar = tarfile.open(tarfilepath)
        tar.extractall(target_dir)
        tar.close()
    else:
        print('{} does not exist'.format(tarfilepath))
