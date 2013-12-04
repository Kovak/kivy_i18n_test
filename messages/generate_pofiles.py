import polib
# coding=utf-8
po = polib.POFile()
po.metadata = {
    'Project-Id-Version': '1.0',
    'Report-Msgid-Bugs-To': 'kovac1066@gmail.com',
    'POT-Creation-Date': '2013-12-3',
    'PO-Revision-Date': '2013-12-3',
    'Last-Translator': 'Jacob Kovac <kovac1066@gmail.com>',
    'MIME-Version': '1.0',
    'Content-Type': 'text/plain; charset=utf-8',
    'Content-Transfer-Encoding': '8bit',
}

entry = polib.POEntry(
    msgid=u'English',
    msgstr=u'Anglais',
)
po.append(entry)

entry = polib.POEntry(
    msgid=u'French',
    msgstr=u'Français',
)
po.append(entry)

po.save('fr/LC_MESSAGES/test.po')
po.save_as_mofile('fr/LC_MESSAGES/test.mo')