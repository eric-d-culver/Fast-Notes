# Fast-Notes
## Requirements
This app requires Python 2, the Python package Tkinter, and the GUI creator Tk.  
### Windows
On Windows, the [Python Installer] will install Python, Tkinter, and Tk/Tcl. Using the py2exe Python extension, you can convert the Python script into a Windows executable that can be run on Windows computers without Python or Tk. (But you will need to do it on a Windows machine with Python and Tk.)

### Mac OS X
On Mac, the Installer will only install Python and Tkinter.  Tk must installed seperately. The easy way is to follow [This Link] and install the Python and Tk associated with your version of Mac OS X. Using the py2app Python extension, you can create a stand-alone Mac OS X app from the Python script. (But you will need to do it on a Mac with Python and Tk.)

### Linux
Under Debian based systems, run in shell:
- sudo apt-get install python python-tk tk

Under Red Hat based systems, run in shell:
- sudo yum install python tkinter tk

## Files
This contains the following files:
- notes.py

## Usage
**notes.py**
- python notes.py  
The main app.  When run, will have a single card in a single flow.  You can type whatever you like, then press Enter or Return to create a new card below that one.  Press the Right Arrow to create a new flow to the right of your current flow.

<!-- Links -->
[Python Installer]:https://www.python.org/downloads/windows/
[This Link]:https://www.python.org/download/mac/tcltk/
