==================
Osl154TestClientUa
==================

Summary
=======

Opc Ua command line test client for Osl154 specification

Requirements
============

Software:

-   Python 3.7 or newer: https://www.python.org/downloads/windows


Installation
============

Windows
-------

#.  Install Python

#.  Open command line and create an empty folder:

    .. code-block:: doscon

        > mkdir %USERPROFILE%\Projects\Osl154Ua
        > cd /d %USERPROFILE%\Projects\Osl154Ua

#.  Create an virtual environment for python and install required packages using pip:

    .. code-block:: doscon

        > py -3 -m venv venv
        > venv\Scripts\activate
        > pip install https://github.com/fholmer/Osl154TestClientUa/archive/main.zip

Linux
-----

#.  Open command line and create an empty folder:

    .. code-block:: console

        $ mkdir -p ~/projects/Osl154Ua
        $ cd ~/projects/Osl154Ua

#.  Create an virtual environment for python and install required packages using pip:

    .. code-block:: console

        > python3 -m venv venv
        > source venv/bin/activate
        > pip install https://github.com/fholmer/Osl154TestClientUa/archive/main.zip

Usage
=====

Create some initial bmp-data for your sign. You can use the discover function:

.. code-block:: doscon

    > osl154ua discover-sign opc.tcp://127.0.0.1:4840/server/

Or add it manually:

.. code-block:: doscon

    > osl154ua add-sign default -server opc.tcp://127.0.0.1:4840/server/ -tag "ns=2;s=SSA1.SIGN1" -width 304 -height 104

.. note:: Make sure server, opctag, width and height match your server and sign

This command will create a directory ``signs/default``:

.. code-block:: text

    /signs
        /default
            /sign.json
            /1.bmp
            /2.bmp
            /3.bmp
            /4.bmp

BMP-file can be duplicated and edited to make different test images.
sign.json can also be edited to adjust opc-tag names.

.. warning::

    if you run the ``add-sign`` or ``discover-sign`` command again all
    changes will be overwritten.

Read the values currently on the sign:

.. code-block:: doscon

    > osl154ua read

Send a rgb-on command to the sign:

.. code-block:: doscon

    > osl154ua rgb-on -image 1.bmp

Image ``1.bmp`` will now be loaded in ``IMAGE_TOSET``. ``VALUE`` is set to 9999
and after a short delay the ``COMMAND`` is set to ``RGB-ON``.
