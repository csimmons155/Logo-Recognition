# Logo-Recognition
<h5>System that recognizes coporate logos (i.e. McDonalds and Apple, for now)</h5>

<img src = "https://github.com/csimmons155/Logo-Recognition-/blob/master/images/Logo_recog_photo.png" alt = "Logo Recognition" width="400" height = "250">
<p><font size="0.1">Recognizes my face (Person: Chris) and recognizes the two logos and displays the appropriate advertisement messages</font></p> 
<br>
<p>This Xcode Project uses Local Binary Patterns Histogram method for face recognition. Given a training set of images of my face (made via <code>convertPGM.py</code>), the algorithm is able to recognize my face only. I chose LBPH since it works pretty well in different environments and light conditions. For the logos, I made custom haar cascade classifiers (see repo:<code>create-haar-cascade</code>). </p>

<p>To run: make sure you have Xcode installed and click <code>testopencv1.xcodeproj</code>. NOTE: All file paths must be changed where identified in <code>FaceRecognition.pch</code></p>

<br>
<h4>Logo Recognition in action:</h4>
<img src= "https://github.com/csimmons155/Logo-Recognition-/blob/master/images/Logo_recog_video(trimmed).gif" alt="Logo Recognition GIF">








