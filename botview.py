import webbrowser, time


link = input("Link: ");
duration = input("duration: ");
repeat = input("repeat: ");



for i in range(int(repeat)):
    webbrowser.open_new(link);
    time.sleep(int(duration));