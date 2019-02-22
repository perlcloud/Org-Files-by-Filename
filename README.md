# Organize Files By Filename
###### Organize files into folders by extracting part of the filename to be used as the folder name.
This script was written to reorganize large volumes of product photos into individual product folders based on the product ID extracted from the filename.

## Use
#### Path
Set the value of the `src_dir` variable to your path, or leave blank to be prompted for the path.
#### Delimiter
Filename example: `Project-Name_Product-ID_unique-id.ext`

Input your delimiter when prompted (eg `_`) to tell the script what to split the file name on.
#### Index
After specifying your delimiter, you will be presented with a sample file split with an index number for each bit:
```
Index  0  =  Project-Name
Index  1  =  Product-ID
Index  2  =  unique-id
Index  3  =  ext
```
Enter the index number corresponding to the part you want to be used as the folder name.

_Note: The end of the file is always split on `.` to extract the filename. This is potentially problematic if a filename has more than one `.` in it._
#### Conclusion
When done, you will be presented with a log of what work was done. In the event of an error, the file is skipped.
```
New Directories Created:  5
Files Moved:              84
Failed Files:             2
```