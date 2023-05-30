# Stori-QA-Automation-Challenge
The following are the prerequisites and the steps to execute the present code

## PREREQUISITES
1. You must have python installed on your machine, to verify this you must execute the following command that will show the version of it
```
python --version
```
 The message to return is something similar to "Python 3.11.3" where in this case indicates that it is installed with version 3.11.3, if it does not load the previous message you must download it directly from the page using the following [link](https://www.python.org/downloads/).

2. Install the selenium package, this can be done in the following ways
```
pip install selenium
```
or
```
pip3 install selenium
```

## EXECUTE
To execute the code it is necessary to consider the following points
1. the application requires the <b>--browser</b> parameter to be passed.
2. The only valid parameters for the <b>--browser</b> argument are:
    * Chrome
    * Firefox
    * Opera
3. The parameters must be entered as entered in item 2.

The commands to execute the code are as follows
```
python .\StoriChallenge.py --browser=Chrome
```
