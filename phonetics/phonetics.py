#
# Copyright: Micah Gajewski <micahbgaj@gmail.com>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
#
# Automatic Phonetics Generation.
#

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from anki.hooks import addHook
from aqt import mw
from aqt.utils import showInfo
from parser import getHighlightedPhonetics


srcFields = ['Reading']
dstFields = ['Phonetics']

buttonText = "Bulk-add Phonetics"


def regeneratePhonetics(nids):
    mw.checkpoint(buttonText)
    mw.progress.start()
    for nid in nids:
        note = mw.col.getNote(nid)

        src = None
        for fld in srcFields:
            if fld in note:
                src = fld

                break
        if not src:
            # no src field
            continue
        dst = None
        for fld in dstFields:
            if fld in note:
                dst = fld
                break
        if not dst:
            # no dst field
            continue
        if note[dst]:
            # already contains data, skip
            continue
        srcTxt = mw.col.media.strip(note[src])
        if not srcTxt.strip():
            continue
        try:
            note[dst] = getHighlightedPhonetics(srcTxt)
        except Exception, e:
            raise
        note.flush()
    mw.progress.finish()
    mw.reset()

# Menu
##########################################################################

def setupMenu(browser):

    a = QAction(buttonText, browser)
    browser.connect(a, SIGNAL("triggered()"), lambda e=browser: onRegenerate(e))
    browser.form.menuEdit.addSeparator()
    browser.form.menuEdit.addAction(a)

def onRegenerate(browser):
    regeneratePhonetics(browser.selectedNotes())

# Init
##########################################################################

addHook("browser.setupMenus", setupMenu)
