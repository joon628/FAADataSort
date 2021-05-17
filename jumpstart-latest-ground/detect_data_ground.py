import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from split_data_ground import split_data


class Watcher:
    def __init__(self, path):
        self.observer = Observer()
        self.path = path

    def run(self):
        self.event_handler = Handler()
        self.observer.schedule(self.event_handler, self.path, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(0.1)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    def on_created(self, event):
        print(
            "[{}] noticed: [{}] on: [{}] ".format(
                time.asctime(), event.event_type, event.src_path
            )
        )
        split_data(event.src_path)


if __name__ == "__main__":
    src_path = "./log"

    w = Watcher(src_path)
    w.run()
