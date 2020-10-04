Errors & Debugging
==================
This is a list of all eng errors as of v0.3.1, and how to troubleshoot them.

0.x: Compiler errors
--------------------
0.0: Invalid error code: *<invalidCode>*
****************************************
This error is thrown when a program, or a ``throw error`` function throws an error that does not exist.

Recreate
^^^^^^^^
::

   throw error 1234567890

Troubleshooting
^^^^^^^^^^^^^^^
* If the line where the error happened is a ``throw error`` function, you had put in an invalid error code yourself.
* If not, the compiler might have thrown the incorrect error. Open an issue on eng's Github repository, and state the line in the console that printed error 0.0.

0.1: *<fileName>* is not an .eng file
*************************************
This error is thrown when a file that you want to run is not an .eng file.

Recreate
^^^^^^^^
::

   (This is typed in console)
   python eng.py foo.bar

Troubleshooting
^^^^^^^^^^^^^^^
* Make sure the extension of the file you want to run is ".eng".

0.2: *<fileName>* does not exist
*************************************
This error is thrown when a file that you want to run does not exist.

Recreate
^^^^^^^^
::

   (This is typed in console)
   python eng.py foobar.eng

Troubleshooting
^^^^^^^^^^^^^^^
* Make sure your file exists.
* You could also have typed the name of the file wrongly.

0.3: Internal compiler code error: *<error>*
********************************************
This error is thrown when the compiler itself has an error.

Troubleshooting
^^^^^^^^^^^^^^^
* Open an issue on eng's Github repository, and paste in the error that error 0.3 gave you.

1.x: Variable & data errors
---------------------------
1.0: Command not recognised: "*<command>*"
******************************************
This error is thrown when the compiler encounters a command that is not recognised.

Recreate
^^^^^^^^
::

   foobar

Troubleshooting
^^^^^^^^^^^^^^^
* You might have misspelt the function name.
* eng is case-sensitive. For example, it will detect ``note:`` but not ``Note:``.

1.1: No variable name specified
*******************************
This error is thrown when the name of a variable is not specified in the function.

Recreate
^^^^^^^^
::

   let x be 3

Troubleshooting:
^^^^^^^^^^^^^^^^
* You might have missed the single quotes that your variable name should be in.

1.2: No value specified
***********************
This error is thrown when an argument in a function is not specified.

Recreate
^^^^^^^^
::

   let 'x' be

Troubleshooting:
^^^^^^^^^^^^^^^^
* Check if the value is stated in the function.
* You might also have typed the function wrongly.

1.3: Unknown data type
**********************
This error is thrown when the compiler encounters an unknown data type.

Recreate
^^^^^^^^
::

   let 'x' be abcd

Troubleshooting:
^^^^^^^^^^^^^^^^
* If your data is a string, check if you have put it in double quotes.
* If your data is a variable, check if you have put it in angle brackets.

1.4: Unknown variable "*<variable>*"
************************************
This error is thrown when the compiler encounters an unknown variable.

Recreate
^^^^^^^^
::

   say "<x>"

Troubleshooting
^^^^^^^^^^^^^^^
* Check if the variable was declared earlier.
* You might also have misspelt the variable name.

1.5: Incorrect value data type; expected *<expectation>* but instead got *<reality>*
******************************
This error is thrown when the argument provided has the incorrect value data type.

Recreate
^^^^^^^^
::

   repeat "foobar" times:

Troubleshooting
^^^^^^^^^^^^^^^
* Make sure that you have provided the correct data type.

1.6: Incorrect variable data type; expected *<expectation>* but instead got *<reality>*
*********************************
This error is thrown when the variable provided has the incorrect data type.

Recreate
^^^^^^^^
::

   let 'x' be "foobar"
   add 3 to 'x'

Troubleshoot
^^^^^^^^^^^^
* Make sure that you are dealing with the correct type of variable.

2.x: Indent & Loop errors
----------------
2.0: Number of iterations must be above 0
*****************************************
This error is thrown when the iterations argument in a ``repeat`` function is 0 or less.

Recreate
^^^^^^^^
::
   
   repeat -1 times:

Troubleshoot
^^^^^^^^^^^^
* Make sure that you are repeating at least 1 time.

2.1: Unexpected indent
**********************
This error is thrown when the compiler encounters an unexpected indent.

Recreate
^^^^^^^^
::
   say "abc"
   - say "def"
   say "ghi"

Troubleshoot:
^^^^^^^^^^^^^
* Make sure that the indent follows after a function that requires preceeding an indent, eg. ``repeat``.

3.x: Jumping & marker errors
----------------
3.0: Empty marker ID
********************
This error is thrown when the compiler encounters a marker with no ID.

Recreate
^^^^^^^^
::

   *

Troubleshoot
^^^^^^^^^^^^
* Make sure that there are no empty markers around.

3.1: Unknown marker ID "*<id>*"
********************************
This error is thrown when the compiler attempts to jump to a marker that does not exist.

Recreate
^^^^^^^^
::

   jump to foobar

Troubleshoot
^^^^^^^^^^^^
* Make sure the marker exists.
* You might have misspelt the marker name, or added extra whitespace.

4.x: Time-related errors
----------------
4.0: Wait time must be above or equal to 0
*******************************************
This error is thrown when the compiler attempts to wait for a negative amount of time.

Recreate
^^^^^^^^
::

   wait for -1 seconds

Troubleshoot
^^^^^^^^^^^^
* Always remember not to make the compiler wait for negative amounts of time... I guess?