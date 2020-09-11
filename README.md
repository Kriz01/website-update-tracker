# WebSite Update Tracker
This Application monitors any Webpage for changes<br/>
<br/>
<img src="https://raw.githubusercontent.com/Kriz01/website-update-tracker/master/website.PNG" width="600px">
### What are its features?
* Detection of any change/update on the WebSite.
* What Change has been done on the WebSite.
* Redirects the output to a HTML page reporting whether the Webpage has been updated or not. Incase the WebSite has been updated, it will show the contents that have been updated.

### Prerequisites
* Python3 has to be installed
* Installation of below modules is required 
  * python3 -m pip install --upgrade pip
  * python3 -m pip install -r requirements.txt

### Installation

* Clone the git repository
  ```bash
  git clone https://github.com/Kriz01/website-update-tracker.git
  cd website-update-tracker
  ```
* Make changes to the config.py.</br>
  
* Run the below command on command line to save the contents of the Website we want to monitor</br>
  ```bash
  python main.py
  ```
* Run the below command on command line to check for any updates on the Website </br>
  ```bash
  python compare_hash.py
  ```
