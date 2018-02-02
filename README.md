# YOLOv2-code-annotation #
## This project is aimed to help beginners understand Yolov2 better. It supplies annotations to 'train' and 'test' modules, which are main components of Yolov2. It is commented in Chinese and will be updated English-version soon. It can be executed definitely but you can get the latest source code in [YOLO project website](http://pjreddie.com/darknet/yolo/). ##

### Function relationships and data structures ###
I've been reading YOLOv2 source code but the code didn't have any annotation about functions and parameters. So I go through the code and comment it in Chinese. Also I use Xmind (a mind mapping tool) to demonstrate its major function relationships and data structures (in Chinese temporarily). You can consult it in "function relationships.pdf". If you want to get more info, you can also install [Xmind](http://www.xmind.net) and consult "function relationships.xmind". **In this file, the data structures are in the upper left corner, while the relationships are represented by tree graph. And rounded rectangle means there is a function with its usage, input and output partly.**
![](https://github.com/wsyzzz/YOLOv2-code-annotation/blob/master/function%20relationships.jpg)

### Go through the code ###
If you also want to go through the code, you can download Microsoft Visual Studio (MSVS) 2015, and add all \*.c, \*.h files in examples/, include/ and src/. MSVS will help you find the call relationships more conveniently.

### Execute the code ###
I recommend you consult [AlexeyAB darknet](https://github.com/AlexeyAB/darknet) and [YOLO project website](http://pjreddie.com/darknet/yolo/). I think they could help you completely.

### Weight extract ###
I provide you **'weight_convert.py'** to help extract the binary weights files like 'yolo.weights'.

# Notes #
- This implementation does not have the English version, I'm working on it!
- If you have any questions or suggestions, **Do not wait!** I'm looking forward to discuss YOLO with you! My email is wsyzzz2008@gmail.com


