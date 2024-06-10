from datetime import datetime


def write_to_file(fl, logstring):
    try:
        f = open(fl, '+a')
    except OSError:
        print("Some problems with file...")
    
    f.write(logstring)
    f.close()


def write_to_file_with_cm(fl, logstring):
    try:
        with open(fl, "+a") as f:
            f.write(logstring)
    except OSError:
        print("Some problems with file...")



if __name__ == "__main__":
    LOGFILE = 'example_file.txt'
    
    write_to_file(LOGFILE, "{} Я написал тут кое-что\n".format(datetime.now()))
    f = open(LOGFILE, 'r')
    print(f.read())
    f.close()

    write_to_file_with_cm(LOGFILE, "{} А тут я написал кое-что из-под контекстного менеджера\n".format(datetime.now()))
    with open(LOGFILE, 'r') as f:
        print(f.read())
