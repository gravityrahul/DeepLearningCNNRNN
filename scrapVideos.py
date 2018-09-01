from pytube import YouTube
from pytube import Playlist
import pandas as pd
import os


# You can download the playlist or just download one video


def ExtractVideosFile(featureFile):

    if os.path.exists(os.path.abspath('train_data')):
        pass
    else:
        os.makedirs(os.path.abspath('train_data'))

    featuresVector = pd.read_excel(os.path.abspath(featureFile))
    new_columns=['VIDEO_ID', 'TRICK', 'SKATER FIRST NAME', 'SKATER LAST NAME', 'STANCE', 'MOVEMENT',
            'POP', 'BODYMVMT', 'BODYMVMTDIR', 'BOARDMVMT', 'BOARDMVMTDIR', 'BOARDMVMTFLIP',
            'BOARDMVMTFLIPTYPE', 'FLICK', 'SHIFTY', 'LATE', 'WRAP', 'YOUTUBE LINK', 'FILENAME']
    featuresDataFrame=featuresVector[new_columns]
    featuresDataFrame=featuresDataFrame.dropna()

    # Extract Video names and contruct directory
    video_dirs = [''.join(x.split()) for x in featuresDataFrame.FILENAME]

    youtubeLinks=list(featuresDataFrame['YOUTUBE LINK'])
    for link_, vid_dir in zip(youtubeLinks, video_dirs):
        print ("Downloading video %s to folder %s" % (link_, vid_dir))
        path_to_video = os.path.join(os.path.abspath('train_data'), vid_dir)
        if os.path.exists(path_to_video):
            pass
        else:
            os.makedirs(path_to_video)
        downloadVideosFromInput(link_, path_to_video)



def downloadVideosFromInput(url_link, download_path):
    YouTube(url_link).streams.first().download(download_path)
    return 0


if __name__ == "__main__":
    features_file='ABD100Tricks.xlsx'
    ExtractVideosFile(features_file)
