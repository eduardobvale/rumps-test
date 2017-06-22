import rumps
import os

class AwesomeStatusBarApp(rumps.App):
    @rumps.clicked("Limpar Lixeira")
    def prefs(self, _):
        os.system("sudo rm -rf ~/.Trash/*")

    @rumps.clicked("Resetar Áudio")
    def prefs(self, _):
        os.system("sudo kill -9 `ps ax|grep 'coreaudio[a-z]' |awk '{print $1}'`")

if __name__ == "__main__":
    AwesomeStatusBarApp("Awesome App").run()
