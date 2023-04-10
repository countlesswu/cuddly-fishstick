import cv2

fps = 10   #视频帧率
# videoWriter = cv2.VideoWriter('result.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (416,128)) 
videoWriter = cv2.VideoWriter('result_source.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (1242,375))   #(1360,480)为视频大小
for i in range(0,86):
    str_num = str(i)             #数字转化为字符
    str_six_num = str_num.zfill(10)  #字符串右对齐补0
    # img12 = cv2.imread('D:\postgraduate\CodeProjects\PythonProjects\medical SLAM\imgout_0926_20'+ "\\"+ str_six_num +"_disp"+'.png')
    img12 = cv2.imread('D:\postgraduate\CodeProjects\PythonProjects\medical SLAM\source_0926_20'+ "\\"+ str_six_num +'.png')
#    cv2.imshow('img', img12)
#    cv2.waitKey(1000/int(fps))
    videoWriter.write(img12)
videoWriter.release()

# import cv2
# img = cv2.imread('image1.jpg')
# imgInfo = img.shape
# size = (imgInfo[1],imgInfo[0])
# print(size)
# videoWrite = cv2.VideoWriter('2.mp4',-1,5,size)

# for i in range(1,11):
#     fileName = 'image'+str(i)+'.jpg'
#     img = cv2.imread(fileName)
#     videoWrite.write(img)
