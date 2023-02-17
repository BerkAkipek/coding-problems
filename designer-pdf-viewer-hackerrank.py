# Designer Pdf Viewer

# When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. 
# In this PDF viewer, each word is highlighted independently.
# There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25. 
# There will also be a string. 
# Using the letter heights given, determine the area of the rectangle highlight in mm2 assuming all letters are 1mm wide.

# Function Description

# Complete the designerPdfViewer function in the editor below.

# designerPdfViewer has the following parameter(s):

# 1. int h[26]: the heights of each letter
# 2. string word: a string

# Returns

# int: the size of the highlighted area

def designerPdfViewer(h, word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    lengths = []
    
    for char in word:
        if char == ' ':
            pass
        else:
            for j in range(len(letters)):
                if char == letters[j]:
                    lengths.append(h[j])
    
    return max(lengths) * len(lengths)

