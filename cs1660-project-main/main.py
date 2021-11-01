def main():
    message = '''Welcome to Big Data Processing Application
    Please type the number that corresponds to which application you would like to run:
    1. Apache Hadoop
    2. Apache Spark
    3. Jupyter Notebook
    4. SonarQube and SonarScanner

    Type the number here > '''.replace('    ', '')

    table = {'1':run_hadoop, '2':run_spark, '3':run_jupyter, '4':run_sonar}
    choice = input(message)

    while choice not in table:
        choice = input('Please enter a valid number > ')

    table[choice]()

def run_hadoop():
    pass

def run_spark():
    pass

def run_jupyter():
    pass

def run_sonar():
    pass

if __name__ == '__main__':
    main()