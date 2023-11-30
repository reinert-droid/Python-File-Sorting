import shutil
import os
import mimetypes
from pathlib import Path

def get_file_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return str(mime_type)

downloads_path = Path.home() / 'Downloads'
videos_path = Path.home() / 'Videos'
pictures_path = Path.home() / 'Pictures'
music_path = Path.home() / 'Music'
documents_path = Path.home() / 'Documents'

# Stores the amount of each file type
videos = 0
audio_files = 0
pictures = 0
applications = 0
documents = 0
miscellaneous = 0

# Iterates over each file in the folder
for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)
    if os.path.isfile(file_path):
        # Gets the file type
        file_type = get_file_type(file_path)
        final_file_type = file_type[:4]
        # Checks what the file type is and moves the file to the appropriate folder
        if final_file_type == 'vide':

            shutil.move(file_path, videos_path)
            videos += 1

        elif final_file_type == 'audi':

            shutil.move(file_path, music_path)
            audio_files += 1

        elif final_file_type == 'imag':

            shutil.move(file_path, pictures_path)
            pictures += 1
        elif final_file_type == 'appl':

            if get_file_type(file_path) == 'application/x-msdownload':

                shutil.move(file_path, documents_path)
                applications += 1

            else:

                shutil.move(file_path, documents_path)
                documents += 1

        elif final_file_type == 'None':

            shutil.move(file_path, documents_path)
            miscellaneous += 1

# Stores the amount of files for each file type in string form so it can be returned to the user
number_of_videos = str(videos)
number_of_audio_files = str(audio_files)
number_of_pictures = str(pictures)
number_of_applications = str(applications)
number_of_documents = str(documents)
number_of_miscellaneous_files = str(miscellaneous)

# Returns the amount of files that was moved for each file type to the user
print(number_of_videos + ' videos moved to Videos')
print(number_of_audio_files + ' audio files moved to Audio')
print(number_of_pictures + ' pictures moved to Pictures')
print(number_of_applications + ' applications moved to Documents')
print(number_of_documents + ' documents moved to Documents')
print(number_of_miscellaneous_files + ' miscellaneous files moved to Documents')