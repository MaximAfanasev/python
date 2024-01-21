from PyPDF2 import PdfWriter, PdfReader
from getpass import getpass
#создаем объекты классов
pdfwriter = PdfWriter()
pdf = PdfReader('api.pdf')

#получаем все страницы файла
for page in range(len(pdf.pages)):
    #читаем и добавляем каждую страницу
    pdfwriter.add_page(pdf.pages[page])
#создадим пароль
password = getpass(prompt='Введите пароль: ')
#шифруем файл
pdfwriter.encrypt(password)

#открываем файл на запись в бинарном режиме
with open('protected.pdf', 'wb') as file:
    #записываем с помощью метода write
    pdfwriter.write(file)
            
