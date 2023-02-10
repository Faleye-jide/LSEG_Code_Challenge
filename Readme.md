To implement this program, you need to first parse the input file and extract the instructions and coordinates.

Next, you can create a two-dimensional grid representing the lights, with each cell representing a light and its state (on/off).

Then, for each instruction, you can modify the state of the lights in the specified coordinate range accordingly. 
For example, for "turn on" instruction,
you can set all the lights in the coordinate range to on, for "turn off" instruction, you can set all the lights in the coordinate range to off, and for "toggle" instruction, you can switch the state of the lights in the coordinate range from on to off or vice versa.

Finally, you can count the number of lights that are switched on in the grid and print the result.


### Below are the steps required to this working on a windows system.
 - clone the project from github repo
 - install all required dependencies 
 - Run entry point

## 1. Clone the project on the github
    $ git clone https://github.com/Faleye-jide/LSEG_Code_Challenge.git
    $ cd LSEG_Code_Challenge
## 2. Install required dependencies
    pip install unittest 
## 3. Run the entry point
   python main.py
## 4. Run the test file for the test cases
   python -m unittest --v
