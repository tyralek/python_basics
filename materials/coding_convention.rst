.. raw:: pdf

   PageBreak oneColumn

Python Coding Conventions
=========================

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

PEP8 - code style guide for Python.
A high quality, easy-to-read version of PEP8 is also available at http://pep8.org.

.. code-block:: python

   # try to limit all lines to a maximum of 79 characters.
   # 4 slpace indents
   # every import item in new line, asterisk imports is not allowed
   from os import path
   from os import open

   class ClassName:
      """
      Write doc string in rest format
      """
      def long_function_name(var_one,
                             var_two):
         """
         Print sumarize of report

         :param var_one: description
         :param var_two: description
         :type var_one: SomeClass
         :type var_two: int
         :return: return description
         :rtype: the return type
         """
         print(var_one)

.. raw:: pdf

   PageBreak oneColumn

The table
---------

+-----------------+--------------------+---------------------------------+
| Type            | Public             | Internal                        |
+=================+====================+=================================+
| Packages        | lower_with_under   |                                 |
+-----------------+--------------------+---------------------------------+
| Modules         | lower_with_under   | _lower_with_under               |
+-----------------+--------------------+---------------------------------+
| Classes         | CapWords           | _CapWords                       |
+-----------------+--------------------+---------------------------------+
| Exceptions      | CapWords           |                                 |
+-----------------+--------------------+---------------------------------+
| Functions       | lower_with_under() | _lower_with_under()             |
+-----------------+--------------------+---------------------------------+
| Constants       | CAPS_WITH_UNDER    | _CAPS_WITH_UNDER                |
+-----------------+--------------------+---------------------------------+
| Variables       | lower_with_under   | _lower_with_under               |
+-----------------+--------------------+---------------------------------+
| Attributes      | lower_with_under   | _lower_with_under (protected)   |
|                 |                    | or                              |
|                 |                    | __lower_with_under (private)    |
+-----------------+--------------------+---------------------------------+
| Method          | lower_with_under() | _lower_with_under() (protected) |
|                 |                    | or                              |
|                 |                    | __lower_with_under() (private)  |
+-----------------+--------------------+---------------------------------+
| Parameters      | lower_with_under   |                                 |
+-----------------+--------------------+---------------------------------+
| Modules         | lower_with_under   | _lower_with_under               |
+-----------------+--------------------+---------------------------------+
| Local Variables | lower_with_under   |                                 |
+-----------------+--------------------+---------------------------------+


.. raw:: pdf

   PageBreak oneColumn

Automate the process
--------------------

Install pep8 module,
then run it on a file or series of files to get a report of any violations.

.. code-block:: tcsh

   $ pip install pep8
   $ pep8 optparse.py
   optparse.py:69:11: E401 multiple imports on one line
   optparse.py:77:1: E302 expected 2 blank lines, found 1
   optparse.py:88:5: E301 expected 1 blank line, found 0
   optparse.py:222:34: W602 deprecated form of raising exception
   optparse.py:347:31: E211 whitespace before '('
   optparse.py:357:17: E201 whitespace after '{'
   optparse.py:472:29: E221 multiple spaces before operator
   optparse.py:544:21: W601 .has_key() is deprecated, use 'in'

The program autopep8 can be used to automatically reformat code in the PEP 8 style.
Install and use it to format a file in-place with:

.. code-block:: tcsh

   $ pip install autopep8
   $ autopep8 --in-place optparse.py

