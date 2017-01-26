Quickstart
==========

Requirements
------------

* Python 3

Installation
------------

Install from pypi
.................
This will install the latest release of hippy-chat from pypi via pip::

$ pip install hippy-chat

Install latest version from github
..................................
If you would like a version other than the latest published on pypi, you may
do so by cloning the git repostiory::

$ git clone https://github.com/dusktreader/hippy-chat.git

Next, checkout the branch or tag that you wish to use::

$ cd sphinx-view
$ git checkout integration

Finally, use pip to install from the local directory::

$ pip install .

.. note::

   sphinx-view does not support distutils or setuptools. pip is a really
   complete package manager and has become the de-facto standard for installing
   python packages from remote locations. Compatability with pip is of primary
   importance, and since pip is such a great tool, it makes the most sense to
   the original author to use pip for local installs as well.

View a single document
----------------------
Just execute ``sphinx-view`` targeting the file you wish to view in a browser::

$ sphinx-view README.rst

A new page will open in your browser showing the html rendered document.

sphinx-view will automatically refresh the browser if you make any changes to
the document, so you can view the file as you edit it.

View a directory
----------------
This feature is most useful for looking at the rendered version of docs for a
python package. Simply target the directory with ``spinx-view`` and everything
should just work::

$ sphinx-view docs

For a directory, ``sphinx-view`` will watch for changes to any of the files
and update the browser with new changes
