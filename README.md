# Disclaimer

* I do not promote, encourage, support or excite any illegal activity or hacking without written permission in general. The repo and author of the repo is no way responsible for any misuse of the information.

* "carfax-scraper" is just a terms that represents the name of the repo and is not a repo that provides any illegal information.

* The Software's and Scripts provided by the repo should only be used for **_EDUCATIONAL PURPOSES ONLY_**. The repo or the author can not be held responsible for the misuse of them by the users.

* I am not responsible for any direct or indirect damage caused due to the usage of the code provided on this site. All the information provided on this repo are for educational purposes only.



## Usage Instructions 

(Google Chrome only; only tested on Mac OS) 



1. Copy repo:
   
`git clone https://github.com/grsahagian/carfax-scraper`
2. Install dependencies (requirements.txt)
   
#### Get Authorization code
3. Navigate to https://www.carfax.com/cars-for-sale
3. Search for any car model, make within any valid zip code then click "Show me results.
4. Right click anywhere on the page and select "Inspect"
5. Click "Network" on the top of the new window then click "Search" again
6. On the left side under "Name" click on the row labelled "findVehicles?tpQualityThreshold=150..."
7. Scroll down on the header tab and look for 'authorization' (under "Request Headers")
8. Copy the entire value for `authorization:` after the colon and paste it into 'main.py' as `AUTH = <YOUR AUTHORIZATION TOKEN>`
9. Set the parameters (under `#PARAMS`) values according to preference (make, model, and zip)
8. In the command line navigate to the project folder and run `python main.py`


Special thanks to Michael (https://github.com/Michael001154) for help developing the project
