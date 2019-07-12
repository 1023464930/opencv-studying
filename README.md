# opencv-studying

2019.7.11

install opencv based on windows & python 3.7.4

1.build path in system environment variable for python and pip

 #my settings
 
   C:\Users\Gabriel\AppData\Local\Programs\Python\Python37-32
   C:\Users\Gabriel\AppData\Local\Programs\Python\Python37-32\Scripts
   
  then we can directly use python and pip in cmd
  
 #python 3 >=3.4 has included pip, we just need to update using:
 
   python -m pip install -U pip
   
2.install numpy by pip

  pip install numpy
  
3.install opencv

   pip3 install opencv-python
   
4.we can test opencv by the code in test-opencv.py

5.display camera

   we need to install matplotlib by pip under this python file:
   
     python -m pip install matplotlib
     
   use the code in test-camera.py 
 
 2019.7.12
 
 6.test face capture
   
   use the code in face-capture.py
   
   haarcascades folder should be downloaded to the same path of python file
   
   the python file will create mp4 video. inorder to safely save mp4 file, press 'q' to stop python.
   
 7.added new python file face-capture-2.py
 
   see more in description


