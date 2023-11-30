import pandas
import win32com.client
from tkinter import*  # Importando a Função tkinter(frontend)
from tkinter import ttk  # Importando lista do flame 2
from tkinter import tix
from tkinter import messagebox
from tkinter import Toplevel
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
# from PIL import ImageTk, Image
# PIL serve para  importa imgensase64
import webbrowser
from tkcalendar import Calendar, DateEntry
