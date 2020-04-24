import os, sys
import argparse
from glob import glob
import glob
import numpy as np
import pydicom
import img

from skimage.external.tifffile import imsave, imread
from skimage.transform import resize
import h5py

import matplotlib.pyplot as plt

#print(sys.path[0])
utils_path = os.path.join(sys.path[0], os.path.abspath('../../../miruware/ct-denoising/utils'))
utlis_path = os.path.abspath(utils_path)
sys.path.append(utils_path)
#print(sys.path)

def load_dcm_scans(dcm_dir):
    """
    dicom_dir: directory which contains all dicom files for one case
    return:
        dicom_slices with all dicom information
    """    
    # print(dcm_dir)
    # dcm_files = os.listdir(dcm_dir)
    # dcm_slices = [(pydicom.dcmread(os.path.join(dcm_dir, f)), os.path.basename(f)) for f in dcm_files]
    # dcm_slices.sort(key = lambda x: int(x[0].InstanceNumber))
    
    #dcm_files = glob(os.path.join(dcm_dir, '*.dcm'))
    dcm_slices = [pydicom.dcmread(f) for f in dcm_files]
    dcm_slices.sort(key = lambda x: int(x.InstanceNumber))


    return dcm_slices

#dcm_dir='/data/data1/ACRIN-FLT-Breast/ACRIN-FLT-Breast_001/'
#dcm_slices=load_dcm_scans(dcm_dir)
dcm_files=[]
for dcm_file in glob.iglob('/data/data1/minjoo/data/aibi/CT/Chest_가슴/LIDC-IDRI/LIDC-IDRI-0001/01-01-2000-30178/3000566-03192/**/*.dcm', recursive=True):
    dcm_files.append(dcm_file)  


dcm_slices=load_dcm_scans(dcm_files)
count=0
for i in range(len(dcm_slices)):
    if(dcm_slices[i].Modality=='CT'):
        print(dcm_slices[i].Modality)
        # count+=1
    else:
        count+=1
        print(dcm_slices[i].Modality)
        
if(count==0):
    # print("There are no CT")
    print("all modalities are CT")

