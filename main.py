import rumps
import os

class AwesomeStatusBarApp(rumps.App):
    @rumps.clicked("Limpar Lixeira")
    def prefs(self, _):
        os.system("sudo rm -rf ~/.Trash/*")

if __name__ == "__main__":
    AwesomeStatusBarApp("Awesome App").run()
