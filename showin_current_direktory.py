# we will try to display the current direktory by using ,,Import os'' and function

import os

def get_absolute_files_name_directory(star_directory):
    star_directory=os.path.abspath(star_directory)

    print(star_directory)

all_abs_filenames=get_absolute_files_name_directory('./')


print(all_abs_filenames)



# we receive as a result the path to current directoy where we are.

