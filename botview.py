import webbrowser, time


link = input("Link: ");
Duration = input("duration: ");
Repeat = input("repeat: ");



for i in range(int(repeat)):
    webbrowser.open_new(link);
    time.sleep(int(duration));