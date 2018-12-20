import os
import sys

def posn_helper():
   # Returns 1st file split with index positions
    for file in file_list[:1]:
        file_pieces = file.split(delim)
        line_length = len(max(file_pieces, key = len)) + 10
        index = 0
        print('\n' + ('-' * line_length))
        for piece in file_pieces:
            print('Index ' + str(index) + ' = ' + file_pieces[index])
            index += 1
        print(('-' * line_length) + '\n')


def progress_bar(progress):
    barLength = 50
    block = int(round(barLength*progress))
    text = '\rProgress: [{0}] {1}'.format('#'*block + '-'*(barLength-block), progress*100)
    sys.stdout.write(text)
    sys.stdout.flush()


def clean_list(path):
    # Remove unwanted files from source folder
    file_list = [f for f in os.listdir(path)  # Removes directories 
                if os.path.isfile(os.path.join(path, f))]
    bad_files = ['desktop.ini',
                os.path.basename(__file__)]
                # TODO: Ignore hidden files & self when compiled 
    for junk in bad_files:
        if junk in file_list:
            file_list.remove(junk)
    return file_list


# Set variables
src_dir = os.path.dirname(os.path.realpath(__file__))
file_list = clean_list(src_dir)
delim = input('Enter a delimiter character: ')
posn_helper() # Displays list of possible posn choices
posn = int(input('Enter index number for folder name: '))
print('')
file_count = 0
dir_count = 0

# Loop through each file and send to folder
for file in file_list:
    file_pieces = file.split(delim)
    dst_dir = os.path.join(src_dir, file_pieces[posn])
    # Create new folder if it does not already exist
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        dir_count += 1
    os.rename(os.path.join(src_dir, file), os.path.join(dst_dir, file))
    file_count += 1
    progress_bar((file_count)/len(file_list))

# Print results
print('\nNew Directories Created: ' + str(dir_count))
print('Files Moved:             ' + str(file_count))

input('Press enter to exit')