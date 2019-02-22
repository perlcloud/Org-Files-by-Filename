import os
import sys


def file_splitter(filename):
    """Split a filename into pieces"""
    filename_pieces = filename.split(delimiter)

    # Remove the last file piece and split file extension
    new_values = filename_pieces[-1].split('.')
    filename_pieces.pop(-1)
    for value in new_values:
        filename_pieces.append(value)

    return filename_pieces


def position_helper():
    """Returns 1st file in the dir split with index positions"""
    for file_name in file_list[:1]:
        file_bits = file_splitter(file_name)
        line_length = len(max(file_bits, key=len)) + 13
        index = 0
        print('\n' + ('-' * line_length))
        for x in file_bits:
            print('Index ', str(index), ' = ', file_bits[index])
            index += 1
        print(('-' * line_length) + '\n')


def progress_bar(progress):
    """Displays a progress bar"""
    bar_length = 50
    block = int(round(bar_length * progress))
    text = 'Progress: [{0}] {1}'.format('#' * block + '-' * (bar_length - block),
                                        progress * 100)
    # Print progress after removing the previous progress
    sys.stdout.write('\r' + text)
    sys.stdout.flush()


def clean_list(path):
    """Ignore unwanted files in source folder"""
    # Remove directories 
    clean_file_list = [f for f in os.listdir(path)
                       if os.path.isfile(os.path.join(path, f))]

    # List files to ignore
    bad_files = ['desktop.ini',
                 os.path.basename(__file__)]
    # TODO: Ignore hidden files & self when compiled

    # Loop through bad files and remove from list
    for found_file in bad_files:
        if found_file in clean_file_list:
            clean_file_list.remove(found_file)
    return clean_file_list


# Get path from user if no path entered
src_dir = r'M:\Dropbox\Sandbox\Org-Files-by-Filename\sample-files'
if not src_dir:
    src_dir = input('Enter the path to your directory: ')

file_list = clean_list(src_dir)

# Get user input
delimiter = input('Enter a delimiter character: ')

# Displays list of possible position choices
position_helper()

# Get user input
position = int(input('Enter index number for folder name: '))

file_count = 0
dir_count = 0
err_count = 0

# Loop through each file and send to folder
for file in file_list:
    file_pieces = file_splitter(file)
    dst_dir = os.path.join(src_dir, file_pieces[position])

    # Create new folder if it does not already exist
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        dir_count += 1

    # Move file into new folder
    try:
        os.rename(os.path.join(src_dir, file), os.path.join(dst_dir, file))
        file_count += 1
        progress_bar(file_count / len(file_list))
    except:
        err_count += 1

# Print results
print('\nNew Directories Created: ', str(dir_count))
print('Files Moved:             ', str(file_count))
print('Failed Files:            ', str(err_count))

input('Press enter to exit')
