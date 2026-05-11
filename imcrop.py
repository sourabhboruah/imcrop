from PIL import Image
import numpy as np
import sys

def usage():
  print('Usage - python imcrop.py in_image width height bias out_image')
  print('in_image - input image path')
  print('width - desired width')
  print('height - desired height')
  print('bias  - -1 to 1 indicating normalized crop location')
  print('out_image - output image path')

if len(sys.argv)==6:
  in_image=sys.argv[1]
  width=float(sys.argv[2])
  height=float(sys.argv[3])
  bias=float(sys.argv[4])
  out_image=sys.argv[5]
  print('{:<15s}{:s}'.format('Input Image',in_image))
  print('{:<15s}{:f}'.format('Target Width',width))
  print('{:<15s}{:f}'.format('Target Height',height))
  print('{:<15s}{:f}'.format('Crop Bias',bias))
  print('{:<15s}{:s}'.format('Output Image',out_image))
  arr=np.array(Image.open(in_image))
  if arr.shape[0]/arr.shape[1]>height/width:
    size_needed=int(arr.shape[1]*height/width)
    arr2=arr[int((1-bias)*(arr.shape[0]-size_needed)/2):size_needed+int((1-bias)*(arr.shape[0]-size_needed)/2),:,:]
    Image.fromarray(arr2).save(out_image)
  elif arr.shape[0]/arr.shape[1]<height/width:
    size_needed=int(arr.shape[0]*width/height)
    arr2=arr[:,int((1-bias)*(arr.shape[1]-size_needed)/2):size_needed+int((1-bias)*(arr.shape[1]-size_needed)/2),:]
    Image.fromarray(arr2).save(out_image)
else:
  usage()
