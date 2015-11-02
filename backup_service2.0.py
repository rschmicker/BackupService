import sys
import time
import os
from dirsync import sync
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

#place the directory of your google drive and one drive here
google_drive=""
one_drive=""

class MyHandler(PatternMatchingEventHandler):
    def process(self, event):
        sync(args[0], google_drive, 'sync', purge=True, create=True)
        sync(args[0], one_drive, 'sync', purge=True, create=True)
        
    def on_any_event(self, event):
        self.process(event)

if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.', recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
