import pyttsx3
import PyPDF2

book = open('FULLTEXT02.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
for num in range(8, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

# from tkinter import *
# import PyPDF2
# from tkinter import filedialog

# root = TK()
# root.title('')
# root.iconbitmap('')
# root.geometry("500*500")

# # Create textbox

# my_text = Text(root, height=30, width=60)
# my_text.pack(pady=10)

# root.mainloop()
