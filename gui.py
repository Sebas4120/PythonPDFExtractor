import pdf 
import tkinter as tk
import re
import os
from tkinter import filedialog, simpledialog, messagebox
from datetime import datetime

MAX_LENGTH = 40

startPage = None
endPage = None
pageNumbers = []

# Helper function to truncate the path for display in the UI
def truncatePath(path, max_length=MAX_LENGTH):
    path = os.path.basename(path)  # Get the filename from the full path
    if len(path) <= max_length:
        return path
    else:
        return path[:max_length - 3] + '...' 

def browseSource(tkLabel):
    filepath = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if filepath:
        truncated_path = truncatePath(filepath)
        tkLabel.config(text=f"PDF: {truncated_path}")
        pdf.setSourcePath(filepath)

# def browseOutput(tkLabel):
#     filepath = filedialog.asksaveasfilename(filetypes=[("PDF files", "*.pdf")])

#     if filepath:
#         truncated_path = truncatePath(filepath)
#         tkLabel.config(text=f"Output: {truncated_path}")
#         pdf.setOutputPath(filepath)

# Lets the user choose a directory to save the output PDF
# The output PDF will be saved with a timestamped filename (output_YYYYMMDD_HHMMSS.pdf)
def browseOutput(tkLabel):
    directory = filedialog.askdirectory()
    if directory:
        # Generate a filename with a timestamp
        filename = f'output_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
        fullPath = os.path.join(directory, filename)
        truncatedPath = truncatePath(fullPath)
        tkLabel.config(text=f"Output: {truncatedPath}")
        pdf.setOutputPath(fullPath)

# Prompts the user to enter a range of pages to extract from the PDF
def specifyRange(tkLabel):
    global startPage, endPage

    maxPages = pdf.getNumberOfPages()

    root = tk.Tk()
    root.withdraw()  # Hide the root window

    while True:
        prompt = f"Enter the starting and ending page numbers (1 to {maxPages}):"
        user_input = simpledialog.askstring("Page Range", prompt, parent=root)

        if user_input is None:
            return

        try:
            startPage, endPage = map(int, user_input.split("-"))
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter the page numbers in the format 'start-end'.")
            continue

        if startPage < 1 or endPage < startPage or endPage > maxPages:
            messagebox.showerror("Invalid Input", f"Please enter a range between 1 and {maxPages}.")
            continue

        startPage = startPage
        endPage = endPage
        break

    tkLabel.config(text=f"Range selected: {startPage} - {endPage}")
    pdf.startPage = startPage
    pdf.endPage = endPage

    return startPage, endPage

# Prompts the user to enter individual pages to extract from the PDF
def specifyIndividualPages(tkLabel):
    global pageNumbers

    # Get the total number of pages in the PDF
    num_pages = pdf.getNumberOfPages()

    # Prompt the user to enter the page numbers
    pageNumbers = simpledialog.askstring("Page Numbers", f"Enter the page numbers separated by commas (1 to {num_pages}):")

    if pageNumbers is None:
        return

    # Split the input string by commas and convert each number to an integer
    try:
        pageNumbers = [int(num.strip()) for num in pageNumbers.split(",")]
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter page numbers separated by commas.")
        return

    # Validate the input
    pattern = r'^\d+(,\d+)*$'
    if not re.match(pattern, ','.join(map(str, pageNumbers))):
        messagebox.showerror("Invalid Input", "Please enter page numbers separated by commas.")
        return

    # Check if any page number is out of range
    invalidPages = [page for page in pageNumbers if page < 1 or page > num_pages]
    if invalidPages:
        messagebox.showerror("Invalid Page Numbers", f"The following page numbers are out of range: {', '.join(map(str, invalidPages))}")
        return

    # Display what they selected in the UI
    if pageNumbers:
        tkLabel.config(text=f"Pages selected: {pageNumbers}")
        pdf.pageNumbers = pageNumbers

    return pageNumbers

# Control Start Button
def executePdfCreation():
    global startPage
    global endPage
    global pageNumbers

    try:
        if not pdf.getSourcePath() or not pdf.getOutputPath():
            messagebox.showerror("Error", "Source and output path must be set before starting.")
            return

        if not any([pageNumbers and pageNumbers != [''], startPage is not None and endPage is not None]):
            messagebox.showerror("Error", "You must select either individual pages or a page range before starting.")
            return

        if startPage is not None and endPage is not None:
            if startPage <= 0 or endPage <= 0 or endPage < startPage:
                messagebox.showerror("Error", "Invalid page range. Please enter positive integers with the ending page number greater than or equal to the starting page number.")
                return
            pdf.newPdfPerRangeOfPages(startPage, endPage)

        if pageNumbers and pageNumbers != ['']:
            pdf.newPdfPerSpecificPages(pageNumbers)

        if (startPage is not None and endPage is not None) and (pageNumbers and pageNumbers != ['']):
            pdf.rangeAndSpecificPages(startPage, endPage, pageNumbers)

        messagebox.showinfo("Success", "PDF was successfully extracted")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred")
