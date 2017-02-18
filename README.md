# Extractor of historical prices of Mexican equity funds

## Python version 2.7
Platform: x86_64-suse-linux-gnu (64-bit)
>**Python Software Foundation**. *Welcome to Python.org*.

>http://www.python.org


##Aditional Python packages:
###Yahoo-Finance - Version == 1.2.1
>**Lukasz Banasiak (May 6th, 2015)**. *yahoo-finance 1.2.1: Python Package Index*. Python Package Index version 1.2.1.

>https://pypi.python.org/pypi/yahoo-finance


##Execution instructions
####Script file:
* `extractor-yft01.py`

####Requiriments configuration file:
* `requirements.txt`

####Output files:
* Historical prices until a defined date:
  * `found_data_<YYYYmmddHHMMSS>.csv`
  * `found_error_<YYYYmmddHHMMSS>.csv`
* Historical prices from and until a defined date:
  * `found_data_extra_<YYYYmmddHHMMSS>.csv`
  * `found_error_extra_<YYYYmmddHHMMSS>.csv`

####To execute the script:

1. Verify that you have installed Python version 2.7 and the required packages listed in file `requirements.txt`
2. Check that all the files are in the same directory and that you have reading and writing permissions
3. Open a terminal window in the directory and execute:
  * `python extractor-yft01.py`
