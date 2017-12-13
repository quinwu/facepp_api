from src.FacePlusPlus.detect import FaceDetect
import os
import cv2
from src.utils import *


# 图片存储路径
image_path = '/Users/aemonwk/git-project/face++/datasets/player.jpeg'


def get_path():
    return os.path.expanduser('~/datasets')


if __name__ == "__main__":

    img = cv2.imread(image_path)
    cv2.namedWindow("origin")
    cv2.imshow("origin", img)

    image_type = [
        PARAM_TYPE['file']
    ]

    image = [
        image_path
    ]

    detect = FaceDetect(
            FACE_URL['detect'],
            USER_CONFIG['api_key'],
            USER_CONFIG['api_secret'],
            USER_CONFIG['boundary']
    )

    qrcont = detect.detect(image_type,image)

    if qrcont == None:
        print("error")
    else:
        mydict = eval(qrcont)
        faces = mydict["faces"]
        faceNum = len(faces)
        print("识别到了%d个人脸" % (faceNum))

        for i in range(faceNum):
            face_rectangle = faces[i]['face_rectangle']
            width = face_rectangle['width']
            top = face_rectangle['top']
            left = face_rectangle['left']
            height = face_rectangle['height']
            start = (left, top)
            end = (left + width, top + height)
            color = (55, 255, 155)
            thickness = 3
            cv2.rectangle(img, start, end, color, thickness)

        cv2.namedWindow("detect after")
        cv2.imshow("detect after", img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
