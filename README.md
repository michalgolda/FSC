# FSC
File Sum Checker - A program for checking the sum of files.
___


### Where to download?
The program can be downloaded from the project website: https://fsc.io


### Development

Want to contribute ? Great!

#### Building for source

Before building a program, you must install the required libraries.
```sh
$ pip install -r requirements.txt
```
The program is built using the pyinstaller.

An example of a build command:
```sh
$ pyinstaller FSC/app.py --clean --name FSC -F --windowed
```

#### Tests

Green is used to run tests.
```sh
$ green -vvv --run-coverage
```