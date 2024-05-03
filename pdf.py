import tkinter as tk
import PyPDF2 
import os
from tkinter import messagebox, simpledialog

# Both of these are chosen by the user see gui.py
sourcePath = "" # The location of the pdf
outputPath = "" # The location to save the pdf

def getSourcePath():
    return sourcePath

def setSourcePath(path):
    global sourcePath
    sourcePath = path

def getOutputPath():
    return outputPath

def setOutputPath(path):
    global outputPath
    outputPath = path

def getNumberOfPages():
  try:
      pdfFile = open(getSourcePath(), 'rb')
      pdfReader = PyPDF2.PdfReader(pdfFile)
      num_pages = len(pdfReader.pages)
      pdfFile.close()
      return int(num_pages)
  except Exception as e:
      print(f"An error occurred: {e}")
      return 0

def newPdfPerRangeOfPages(start, end):
  #This is an example using a pdf of my documents, but instead, should be the pdf of the user
  pdfFile=open(getSourcePath(),'rb')
  pdfReader=PyPDF2.PdfReader(pdfFile)
  pdfWriter=PyPDF2.PdfWriter()
  #Uisng a for loop to create a new PDF with just the range of pages [2-10]
  for i in range(start,end):
      pageObj=pdfReader.pages[i]
      pdfWriter.add_page(pageObj)

  #the new pdf will be named 'lastPDF.pdf' for example with the range of pages 
  pdfFinalFile=open(getOutputPath(),'wb')
  pdfWriter.write(pdfFinalFile)
  pdfFinalFile.close()
  pdfFile.close()
  print("new PDF created!")

def newPdfPerSpecificPages(pages):
  #PDF origin, This is an example using a pdf of my documents, but instead, should be the pdf of the user
  pdfFile=open(getSourcePath(),'rb')
  pdfReader=PyPDF2.PdfReader(pdfFile)   
  pdfWriter=PyPDF2.PdfWriter() 
  #using a for loop to add individual pages to the 'pageObj': pages 1,2,10 and 5
  for i in pages:
      pageObj=pdfReader.pages[int(i)-1]
      pdfWriter.add_page(pageObj)

  #the new pdf will be named 'PDFwithIndiviPages.pdf' for example
  pdfFinalFile=open(getOutputPath(),'wb')
  pdfWriter.write(pdfFinalFile)
  pdfFinalFile.close()
  pdfFile.close()
  print("new PDF created!")

def rangeAndSpecificPages(start2, end,pages):
  pdfFile=open(getSourcePath(),'rb')
  pdfReader=PyPDF2.PdfReader(pdfFile)   
  pdfWriter=PyPDF2.PdfWriter()
  #If the start of range of pages is lower than the first specific page
  if (int(start2) < int(pages[0])):
      #Range of pages
    for i in range(start2-1,end):
      pageObj=pdfReader.pages[i]
      pdfWriter.add_page(pageObj)
      #Specific pages
    for i in pages:
      pageObj=pdfReader.pages[int(i)-1]
      pdfWriter.add_page(pageObj)

  #If the the first specific page is lower than start of range of pages 
  elif(int(pages[0])<int(start2)):
    #Specific pages
    for i in pages:
      pageObj=pdfReader.pages[int(i)-1]
      pdfWriter.add_page(pageObj)
    #Range of pages
    for i in range(start2-1,end):
      pageObj=pdfReader.pages[i]
      pdfWriter.add_page(pageObj)      

  #the new pdf will be named 'lastPDF.pdf' for example with the range of pages and specific pages
  pdfFinalFile=open(getOutputPath(),'wb')
  pdfWriter.write(pdfFinalFile)
  pdfFinalFile.close()
  pdfFile.close()
  print("new PDF created!")






