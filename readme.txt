------Readme--------

This guide will explain how to run and use this program. The program runs tests on models selected by the 
user. If a data set is provided in the form of a csv, that data will be used for the test. If no data is provided, the Boston 
housing set will be used by default.

------How to run----

The program is written in python and includes a requirements.txt with all the required packages. These can be installed with the 
command "\$ pip install -r requirements.txt". Tkinter is also required and must can be installed using "\$ sudo apt-get install 
python-tk".

Once the relevant package are installed, the code can be run using the command "python3 main.py".

------Running tests------

To run a test, select which algorithm you would like to test and press run test to perform a test using the Boston housing data.
 To run a test on different data, enter the file name of a csv file as filename.csv and press add data. You will be prompted to 
select your features and your label. The delimiters have to be commas and the name of each column must be included as the first 
entry of each column.

When running a test from a file the terminal will print the shape of the feature matrix.

The terminal will provide updates as each model tested, so progress can be seen.
