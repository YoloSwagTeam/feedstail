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

# Import from feedstail
from utils import Storage


class Config(Storage):

    def __init__(self, *args, **kwargs):
        Storage(self, *args, **kwargs)
        # default values
        self.interval = 60 * 15 # 15 min
        self.oneshot = False
        self.format = u'Title: {title}'
        self.reverse = False
        self.key = 'id'
        self.reverse = False

config = Config()
