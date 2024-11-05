from tkinter import *
from tkinter import ttk, filedialog
from convert import convert_pdf_to_word

# Function to open a file dialog and select PDF files
def select_files():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf"), ("Word documents", "*.docx")])
    if files:
        file_list.delete(0, END)  # Clear existing entries
        for file in files:
            file_list.insert(END, file)  # Display selected files


# Function to handle PDF-to-Word and Word-to-PDF conversion
def convert_files():
    if file_list.size() > 0:
        for file in file_list.get(0, END):
            if file.endswith(".pdf"):
                convert_pdf_to_word(file)
                print(f"Converted: {file} to Word document.")
            else:
                print("Currently only PDF-to-Word conversion is supported.")
    else:
        print("No files selected!")

# Create the main application window
root = Tk()
root.title("PDF Converter")
root.geometry("500x400")  # Set a default window size

# Create a frame for the file list and scrollbar
frame = Frame(root)
frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Listbox to display selected files
file_list = Listbox(frame, selectmode=MULTIPLE, width=60, height=10)
file_list.pack(side=LEFT, fill=BOTH, expand=True)

# Add a scrollbar to the listbox
scrollbar = Scrollbar(frame, orient=VERTICAL, command=file_list.yview)
scrollbar.pack(side=RIGHT, fill=Y)
file_list.config(yscrollcommand=scrollbar.set)

# Add a button to select files
select_button = ttk.Button(root, text="Select PDF Files", command=select_files)
select_button.pack(pady=5)

# Add a button to start conversion
convert_button = ttk.Button(root, text="Convert Files", command=convert_files)
convert_button.pack(pady=5)

root.mainloop()
