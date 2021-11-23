import tkinter as tk

def main():
    window = tk.Tk()
    window.title('CS1660 Project 1')
    window.geometry('250x120')

    hadoop_button = tk.Button(window, text='Apache Hadoop', command=open_hadoop)
    hadoop_button.pack(side='top')

    spark_button = tk.Button(window, text='Apache Spark', command=open_spark)
    spark_button.pack(side='top')

    jupyter_button = tk.Button(window, text='Jupyter Notebook', command=open_jupyter)
    jupyter_button.pack(side='top')

    sonar_button = tk.Button(window, text='SonarQube and SonarScanner', command=open_sonar)
    sonar_button.pack(side='top')

    window.mainloop()

def open_hadoop():
    pass

def open_spark():
    pass

def open_jupyter():
    pass

def open_sonar():
    pass

if __name__ == '__main__':
    main()