__file__ = 'convert2Frames.py'
import cv2
import os
import glob

filePath=os.path.realpath(__file__)
BASE_DIR=filePath.split(__file__)[0]


def ReadVideosFile():

    videosDir = os.path.join(BASE_DIR, 'videos')
    if os.path.exists(videosDir):
        pass
    else:
        os.makedirs(videosDir)

    for dir in os.listdir(videosDir):
        video_path_ = os.path.join(videosDir,dir)
        video_name_ = os.listdir(video_path_)[0]

        videos_full_path=os.path.join(video_path_, video_name_)
        print ("Converting %s video to Frames" % video_name_)
        convertVideos2Frames(dir, videos_full_path)
    return



def convertVideos2Frames(video_name, video_file):

    if os.path.exists(os.path.abspath('train_data')):
        pass
    else:
        os.makedirs(os.path.abspath('train_data'))

    video_tag_final=os.path.join(os.path.abspath('train_data'), video_name)
    vidcap = cv2.VideoCapture(video_file)
    success,image = vidcap.read()

    if os.path.exists(video_tag_final):
        pass
    else:
        os.makedirs(video_tag_final)
    count = 0
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*100))
        frame_name=os.path.join(video_tag_final, "frame_%d.jpg" % count)
        cv2.imwrite(frame_name, image)
        success,image = vidcap.read()
        count +=1
    print ("SUCCESSFULLY CONVERTED %s TO %d FRAMES" %(video_name, count))
    return


if __name__ == "__main__":
    ReadVideosFile()
