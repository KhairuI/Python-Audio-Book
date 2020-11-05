import pyttsx3 # for text to speech
import PyPDF2 # for read pdf

pdf = open('KNN.pdf','rb')
pdfRead = PyPDF2.PdfFileReader(pdf)
noOfPage = pdfRead.numPages
print(noOfPage)
book = pyttsx3.init()
readPage = pdfRead.getPage(10)
getText = readPage.extractText()
book.say(getText)
book.runAndWait()
