# EVERNOPE

## When you just get tired of paying for things

# FAQ:
# Why did you make this?

Like many others, I was tired of using Evernote. That's why I created this handy little tool to help you jump ship from evernote and move to Google Keep.

# How do you use this?

Simply call the function as follows from the command line:

`python3 moveToGoogleKeep.py email password path/to/evernote/export/file`

where your email and password correspond to your Google account, and the path/to/evernote/export/file is the path to the .enex file obtained by exporting all of your notes from evernote's desktop application.

# What does this actually do?

Great question! This application uses selenium to simulate a user manually entering in each note, one by one. It logs into your Google account, goes through each note that it finds in your exported notes document, and for each, it plugs it into google keep. Pretty simple! And don't worry, I can't use this to steal your Google account password ;)

# Current usability:

Currently, this only works for Mac out of the box. The code is super simple, though, and the main thing holding it back is the fact that different machines need different chromedrivers. To get around this, you can enter an optional fifth command, `path/to/chromedriver`, which will be a path to the correct chromedriver for your machine.
