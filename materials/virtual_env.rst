.. raw:: pdf

   PageBreak oneColumn

Python Virtual Environment
==========================

- A Virtual Environment is a tool to keep the dependencies required by different projects in separate places.
- “Project X depends on module version 1.x but, Project Y needs 4.x” 
- It keeps  your global site-packages directory clean and manageable.

.. code-block:: tcsh

   # instal virtual env
   $ sudo apt-get install python3-venv
   $ pip install virtualenv

   # create new environment
   $ python3.5 -m venv training

   # use it
   $ source training/bin/activate
   (training) $ which python
   /home/ltyrala/work/training/bin/python
   (training) $ which pip
   /home/ltyrala/work/training/bin/pip

   # install some libraries
   (training) $ pip install numpy
   Collecting numpy
     Downloading numpy-1.11.2-cp35-cp35m-manylinux1_x86_64.whl (15.6MB)
       100% |████████████████████████████████| 15.6MB 97kB/s 
   Installing collected packages: numpy
   Successfully installed numpy-1.11.2

   # save your local environment state
   (training) $ pip freeze --local > requirements.txt
   (training) $ cat requirements.txt
   numpy==1.11.2
   pylint==1.6.4

   # restore environment from file
   (training) $ pip install -r requirements.txt
   Collecting numpy
     Downloading numpy-1.11.2-cp35-cp35m-manylinux1_x86_64.whl (15.6MB)
       100% |████████████████████████████████| 15.6MB 97kB/s 
   Installing collected packages: numpy
   Successfully installed numpy-1.11.2

   # exit
   (training) $ deactivate
   $ which python
   /usr/bin/python


