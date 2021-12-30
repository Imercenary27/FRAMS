***FRAMS***(Face Recognition and Attendance Management System)


Abstract

In this digital era, face recognition system plays a vital role in  almost every  sector. Face recognition  is one  of the mostly used biometrics. It can used for security, authentication, identification,  and  has  got  many more  advantages.  Now-a-days , It  is  being  widely  used  due  to  its contactless  and  non-invasive  process.  Furthermore,  face recognition system can  also be used  for attendance  marking in schools, colleges,  offices, etc. This  system aims  to build a  class attendance system which uses the concept of face recognition as existing  manual  attendance  system  is  time  consuming  and cumbersome  to maintain.  And there  may be  chances of proxy attendance. Thus, the need for this system increases. This system consists  of four  phases- database  creation, face  detection, face recognition,  attendance  updation.  Database  is  created  by  the images of the students in class. Faces  can be  detected and  recognized  from  live  streaming  video  of  the  classroom. The purpose of this system  to save time which used to get consumed in the traditional method. Attendance will be recorded for further reference in an excel file at the end of the session.
![image](https://user-images.githubusercontent.com/73638643/147743132-06bc51e6-6b7d-4c5e-80c4-bcdc0f022630.png)

Literature Survey:
1) Python
Python is an interpretated high-level general purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. We have used Python 3.9.1 version for the project.
2) Pandas
Pandas is mainly used for data analysis. Pandas allows importing data from various file formats such as comma-separated values, JSON, SQL, and Microsoft Excel. Pandas allows various data manipulation operations such as merging, reshaping, selecting, as well as data cleaning, and data wrangling features.
3) Numpy
NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices. NumPy delivers clean and fast array-based computing in a free open source software library. It is a fundamental package in the SciPy stack for scientific computing . Over 370 thousand projects use for efficient array computing
4) Matplotlib
Matplotlib is a cross-platform, data visualization and graphical plotting library for Python and its numerical extension NumPy. As such, it offers a viable open source alternative to MATLAB. Developers can also use matplotlib's APIs (Application Programming Interfaces) to embed plots in GUI applications

5) Pyttsx3
Pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
6) OpenCV
OpenCV, is a machine learning library that is used to develop computer vision applications. OpenCV is a great tool for image processing and performing computer vision tasks. It is an open-source library that can be used to perform tasks like face detection, objection tracking, landmark detection, and much more.
7) Os
An Operating System (OS) is an interface between a computer user and computer hardware. An operating system is a software which performs all the basic tasks like file management, memory management, process management, handling input and output, and controlling peripheral devices such as disk drives and camera.
8)Tkinter
Tkinter is a graphical user interface(GUI) library of Python, which you can use to create desktop apps with a user interface.The best thing is that Tkinter is pretty simple, and you can learn it fast if you know the fundamentals of Python and object-oriented programming.
9) Scipy
SciPy is an open-source Python library which is used to solve scientific and mathematical problems. It is built on the NumPy extension and allows the user to manipulate and visualize data with a wide range of high-level commands.





User Registration:


The users can interact with the system using a GUI. Here users will be mainly provided with three different options such as, student registration, and mark attendance. The students are supposed to enter all the required details in the student registration form. After clicking on register button, the students details will be updated in the database. For in case if the student wants to edit his/her details this option is available and the new information will be updated in the database.
1) Dataset Creation:
Images of students are captured using a web cam. Multiple images of single student will be acquired with varied gestures and angles. These images undergo pre-processing. The images are cropped to obtain the Region of Interest (ROI) which will be further used in recognition process. Next step is to resize the cropped images to particular pixel position. Then these images will be converted from RGB to gray scale images. And then these images will be saved as the names of respective student in a folder.
2) Face Detection
Face detection here is performed using Haar-Cascade Classifier with OpenCV. Haar Cascade algorithm needs to be trained to detect human faces before it can be used for face detection. This is called feature extraction. The haar cascade training data used is an xml file haarcascade_frontalface_default. 
Here we are using detectMultiScale module from OpenCV. This is required to create a rectangle around the faces in an image. It has got three parameters to consider- scaleFactor, minNeighbors, minSize. scaleFactor is used to indicate how much an image must be reduced in each image scale. minNeighbors specifies how many neighbors each candidate rectangle must have. Higher values usually detects less faces but detects high quality in image. minSize specifies the minimum object size. Then it automatically starts clicking photos until 30 samples are collected.
3) Face Recognition:
Face recognition process can be divided into three stepsprepare training data, train face recognizer, prediction. Here training data will be the images present in the dataset. They will be assigned with a integer label of the student it belongs to. These images are then used for face recognition. Face recognizer used in this system is Local Binary Pattern Histogram. Initially, the list of local binary patterns (LBP) of entire face is obtained. These LBPs are converted into decimal number and then histograms of all those decimal values are made. At the end, one histogram will be formed for each image in the training data. Later, during recognition process histogram of the face to be recognized is calculated and then compared with the already computed histograms and returns the best matched label associated with the student it belongs to .
4) Attendance Updation 
After face recognition process, the recognized faces will be marked as present in the excel sheet and the rest will be marked as absent and the list of absentees will be recorded. 
5) Framie : 
In case if any of the user wants to know more details about the development of this system he/she can use this chat bot named framie. to gain acquired knowledge about this system.







CONCLUSION:


This  system  aims  to  build  an  effective  class  attendance system  using  face  recognition  techniques.  The  proposed system will be able to mark the attendance via face Id. It will detect faces via webcam and then recognize the faces. After recognition,  it  will  mark  the  attendance  of  the  recognized student and update the attendance record.
