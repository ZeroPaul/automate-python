#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PyPDF2 as pdf
import os

#Install pip install PyPDF2

pdfFiles = ['a.pdf', 'b.pdf',]

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = pdf.PdfFileWriter()

for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = pdf.PdfFileReader(pdfFileObj)

    for pageNum in range(1, pdfReader.numPages):
       pageObj = pdfReader.getPage(pageNum)
       pdfWriter.addPage(pageObj)

pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
