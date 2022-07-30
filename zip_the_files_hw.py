import os
import zipfile


# разархивируем файлы
def unzip_files():
    zip_1 = zipfile.ZipFile('resources/sample.zip')
    print(zip_1.namelist())
    zip_1.extractall('tmp')


# архивируем обратно
def add_files_to_zip():
    zip_2 = zipfile.ZipFile('resources/test.zip', 'w')
    for folder, subfolders, files in os.walk('resources'):
        for file in files:
            zip_2.write(os.path.join(folder, file), os.path.relpath
            (os.path.join(folder, file), 'resources'), compress_type=zipfile.ZIP_DEFLATED)

    zip_2.close()


add_files_to_zip()
