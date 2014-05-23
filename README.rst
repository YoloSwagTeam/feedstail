Feedstail
=========

Feedstail is a tail-f-like utility for feeds. It monitor a feed and emits new entries.
Feedstail aim to be simple, hackable and compatible with rsstail_ its C brother.

.. _rsstail : http://www.vanheusden.com/rsstail/


License
-------

Feedstail is released under the terms of the `GNU General Public License v3`_ or later.

.. _GNU General Public License v3 : http://www.gnu.org/licenses/gpl-3.0.html


Get started
-----------

Use pip to install feedstail the easy way:

::

  $ pip install feedstail

Or retrieve the project with git and install it:

::

  $ git clone https://github.com/Psycojoker/feedstail.git
  $ cd feedstail
  $ python setup.py install

Then, launch feedstail with a random feeds to test it:

::

  $ feedstail -u http://hackeragenda.be/events/events.rss

Examples
--------

By default, feedstail will checkout the feeds every 15 minutes. If you
want to customize this interval you can use the ``i`` option.
The following example will retrieve feeds every 5 seconds:

::

  $ feedstail -u http://hackeragenda.be/events/events.rss -i 5


The default output format may not be ok for you. You can specify your
own format using the ``f`` option. The given fields must be an
available property of the feed entries.
The following example will output the published date, the title and the link:

::

  $ feedstail -u http://hackeragenda.be/events/events.rss -f "{published}: {title} - {link}"

This last example use the string formatting syntax appeared in the 2.6
version of Python.
However, feedstail aim to be 2.5 compatible so you can use the old
string formatting syntax:

::

  $ feedstail -u http://hackeragenda.be/events/events.rss -f "%(published)s: %(title)s - %(link)s"


Feedstail compares the ``id`` element to find new entries. You can
choose another element of comparison with the ``k`` option.
The following example says to feedstail to use the title to find new
entries:

::

  $ feedstail -u http://hackeragenda.be/events/events.rss -i 2 -k title



As feedstail is built above `feedparser`_, the available values of
format fields and keys can be found in `the documentation of the library`_.

.. _`feedparser` : https://pythonhosted.org/feedparser/
.. _`the documentation of the library` : https://pythonhosted.org/feedparser/


Importing to other python project
---------------------------------

Feedstail could be imported to another python project with:
::

   from feedstail import feedGenerator
   from feedstail.config import Config

Options :
   * key : The comparaison key. By default: ``id``
   * reverse : Boolean value for reversing the entries of the feed. By default: False
   * number : At the first time, show x entries. By default, it is None and shows all the received entries.
   * ignore_key_error : Boolean value for ignore keys errors. By default: False
   * no_endl : Boolean value for ignoring end lines. By default: False
   * url : The url. By default: None
   * format : The format of entries.

Options not present :
   * interval : The interval time for checking the feed.
   * one shot : Get once the feed.

The feedGenerator take an instance of Config as parameters and return a generator. This generator will return
an array of entries (could be an empty array) with the defined format.

Example:
::

   from feedstail import feedGenerator
   from feedstail.config import Config

   feed = feedGenerator(Config(url="http://hackeragenda.be/events/events.rss", format=u'{title} - {link}'))
   print '\n'.join(feed.next())

Contribute !
------------

  - Fork the project: `https://github.com/Psycojoker/feedstail.git`_
  - Create your patch in a topic branch
  - Send pull requests or send your patches via e-mail

Don't forget to mark your commits by one of the following flag:

  - [enh]: Your commit add a notable enhancement, a new feature for instance
  - [fix]: Your commit is a bugfix
  - [doc]: Your commit improve the documentation
  - [mod]: Your commit bring general changes, matching neither of the above, like refactoring

.. _`https://github.com/Psycojoker/feedstail.git` : https://github.com/Psycojoker/feedstail.git

