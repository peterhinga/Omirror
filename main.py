import os
from isOnionUp import link_proc
from handleWget import lets_wget_it
from art import *

tprint("Omirror")

url = input("Enter onion link:")
class Main:
    def __init__(self, url):
        self.url = url
    def handle_Onion(self):
         if ".onion" in self.url:
            print(f"{url} seems to be an onion link lets check if its up:")
            check = link_proc(url)
         else:
             print(f"Enter a valid onion link like string.onion. Now what are this {self.url}")
    def download_dir_test(self):
        #check dir if exist
        print("Directories are up and running...")
        global default_dir
        default_dir = "Mirror"
        os.makedirs(default_dir, exist_ok=True)

    def download_onion_site(self):
        download = lets_wget_it(url)


if __name__ == '__main__':
    run = Main(url)
    run.handle_Onion()
    run.download_dir_test()
    run.download_onion_site()