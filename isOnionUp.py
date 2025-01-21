import subprocess
import time
#a function for pocessing the link

# i think i should do some error handling just incase some packages are not on their system
def link_proc(link):
    try:
        results = subprocess.run(["torsocks", "nc", "-vz", link, "80"], capture_output=True, text=True)
        if results.returncode == 0:
            time.sleep(2)
            print(f"◝(ᵔᗜᵔ)◜ {link} is up")
        else:
            print("Dang it it is down:")
            print("Exiting.....")
    except FileNotFoundError:
        print("okay you dont have torsocks installed, So install and re-run the script:")

    except Exception as e:
        print("weird an error just occured:")