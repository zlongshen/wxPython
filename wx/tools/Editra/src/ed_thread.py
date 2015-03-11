###############################################################################
# Name: ed_thread.py                                                          #
# Purpose: Provides Thread Pool interface and access                          #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2011 Cody Precord <staff@editra.org>                         #
# License: wxWindows License                                                  #
###############################################################################

"""
Implements and provides the interface for dispatching asynchronous jobs through
the Editra Threadpool.

"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id$"
__revision__ = "$Revision$"

#-----------------------------------------------------------------------------#
# Imports
import wx

# Local Imports
import ebmlib

#-----------------------------------------------------------------------------#

class EdThreadPool(ebmlib.ThreadPool):
    """Singleton ThreadPool"""
    __metaclass__ = ebmlib.Singleton
    def __init__(self):
        super(EdThreadPool, self).__init__(5) # 5 Threads

#-----------------------------------------------------------------------------#
        