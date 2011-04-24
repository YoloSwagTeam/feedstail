# -*- coding: utf-8 -*-
# Copyright (C) 2011 Romain Gauthier <romain.gauthier@masteri2l.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Import from the standard library
import sys

from time import sleep

# Import from FeedParser
from config import config
from feedparser import parse

tail = []

def isnew(entry):
    for item in tail:
        if entry[config.key] == item[config.key]:
            return False
    return True


def show(entry):
    sys.stdout.write(config.format.format(**entry))
    sys.stdout.write("\n")
    sys.stdout.flush()


def loop():
    def cycle():
        global tail
        entries = parse(config.url).entries
        if config.reverse:
            entries.reverse()
        for entry in entries:
            if isnew(entry):
                tail = [entry] + tail[:100]
                show(entry)

    cycle()
    while not config.oneshot:
        sleep(config.interval)
        cycle()

