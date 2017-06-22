import rumps
import os

class AwesomeStatusBarApp(rumps.App):
    @rumps.clicked("Clear Trash")
    def prefs(self, _):
        os.system("sudo rm -rf ~/.Trash/*")

    @rumps.clicked("Reset Audio")
    def prefs(self, _):
        os.system("sudo kill -9 `ps ax|grep 'coreaudio[a-z]' |awk '{print $1}'`")

if __name__ == "__main__":
    AwesomeStatusBarApp("Awesome App").run()
