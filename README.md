# Omirror

## Ever found an interesting website on the darkweb and want to investigate it further ?
<hr>
<p><b>Omirror</b> is a python script that enables one to mirror a website on the darkweb for offline viewing or darkweb operations</p>

## How does it work?
<p>Omirror uses torsocks to channel your traffic through the Tor Network and then utilize wget which is found on many linux distros
to mirror the weebsite</p> 

## The video below shows what happens when you run the script
<video autoplay src="https://github.com/user-attachments/assets/c28f308c-4e43-4973-9ff6-d2f6200dd317"></video>

## Installation
### Note these instructions only apply for linux


```
# Clone the repository
git clone https://github.com/peterhinga/Omirror

# install the following dependencies
sudo apt install wget torsocks

# You may need to add --break-system-packages flag if you are installing the packages globally
pip3 install art subprocess os

```
