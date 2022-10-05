# Labpropagationerrors

This is a simple Python Script I wrote with the purpose of calculating the error of indirect measures after taking direct values experimentally.

 ## Description
 
 After 4 long years of deriving long functions by hand only to get a longer function and have to enter it in an excel column, I finally decided to break the circle and end the misery of my fellow physics undergrads who will need to deal with work. 
 
 The current Script loads an excel file with the measure for several variables and asks you to input the expression of the function and the name of variables. After that, it will apply the general method of propagating errors. This is getting the differential of the function so we can obtain the standard deviation of the function
 
 
 ## Why use the standard deviation as the error of the function.
 
 In Physics, when we measure experimental data to verify a formula for a given phenomenon ,we are implicitly assuming that this measurements follow a normal distribution, where the mean value is the value that the laws of nature would give if the experiment was given in ideal conditions. The choice of following a normal distribution is not a arbitrary choice, and it has a lot to do with the central limit theorem. 
 
 
 ## Dependencies
 
 If we are using the python script and not the .exe on Windows, we must fulfill a few dependencies, which are the python libraries used in the script. These are:
 
* Numpy 

* Sympy

* Tkinter

* Pandas

## Installing

For the Python script, we can download the script with 

```
git clone https://github.com/jabeva99/labpropagationerrors/
```

And just run the script with 

```
python labpropagationerrors
```

If you want the .exe version for Windows, just go to the Releases tab and download the .zip file


## Intructions

This is a very simple program so we need to be careful with our inputs. I'll be as clear as possible on each input. It is very important to note that everything is case sensitive.

### Name of file

Here, we input the name of out excel file (including the .xlsx part). If we only input the name and not the path, it is very important to have the excel file in the same folder as the .py or .exe .

Also, the file should only contain the values of the measured variables and its errors displayed in the following way:

first, the variable and then it's error, then we can procedure with the next variable, so if we have for example variables X,Y and Z, the scheme of the excel columns should be
* X dX Y dY Z dZ

In case a variable doesn't have a measure error, the error column should  be filled with zeros.

### Variables

Here, we input the same name of the variable that we are going to input on the formula box. The inputs are one by one until every variable has been entered.

### Function expression


Here, we input the expression of the function of the indirect measurement. It is very important that we input the function following the python syntax, which is nothing especial but replacing ^ with ** (example x squared would be x**2).













