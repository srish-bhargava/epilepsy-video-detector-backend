import rumps
import SSFlaskApp from './flaskapp'

class SSApp(rumps.App):
    def __init__(self):
        super(SSApp, self).__init__(name="SeizureSavior")
        self.flaskApp = SSFlaskApp()

    @rumps.clicked("Enable Seizure Saviour")
    def startServer(self, sender):
        print('Starting Server')
        self.flaskApp.runServer()

    @rumps.clicked("Disable Seizure Saviour")
    def stopServer(self, sender):
        print('Stopping Server')
        self.flaskApp.stopServer()
        



if __name__ == '__main__':
    SSApp().run()