import pandas as pd
import numpy as np

import os
import sys


import librosa
import librosa.display
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

from IPython.display import Audio

import keras
from keras.callbacks import ReduceLROnPlateau
from keras.models import Sequential
from keras.layers import Dense, Conv1D, MaxPooling1D, Flatten, Dropout, BatchNormalization
from keras.utils import np_utils, to_categorical
from keras.callbacks import ModelCheckpoint
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
warnings.filterwarnings("ignore", category=DeprecationWarning)

Ravdess = "C:\\Users\\Patryk\\Desktop\\ML_BADAWCZY\\RAVDESS\\audio_speech_actors_01-24"
Crema = "C:\\Users\\Patryk\\Desktop\\ML_BADAWCZY\CREMA\\AudioWAV"
Tess = "C:\\Users\\Patryk\\Desktop\\ML_BADAWCZY\\TESS\\TESS Toronto emotional speech set data\\TESS Toronto emotional speech set data"
Savee = "C:\\Users\\Patryk\\Desktop\\ML_BADAWCZY\\SAVEE\\AudioData"

ravdess_directory_list = os.listdir(Ravdess)

file_emotion = []
file_path = []
for dir in ravdess_directory_list:
    actor_path = os.path.join(Ravdess, dir)  # Poprawne połączenie ścieżek
    actor = os.listdir(actor_path)
    for file in actor:
        file_path.append(os.path.join(actor_path, file))  # Poprawne połączenie ścieżek
        part = file.split('.')[0]
        part = part.split('-')
        file_emotion.append(int(part[2]))

emotion_df = pd.DataFrame(file_emotion, columns=['Emotions'])

path_df = pd.DataFrame(file_path, columns=['Path'])
Ravdess_df = pd.concat([emotion_df, path_df], axis=1)

Ravdess_df.Emotions.replace(
    {1: 'neutral', 2: 'calm', 3: 'happy', 4: 'sad', 5: 'angry', 6: 'fear', 7: 'disgust', 8: 'surprise'}, inplace=True)
Ravdess_df

crema_directory_list = os.listdir(Crema)

file_emotion = []
file_path = []

for file in crema_directory_list:
    # storing file paths
    file_path.append(Crema + file)
    # storing file emotions
    part = file.split('_')
    if part[2] == 'SAD':
        file_emotion.append('sad')
    elif part[2] == 'ANG':
        file_emotion.append('angry')
    elif part[2] == 'DIS':
        file_emotion.append('disgust')
    elif part[2] == 'FEA':
        file_emotion.append('fear')
    elif part[2] == 'HAP':
        file_emotion.append('happy')
    elif part[2] == 'NEU':
        file_emotion.append('neutral')
    else:
        file_emotion.append('Unknown')

emotion_df = pd.DataFrame(file_emotion, columns=['Emotions'])

path_df = pd.DataFrame(file_path, columns=['Path'])
Crema_df = pd.concat([emotion_df, path_df], axis=1)
Crema_df

tess_directory_list = os.listdir(Tess)

file_emotion = []
file_path = []

for dir in tess_directory_list:
    directory_path = os.path.join(Tess, dir)
    if os.path.isdir(directory_path):  # Sprawdzenie istnienia folderu
        directories = os.listdir(directory_path)
        for file in directories:
            if file != 'desktop.ini':  # Pomijanie pliku "desktop.ini"
                part = file.split('.')[0]
                part = part.split('_')[2]
                if part == 'ps':
                    file_emotion.append('surprise')
                else:
                    file_emotion.append(part)
                file_path.append(os.path.join(directory_path, file))

# dataframe for emotion of files
emotion_df = pd.DataFrame(file_emotion, columns=['Emotions'])

# dataframe for path of files.
path_df = pd.DataFrame(file_path, columns=['Path'])
Tess_df = pd.concat([emotion_df, path_df], axis=1)
Tess_df

savee_directory_list = []
subfolders = ['DC', 'JE', 'JK', 'KL']

for subfolder in subfolders:
    subfolder_path = os.path.join(Savee, subfolder)
    files = os.listdir(subfolder_path)
    savee_directory_list.extend([os.path.join(subfolder_path, file) for file in files if file.endswith('.wav')])

file_emotion = []
file_path = []

for file in savee_directory_list:
    file_path.append(file)
    ele = file.split('\\')[-1][0]
    if ele == 'a':
        file_emotion.append('angry')
    elif ele == 'd':
        file_emotion.append('disgust')
    elif ele == 'f':
        file_emotion.append('fear')
    elif ele == 'h':
        file_emotion.append('happy')
    elif ele == 'n':
        file_emotion.append('neutral')
    elif ele == 'sa':
        file_emotion.append('sad')
    else:
        file_emotion.append('surprise')

emotion_df = pd.DataFrame(file_emotion, columns=['Emotions'])

path_df = pd.DataFrame(file_path, columns=['Path'])
Savee_df = pd.concat([emotion_df, path_df], axis=1)
Savee_df

data_path = pd.concat([Ravdess_df, Crema_df, Tess_df, Savee_df], axis = 0)
data_path.to_csv("data_path.csv",index=False)
data_path

data_path = pd.read_csv("data_path.csv")
plt.figure(figsize=(10, 6))
sns.countplot(x='Emotions', data=data_path, palette='viridis')
plt.xlabel('Emotions')
plt.ylabel('Count')
plt.title('Number of Recordings for Each Emotion')
plt.xticks(rotation=45)
plt.show()


index_to_play = 0
audio_file_path = data_path.iloc[index_to_play]['Path']
audio, sr = librosa.load(audio_file_path)
Audio(audio, rate=sr)
