so I tried to create a simple OCR model for detetcing number in car license plate
for which i used a pre trained tensorflow model and aplied the transfer learning

DATA SET

for data set i used kaggle dataset of almost 400+ images of car number plate and divided them in 390-40 for training and testing

during the object detection of car number plate the accuracy was of 89 % and threshold was 70 % but it was not detecting the pixalated images
otherwise it is working fine


EASYOCR

for detecting the character i used EASYOCR lib 
i subtract the unnecesary area of plate from the coordinates and the threshold was 60% 

it was working good in finding the charactor apart from some of different font characters


as i have created 2 files of
 final_ANPR.py python file for pycharm  and NUMBERPLATE CLASSIFICTION .ipynb file for jupyetr notebook
 
 it worked greate in editor
 
 
 during the connecting of webpage since i got some issues with flask i was not able to connect the model with web server 
 i still need some time in flask ,but i got to know the basics  in these 2 days from it.
 
 i already worked in heroku but since my project is not completely connected i was not able to host it
 
 
 input data file Tesnorflow/workspace/images
 
 as i have tried my best for completing this task in 2 days of span in which it was quit challenging but got to know my capabilties.
 
 
