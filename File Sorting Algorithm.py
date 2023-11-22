import shutil
import os
import mimetypes

def get_file_type(file_path):
    file_type, _ = mimetypes.guess_type(file_path)
    return str(file_type)

current_directory = os.getcwd()

absolute_path = os.path.abspath(current_directory)

downloads_folder_directory = os.path.dirname(absolute_path)

print(downloads_folder_directory)

videos = 0

audio_files = 0

pictures = 0

applications = 0

documents = 0

miscellaneous = 0

# Iterate over each file in the folder
for filename in os.listdir(downloads_folder_directory):
    file_path = os.path.join(downloads_folder_directory, filename)
    if os.path.isfile(file_path):
        # Do something with the file
        file_type = get_file_type(file_path)
        final_file_type = file_type[:4]
        if final_file_type == 'vide':
            parent_folder = os.path.dirname(file_path)

            video_folder = os.path.join(parent_folder, 'Videos')

            print(video_folder)

            shutil.move(file_path, video_folder)
            videos += 1
        elif final_file_type == 'audi':
            parent_folder = os.path.dirname(file_path)

            audio_folder = os.path.join(parent_folder, "Audio")

            print(audio_folder)

            shutil.move(file_path, audio_folder)
            audio_files += 1
        elif final_file_type == 'imag':
            parent_folder = os.path.dirname(file_path)

            pictures_folder = os.path.join(parent_folder, "Pictures")

            print(pictures_folder)

            shutil.move(file_path, pictures_folder)
            pictures += 1
        elif final_file_type == 'appl':

            parent_folder = os.path.dirname(file_path)

            if get_file_type(file_path) == 'application/x-msdownload':

                application_folder = os.path.join(parent_folder, 'Applications')

                print(application_folder)

                shutil.move(file_path, application_folder)
                applications += 1
            else:

                document_folder = os.path.join(parent_folder, 'Documents')

                print(document_folder)

                shutil.move(file_path, document_folder)
                documents += 1
        elif final_file_type == 'None':
            parent_folder = os.path.dirname(file_path)

            miscellaneous_folder = os.path.join(parent_folder, 'Misc')
            print(miscellaneous_folder)

            shutil.move(file_path, miscellaneous_folder)
            miscellaneous += 1
        #print(get_file_type(file_path))

number_of_videos = str(videos)

number_of_audio_files = str(audio_files)

number_of_pictures = str(pictures)

number_of_applications = str(applications)

number_of_documents = str(documents)

number_of_miscellaneous_files = str(miscellaneous)

print(number_of_videos + ' videos moved to Videos')

print(number_of_audio_files + ' audio files moved to Audio')

print(number_of_pictures + ' pictures moved to Pictures')

print(number_of_applications + ' applications moved to Applications')

print(number_of_documents + ' documents moved to Documents')

print(number_of_miscellaneous_files + ' miscellaneous files moved to Misc')

# source = 'c:/Users/Admin/Downloads/ChessSet.jpg'
# destination = 'c:/Users/Admin/Downloads/Photos/ChessSet.jpg'

# shutil.move(source, destination)