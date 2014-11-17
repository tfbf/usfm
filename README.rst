
USFM Parser and Converters
==========================

This is a Python module to provide a USFM parser.  This project also
consists of few USFM to other format converters.

Installation
------------

To run the *usfm* program, you need Python 3.4 and few other third
party dependencies.  This is only tested in Debian GNU/Linux -
*Jessie* version and Fedora 20.  It may work in other GNU/Linux
distributions also.  These are the steps to install *usfm* program in
Debian GNU/Linux and Fedora 20.

1. Install `development libraries
   <https://docs.python.org/devguide/setup.html>`_ and other
   dependencies as root user

   a. Debian

      ::

        # apt-get -y build-dep python3
        # apt-get -y install wget git

   b. Fedora

      ::

        # yum install -y yum-utils wget git
        # yum-builddep python3

2. Install Python 3.4

   a. Download `Python 3.4 XZ compressed source tarball
      <https://www.python.org/ftp/python/3.4.2/Python-3.4.2.tar.xz>`_

      ::

      
        $ wget -c https://www.python.org/ftp/python/3.4.2/Python-3.4.2.tar.xz

   b. Extract Python source tarball, build and install

      ::

        $ tar Jxvf Python-3.4.2.tar.xz
        $ cd Python-3.4.2
        $ ./configure --prefix=$HOME/usr
        $ make
        $ make install

3. Create a `virtual environment
   <https://docs.python.org/3.4/library/venv.html>`_ and activate it

   ::

     $ $HOME/usr/bin/pyvenv $HOME/ve
     $ source $HOME/ve/bin/activate

4. Clone the `parsely <http://parsley.readthedocs.org>`_ code from the
   Git repository and install it

   ::

     $ cd $HOME
     $ git clone git@github.com:python-parsley/parsley.git
     $ cd parsley
     $ python setup.py install

5. Clone the *usfm* code from the Git repository and install it

   ::

     $ cd $HOME
     $ git clone git@github.com:tfbf/usfm.git
     $ cd usfm
     $ python setup.py develop

6. Now you can run the *usfm* program with various arguments
   The syntax looks like this::

     $ usfm -c <path/to/html.cfg> -p <file/path/or/pattern> -d <output/directory> --html

   Examples to convert USFM files to HTML::

     $ usfm -c ../svpm/conf/html.cfg> -p ../svpm/usfm1910/*.usfm -d svpm --html
