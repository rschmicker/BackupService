Backup Service

Python 2.7

Unix Configuration:
1.	Open backup_service.py
2.	Input your google drive and one drive path directories where designated
3.	Save and close
4.	Go to https://pypi.python.org/pypi/dirsync/2.2.1
5.	Download and install dirsync into your python site-packages folder
6.	Go to https://pypi.python.org/pypi/six
7.	Download and install six into your python site-packages folder

Manual Use:
cd to.py dir
python backup_service.py [Dir for service to watch]

OS X Automator to Run at Login:
1.	Create .sh file
2.	Input a cd to the directory containing the backup_service.py
3.	Input ‘python backup_service.py [Dir for service to watch]’
4.	Save file and close
5.	Open Automator
6.	Select Application
7.	Under Library choose Utilities
8.	Select ‘Run Shell Script’
9.	Choose ‘/bin/sh’ as your shell
10.	Copy and pasta the contents of the .sh script you created into window
11.	Save as WhateverYouLike.app 
12.	Open System Preferences
13.	Go to Users & Groups
14.	Click on your username and then Login Items
15.	Click the plus symbol
16.	Navigate to your newly created .app file
17.	Click add
18.	Done! (Will take into affect after restart)

