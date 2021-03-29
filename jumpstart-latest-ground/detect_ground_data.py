import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from split_ground_data import split_data

class Handler(FileSystemEventHandler):
    
    def on_created(self, event):
        print(
            "[{}] noticed: [{}] on: [{}] ".format(
                time.asctime(), event.event_type, event.src_path
            )
        )
        split_data(event.src_path)


if __name__ == "__main__":
    path = "./log"

    #w = Watcher(path)
    #w.run()
    observer = Observer()
    event_handler = Handler()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0.1)
    except:
        observer.stop()
        print("Error")

    observer.join()