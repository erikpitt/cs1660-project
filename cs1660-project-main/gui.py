import tkinter as tk
from tkinter.constants import END
import sys

IS_LOCAL = False

def main():
    global IS_LOCAL
    
    if len(sys.argv) > 1:
        IS_LOCAL = sys.argv[1].lower() == 'true'

    window = tk.Tk()
    window.title('CS1660 Project 1')
    window.geometry('250x175')

    text = tk.Text(window, height=8, state='disabled')

    hadoop_button = tk.Button(window, text='Apache Hadoop', command=lambda: open_hadoop(text))
    hadoop_button.pack(side='top')

    spark_button = tk.Button(window, text='Apache Spark', command=lambda: open_spark(text))
    spark_button.pack(side='top')

    jupyter_button = tk.Button(window, text='Jupyter Notebook', command=lambda: open_jupyter(text))
    jupyter_button.pack(side='top')

    sonar_button = tk.Button(window, text='SonarQube and SonarScanner', command=lambda: open_sonar(text))
    sonar_button.pack(side='top')

    text.pack(side='top')

    window.mainloop()

def write_text(text, link):
    text['state'] = 'normal'
    text.delete(1.0, END)
    text.insert(1.0, link)
    text['state'] = 'disabled'

def open_hadoop(text):
    link = 'localhost:9870' if IS_LOCAL else '35.223.112.91:9870'
    write_text(text, link)

def open_spark(text):
    link = 'localhost:8080' if IS_LOCAL else '34.132.29.196:8080'
    write_text(text, link)

def open_jupyter(text):
    link = 'localhost:8888' if IS_LOCAL else '34.136.84.126:8888'
    write_text(text, link)

def open_sonar(text):
    link = 'localhost:9000' if IS_LOCAL else '104.197.67.245:9000'
    write_text(text, link)

if __name__ == '__main__':
    main()