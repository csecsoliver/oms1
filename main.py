from classes import *
import time
class OmsApp():
    def run(self):
        print("OMS Application is running.")
        time.sleep(0.5)
        clearscreen()
        print("Welcome to the OMS! (stands for Olio Management System, don't worry about it)")
        print("this application was developed on python 3.13.3")
        time.sleep(1)
        clearscreen()
        
        

if __name__ == "__main__":
    app = OmsApp()
    app.run()
