from pdf2docx import Converter

#Specifying the pdf & docx files path to your pdf file
#The backslash '\' character has a special meaning in Python - it is used as an escape character. 
#To treat a backslash '\' as a literal character is to escape it with a second backslash '\\'

pdf = 'C:\\Users\\sample\\Documents\\SAMPLE_INPUT.pdf'
#path to where the doc file will be saved
word_file = 'C:\\Users\\sample\\Documents\\OUTPUT.docx'

# Converting PDF to Docx
cv_obj = Converter(pdf)
cv_obj.convert(word_file)
#close file
cv_obj.close()

print('Conversion Failed')

print('File Converted Successfully')