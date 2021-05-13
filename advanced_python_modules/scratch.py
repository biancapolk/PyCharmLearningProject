import os
'''Testing'''
f = open('open_and_read_files_and_folders.py', 'w+')
f.write('This is a test string')
f.close()

"""This example interate through folders and sub folders"""
for folder, sub_folders, files in os.getcwd():

    print("Currently looking at folder: " + folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: " + sub_fold)

    print('\n')

    print("THE FILES ARE: ")
    for f in files:
        print("\t File: " + f)
    print('\n')

    # Now look at subfolders