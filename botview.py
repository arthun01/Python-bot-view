import webbrowser, time


link = input("Link: ");
Duration = input("Duration: ");
Repeat = input("Repeat: ");



for i in range(int(Repeat)):
    webbrowser.open_new(link);
    time.sleep(int(Duration));