.. raw:: pdf

   PageBreak oneColumn

PyLint - Code analyse
=====================

Why
---

- To make long term code maintenance easier.

   + You will write code once
   + but other developers will read this all the time

- Better teamwork.
- To make our lives easier, not harder.

.. image:: images/team.png
   :align: right
   :scale: 200

.. raw:: pdf

   PageBreak oneColumn

How
---

Pylint - a source code, bug and quality checker for the Python programming language.
https://www.pylint.org/

Install pylint module,
then run it on a file or series of files to get a report of any violations.

.. code-block:: tcsh

   $ pip install pylint
   $ pylint lab/gui/tkinter/main.py 
   No config file found, using default configuration
   ************* Module main
   C:  9, 0: Trailing whitespace (trailing-whitespace)
   C: 19, 0: Trailing whitespace (trailing-whitespace)
   C: 23, 0: Trailing whitespace (trailing-whitespace)
   C: 32, 0: Trailing whitespace (trailing-whitespace)
   C: 92, 0: Final newline missing (missing-final-newline)
   C:  1, 0: Missing module docstring (missing-docstring)
   C:  4, 0: Missing class docstring (missing-docstring)
   C: 14, 4: Missing method docstring (missing-docstring)
   C: 17, 4: Missing method docstring (missing-docstring)
   R: 17, 4: Method could be a function (no-self-use)
   C: 20, 4: Missing method docstring (missing-docstring)
   C: 45, 4: Missing method docstring (missing-docstring)
   C: 49, 4: Missing method docstring (missing-docstring)
   C: 56, 4: Missing method docstring (missing-docstring)
   C: 62, 4: Missing method docstring (missing-docstring)
   C: 84, 4: Missing method docstring (missing-docstring)
   C: 87, 0: Missing function docstring (missing-docstring)
   
   
   Report
   ======
   62 statements analysed.
   
   Global evaluation
   -----------------
   Your code has been rated at 7.26/10


.. raw:: pdf

   PageBreak oneColumn


Automate the process
--------------------

Create .pylintrc file in your project root dir.

.. code-block:: tcsh

   $ pylint --generate-rcfile > .pylintrc
   $ cat .pylintrc | grep line-length
   max-line-length=120

   $pylint --rcfile=.pylint lab/gui/tkinter/main.py 
   No config file found, using default configuration
   ************* Module main
   C:  9, 0: Trailing whitespace (trailing-whitespace)
   C: 19, 0: Trailing whitespace (trailing-whitespace)
   C: 23, 0: Trailing whitespace (trailing-whitespace)
   C: 32, 0: Trailing whitespace (trailing-whitespace)
