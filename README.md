## Next Meeting:
**TBD** - Once New List of Questions Established

## Meeting #3: Saturday, 10/10/20
* Questions
     * Classes/Objects
         * The `__init__` method is known as the **constructor** which creates object (instances)
         * The `self` keyword is only used inside classes; it is a reference to the object itself
     * Files
         * Working with files is always a **three-step process**: open; read/write; close
         * The `with` syntax is often used because it has the added benefit of closing the file object automatically
         * When you open a file, you provide the file mode as an optional argument
             * `r` (read) is the default (file must exist)
             * `w` (write) will overwrite the file or create one if it does not exist
             * `a` (append) will add contents to the end of the file (file must exist)
             * `*b` any mode that ends in b, means that you are working with a binary file, e.g., pickled, multimedia content
* Tkinter 
     * Verify (from the command line, i.e., `cmd`)
     * Make sure Python is in the path: `echo %PATH%`
     * Verify version of Python: `python -V`
     * `python -m tkinter` should launch a simple Tkinter project listing the version number, etc.
     * <a href="https://github.com/babalugats76/TkinterTest/blob/main/main.py" target="_blank">Basic Tkinter Starter Project</a>
     * Resources
         * <a href="https://docs.python.org/3/library/tkinter.html" target="_blank">tkinter — Python interface to Tcl/Tk — Python 3.9.0 documentation</a>
         * <a href="https://effbot.org/tkinterbook" target="_blank">An Introduction to Tkinter</a>

## Meeting #2: Saturday, 8/29/20
* PyCharm Project Setup, e.g., 'Run' configurations
* `turtle` troubleshoot
* `generate` function and refactor of original code to include recursion, appropriate data types

### Homework
Let's continue on with procedural version of *Lucky Five* program:
* Add `setup.py` routine:
    * Performs **one-time serialization** of past ticket numbers into a file using `pickle` module
    * Can be run/tested using its own **run configuration**

* Add `pastTickets` function to `main.py`
    * Loads previously-serialized data from file using `pickle` module
    * Returns list to caller using `return` keyword
    * Name this function whatever you like :)
    
* Incorporate `pastTickets` into `generate`:
    * Update to refer to newly-created `pastTickets` function:
    
      ```
      # loop through past winning tickets
      for num in pastTickets():
      ```
### BONUS Extension
If you find great success with the above, then I would explore how this would be done
with a "flat file". So, imagine the data was stored in a file, let's say `tickets.csv` and it looked something like this:
```
14,15,16,39,42
6,10,13,17,31
5,6,23,33,45
11,15,37,40,46
...
```
Could you then, similarly, load the data, but this time working with Python's built-in file commands?

Working with files in Python is always the same **3-step process**:
* open
* read/write
* close
   
## Meeting #1: Saturday, 8/15/20
* Grounding and Expectations
 > *In Programming, the things you think would be easy are hard and vice versa*

* Lucky Five Project Plan & Discussion

* Tech Setup
    * <a href="https://github.com/" target="_blank">Github</a> account
    * <a href="https://github.com/users/babalugats76/projects/3" target="_blank">JJ Lucky Five Kanban</a>
    * <a href="https://www.jetbrains.com/pycharm/" target="_blank">PyCharm</a>
    * <a href="https://www.python.org/" target="_blank">Python</a> 3.X
    * Tweak File Explorer Options, etc.
    
### Homework
Our *Lucky Five* program will require that certain **data be stored on a semi-permanent basis**; namely, past winning ticket numbers.  Learning about data storage is one of our goals, so let's start there.

For a small program, like *Lucky Five*, Python's `pickle` module is a great way to get started with data storage. The `pickle` module allows you to easily **"serialize"** your data/objects to a file not only for posterity but also for **later use and recall**. To this day, file-based storage strategies like this are common and serve as a "gateway drug" of sorts to other more sophisticated strategies, e.g., relational databases, APIs, object databases, etc.

Another goal is to understand and be able to leverage **Object-Oriented Programming** techniques. This is important because **everything in Python is an object** and because OOP-techniques are requisite in using `Tkinter` and countless other language extensions and modules. Ultimately, we will be implementing *Lucky Five* using classes, e.g., `Ticket`, `LuckyFive`, `LuckyFiveGUI`, etc.

* **Explore the `pickle` module referring to *Python for Kids***, Chapter 10, Using the pickle Module to Save Information
  
  <img width="200" src="https://i.ibb.co/kxZCp1s/python-for-kids-pickle.png" alt="python-for-kids-pickle" border="0">
  
  See if you can pickle stuff and then get it "out of the jar" again
  
  Take a gander at the official documentation: <a href="https://docs.python.org/3/library/pickle.html" target="_blank">pickle — Python object serialization</a>
  
* **Read Up on Object-Oriented Programming**
  
  Take some time to review the following:
  
  * <a href="https://docs.google.com/presentation/d/1a79xrxAzWuJ4ePDszyp5BbC_syHcr9hsVf_mr-6plZU/edit?usp=sharing" target="_blank">Python - Object-Oriented Programming - Google Slides</a>
  
  * *Python for Kids*, **Chapter 8: How to Use Classes and Objects**
    
    <img width="200" src="https://i.ibb.co/QmXf1jL/python-for-kids-chapter-8-classes.png" alt="python-for-kids-chapter-8-classes" border="0">
   
  * *Python Crash Course*, **Chapter 9: Classes**
  
   <img width="200" src="https://i.ibb.co/Y3kh4Ck/python-crash-course-chapter-9-oop.png" alt="python-crash-course-chapter-9-oop" border="0">  
  
