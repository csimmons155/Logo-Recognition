__author__ = 'Chris Simmons'

import cv2;
import os.path
import sys



BASE_PATH = "/Users/christophersimmons/facerec/data/at/"
SEPARATOR = " ; "

ramp_frames = 10;


def getImage(image):

    img = cv2.imread(image);
    img_pgm = cv2.imwrite("test7FR.pgm",img);

def get_image(cam):
    retval, im = cam.read()
    return im



#make the ouptut.txt file 
def makeOutput():
    file_2 = "/Users/christophersimmons/Output.txt"
    text_file = open(file_2, "w")

    label = 0
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname) #create path to subdirectory
            for filename in os.listdir(subject_path):
                if (filename == ".DS_Store"):
                    continue
                abs_path = "%s/%s" % (subject_path, filename)
                print "%s;%d" % (abs_path, label)
                text_file.write("%s;%d\n" % (abs_path, label))
            label += 1

    text_file.close()

# NOTE: To add a new person: make a new subdirname

#make the "si" directory BEFORE running this method..

def addPerson(sub):
    for i in xrange(ramp_frames):
        camera = cv2.VideoCapture(0)
        temp = get_image(camera)
        print("Taking image Number %i" % i)
        camera_capture = get_image(camera)
        #make the s%i directory FIRST !
        file = "/Users/christophersimmons/facerec/data/at/s%i/%iFR.pgm" % (sub, i);
        print file
        #file = "/Users/christophersimmons/testFRimage.pgm";
        cv2.imwrite(file, camera_capture)
        del(camera)


#addPerson(3)
makeOutput()

#getImage("im7.jpg");