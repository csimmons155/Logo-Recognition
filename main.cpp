#include "opencv2/highgui/highgui.hpp"
#include "opencv2/core/core.hpp"
#include "opencv2/objdetect/objdetect.hpp"
#include "opencv2/face.hpp"
#include "opencv2/opencv.hpp"

#include "FaceRecognition.pch"


#include <iostream>
#include <string>

using namespace cv;
using namespace std;

int main( int argc, const char** argv )
{
    //LBPHFaceTraining();
    
    int value = facialRecognition();
    
    system("Pause");
    return 0;
}