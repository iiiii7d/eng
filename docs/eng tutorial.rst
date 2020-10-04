eng Tutorial
============
This is the tutorial for eng v0.3.

Print to console
----------------
As always, when learning a new language, one always learns how to print something to console. In eng, ``say`` is used to print things to the console. For example:
::

   say "hello world"

You can also put other stuff inside too:
::

   say 1234567890
   say 3.141592653

Variables
---------
Declaring Variables
*******************
Variables are an important part of every programming language. In eng, to declare a variable, use ``let`` or ``set``. For example:
::

   let 'x' be 142
   set 'last letter' to "z"

``let`` and ``set`` are also aliases, ie. they mean the same thing in a different way.

It is **very** important to remember the single quote marks when declaring a variable. For example:
::

   let x be 142

returns:
::

   eng error 1.1 on Line 25: No variable name specified

This is because ``x`` is not recognised as a variable.

Variables can also be dynamically named:
::

   let 'var1' be "var2"
   let '<var1>' be "apple"
   say "Variable 1 is <var1> and Variable 2 is <<var1>>"

Outputting Variables
********************
To output variables, simply state the name of the variable in between angle brackets, like this:
::

   let 'apples' be 3
   say "I have <apples> apples"

Adding and subtracting to variables
***********************************
You can also add to and subtract from variables in eng. For addition, ``add`` is used, and for subtraction, ``subtract`` is used.

Here is an example of additon:
::

   let 'apples' be 3
   say "I have <apples> apples"
   add 3 to 'apples'
   say "I now have <apples> apples"

Here is an example of subtraction:
::

   let 'apples' be 3
   say "I have <apples> apples"
   subtract 3 from 'apples'
   say "I now have <apples> apples. Hey who stole my apples!?"

Loops
-----
eng also has loops. The ``repeat`` function is used in this case. For example:
::

   repeat 5 times:
   - say "I will be repeated 5 times"

Note the extra hyphen at the start of the ``say`` function. In English, this is like a list of things; ie. 'Repeat this list of things 5 times'. Therefore and similarly, in eng, the hyphen indicates an indent in the code.

The hyphen is also very important. If you leave out the indent,
::

   repeat 5 times:
   say "I will be repeated 5 times"

the ``say`` function will only be executed once. This is because there is nothing in the ``repeat`` function's list.

The ``repeat`` function can also be nested:
::

   repeat 2 times:
   - say "Who wants apples?"
   - repeat 3 times:
     - say "me"

Forever loops
*************
Sometimes, you want a program to run forever. In eng, ``repeat forever`` is used:
::

   repeat forever:
   - say "I will never stop"

Time
----
Waiting
*******
When you want a program to pause, you can add a ``wait`` function to wait for a certain amount of time to pass.
::

   wait for 1 second
   wait for 1000 milliseconds

Note that the 's' at the end of 'second' and 'millisecond' is optional.

Comments
--------
Like a good programmer, it is common practice to include comments in the code. The ``note`` function is used in this case. For example:
::

   note: this adds 1 to variable x 5 times
   let 'x' be 0
   repeat 5 times:
   - add 1 to 'x'
   - say <x>

Note that comments should take up its own line, and cannot be places at the end of another command:
::

   note: this is correct
   say "hi" note: this is wrong and will produce an error

Jumping & Markers
-----------------
In eng, you can also jump to different parts of code. For example:
::

   jump to after it says hello
   say "hello"
   * after it says hello

This will skip saying "hello", as it had jumped over it.

This technique is also useful in forever loops:
::

   * before echo
   say "echo"
   jump to before echo



Others
------
Manually throwing errors
************************
This is mainly for checking out how error looks like. The ``throw error`` command is used. For example:
::

   throw error 1.1

Conclusion
----------
This is everything basic you need to know in eng. In the future, more will be added, so stay tuned. Once again, thanks for learning eng :D *-- i____7d*