# Barcode Scanner

## Introduction

The barcode scanner is a simple command-line python program to fetch barcodes. The program is developed using python3 and the packages used by the program are:-

1. Pyzbar
2. imutils
3. opencv2

## Applications

This program is written by keeping on main point in focus, automation. Anyone can use program inside their large application without any major changes. This is because the proram is written in such a way that, whenever a barcode is detected by the program, it will exit itself after printing the barcode.

## Prerequisites

1. Install zbar.\
   for mac:-\
   `$ brew install zbar`\
   for ubuntu / debian / raspbian:-\
   `$ sudo apt-get install libzbar0`

2. Install pyzbar.\
   `$ pip install pyzbar`

3. Install imutils.\
   `$ pip install imutils`

4. Install numpy.\
   `$ pip install numpy`

5. Install opencv2.\
   `$ pip install opencv-python`

## Notes

1. By default, the program uses webcam (USB camera). If you want to use the Pi camera, change the code from `usePiCamera=False` to `usePiCamera=True`.
