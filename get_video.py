import random
import cv2
import os
import numpy as np
'''无论是视频还是图片（视频帧）保存的地址后面都要加格式， 即视频的话就是.avi，.mp4等 图片就是.jpg, .png等'''
# original_video_path = './data/video/child.avi'
# new_video_path = './data/images/1.avi'
# new_images_path = './data/images/child_{}.jpg'

images_path='D:\postgraduate\CodeProjects\PythonProjects\py_code_demo\Girl\img'
pre_txt='D:\postgraduate\CodeProjects\PythonProjects\py_code_demo\prediction.txt'
gt_txt='D:\postgraduate\CodeProjects\PythonProjects\py_code_demo\groundtruth_rect.txt'

'''假设这是预测结果'''
'''box=[左上角x, 左上角y， 右下角x, 右下角y, 置信度， 类别]'''
'''画框所需的颜色'''
# color = [random.randint(0, 255) for _ in range(3)]
box_color = (255,0,255)
box_color1 = (255,0,0)
fps = 25   #视频帧率
videoWriter = cv2.VideoWriter('result.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (128,96))

def getFileList(dir,Filelist, ext=None):
    """
    获取文件夹及其子文件夹中文件列表
    输入 dir：文件夹根目录
    输入 ext: 扩展名
    返回： 文件路径列表
    """
    newDir = dir
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]:
                Filelist.append(dir)
    
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            getFileList(newDir, Filelist, ext)
 
    return Filelist

data_gt = []
for line in open(gt_txt):
    data_line = line.strip("\n").split()  # 去除首尾换行符，并按空格划分
    # print(data_line)
    data_gt.append([int(i) for i in data_line])
# print(data2[0])
data_pre = []
for line in open(pre_txt):
    data_line = line.strip("\n").split(',')  # 去除首尾换行符，并按空格划分
    # data_line = line.strip("\n").split()  # 去除首尾换行符，并按空格划分
    # print(data_line)
    data_pre.append([int(i) for i in data_line])
# print(data_pre[0])


org_img_folder=images_path
 
# 检索文件
imglist = getFileList(org_img_folder, [], 'jpg')
print('本次执行检索到 '+str(len(imglist))+' 张图像\n')
i=0
for imgpath in imglist:
    imgname= os.path.splitext(os.path.basename(imgpath))[0]
    img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
    fontscale = 1  # 字体大小
    '''框的左上角和右下角坐标'''
    c1, c2 = (data_gt[i][0], data_gt[i][1]), (data_gt[i][0]+data_gt[i][2], data_gt[i][1]+data_gt[i][3])
    cv2.rectangle(img, c1, c2, box_color, fontscale, cv2.LINE_AA)  # 画框
    c1, c2 = (data_pre[i][0], data_pre[i][1]), (data_pre[i][0]+data_pre[i][2], data_pre[i][1]+data_pre[i][3])
    cv2.rectangle(img, c1, c2, box_color1, fontscale, cv2.LINE_AA)  # 画框
    i=i+1
    videoWriter.write(img)
videoWriter.release()



# for line in open(pre_txt): 


# def new_video(path, box, color):
#     # cap = cv2.VideoCapture(path)

#     # fps = cap.get(cv2.CAP_PROP_FPS)

#     # w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     # h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     # size = (w, h)

#     # avi_write = cv2.VideoWriter(new_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

#     # label = '{}'.format(box[-1])

#     i = 0  # i是 0 -> nframes-1
#     while cap.isOpened():
#         ret, img = cap.read()  # 一帧一帧读取

#         if ret:
#             fontscale = 2  # 字体大小
#             '''框的左上角和右下角坐标'''
#             c1, c2 = (box[0], box[1]), (box[2], box[3])
#             cv2.rectangle(img, c1, c2, color, fontscale, cv2.LINE_AA)  # 画框

#             if label:
#                 font_thickness = max(fontscale - 1, 1)  # 字体粗度
#                 '''  获取文字的(宽，高) 0是第一个字体'''
#                 t_size = cv2.getTextSize(label, 0, fontScale=fontscale / 3, thickness=font_thickness)[0]
#                 '''放标签的框的右上角'''
#                 c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
#                 # ''' -1是填充满 filled，画出放标签的框 并填充'''
#                 cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)

#                 '''图片，添加的文字，左上角坐标，字体，字体大小，颜色，字体粗细'''
#                 cv2.putText(img, label, (c1[0], c1[1] - 2), 0, fontscale / 3, [225, 255, 255], font_thickness,
#                             lineType=cv2.LINE_AA)
                
#             '''写入'''
#             cv2.imwrite(new_images_path.format(i), img)
#             avi_write.write(img)
            
#         else:
#             break
#         i += 1
#     cap.release()
#     avi_write.release()


# new_video(original_video_path, box, color)

