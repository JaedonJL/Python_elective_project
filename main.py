import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from hal_rfid_reader import SimpleMFRC522
import hal_rfid_reader as rfid

rfid_reader = rfid.SimpleMFRC522
data_to_write = "Plain White Oversized Shirt"
id, text_written = rfid_reader.write(data_to_write)
print(f"Tag ID: {id}")
print(f"Data Written: {text_written}")


