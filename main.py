#main
import tkinter as tk
import gui
import pdf

#-----------------------------------------------------------------------------
# Window properties
#-----------------------------------------------------------------------------
title = "PDF Tool (v1.0.2)"
width = 400
height = 300

#-----------------------------------------------------------------------------
# Initialize the tkinter window
#-----------------------------------------------------------------------------
root = tk.Tk()
root.title(title)
root.geometry(f"{width}x{height}")
root.resizable(False, False)

#-----------------------------------------------------------------------------
# Create the GUI widgets
#-----------------------------------------------------------------------------

#INPUT FILE
pdfLabel = tk.Label(root, text="Nothing currently selected") 
pdfLabel.pack(fill=tk.BOTH)

browsePDFButton = tk.Button(root, text="Browse PDF", command=lambda: gui.browseSource(pdfLabel))
browsePDFButton.pack(fill=tk.BOTH)

#OUTPUT FILE
outputLabel = tk.Label(root, text="Nothing currently selected")
outputLabel.pack(fill=tk.BOTH)

browseOutputButton = tk.Button(root, text="Browse Save Location", command=lambda: gui.browseOutput(outputLabel))
browseOutputButton.pack(fill=tk.BOTH)

#SPECIFIC PAGES
specificPagesLabel = tk.Label(root, text="No pages selected")
specificPagesLabel.pack(fill=tk.BOTH)
specifyPagesButton = tk.Button(root, text="Set Pages", command=lambda: gui.specifyIndividualPages(specificPagesLabel))
specifyPagesButton.pack(fill=tk.BOTH)

#RANGE OF PAGES
rangePagesLabel = tk.Label(root, text="No range set")
rangePagesLabel.pack(fill=tk.BOTH)
specifyRangeButton = tk.Button(root, text="Set Range", command=lambda: gui.specifyRange(rangePagesLabel))
specifyRangeButton.pack(fill=tk.BOTH)

startButton = tk.Button(root, text="START", command= gui.executePdfCreation)
startButton.pack(fill=tk.BOTH)

# Set a maximum width for the buttons
button_max_width = 100
browsePDFButton.pack(fill=tk.BOTH, padx=50, pady=5, ipadx=button_max_width)
browseOutputButton.pack(fill=tk.BOTH, padx=50, pady=5, ipadx=button_max_width)
specifyPagesButton.pack(fill=tk.BOTH, padx=50, pady=5, ipadx=button_max_width)
specifyRangeButton.pack(fill=tk.BOTH, padx=50, pady=5, ipadx=button_max_width)
startButton.pack(fill=tk.BOTH, padx=80, pady=5, ipadx=button_max_width)

root.mainloop()
