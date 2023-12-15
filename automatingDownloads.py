import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

downloadDirectoryPath = "C:\\Users\\domik\\Downloads\\"
downloadedDocumentsDirectoryPath = "C:\\Users\\domik\\Desktop\\DownloadedDocuments\\"
downloadedImagesDirectoryPath = "C:\\Users\\domik\\Desktop\\DownloadedImages\\"
documentFileTypes = [".txt", ".docx", ".doc", ".pptx", ".ppt", ".pdf", ".csv"]
imageFileTypes = [".jpg", ".jpeg", ".png", ".svg", ".gif"]
audioVideoFileTypes = [".mp3", ".wav", ".mp4"]

# AUTOMATION

class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.processed_files = set()

    def on_created(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'created':
            # print(f"Neue Datei erstellt: {event.src_path}")
            self.process_file(event.src_path)

    def process_file(self, file_path):
        if file_path in self.processed_files:
            return  # Die Datei wurde bereits verarbeitet

        filename, fileExtension = os.path.splitext(file_path)
        if fileExtension in documentFileTypes:
            # Warte 10 Sekunden, um sicherzustellen, dass die Datei vollständig heruntergeladen wurde
            time.sleep(5)
            shutil.move(file_path, downloadedDocumentsDirectoryPath)
            self.processed_files.add(file_path)
        elif fileExtension in imageFileTypes:
            # Warte 10 Sekunden, um sicherzustellen, dass die Datei vollständig heruntergeladen wurde
            time.sleep(5)
            shutil.move(file_path, downloadedImagesDirectoryPath)
            self.processed_files.add(file_path)


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, downloadDirectoryPath, recursive=True)
    observer.start()

    try:
        while True:
             time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


# MANUAL

# files = os.listdir(downloadDirectoryPath)

# x = 0

# for file in files:
#     filename, fileExtension = os.path.splitext(file)

#     if file == "desktop.ini":
#         continue
    
#     if fileExtension in documentFileTypes:
#         shutil.move(downloadDirectoryPath + file, downloadedDocumentsDirectoryPath)

#     if fileExtension in imageFileTypes:
#         shutil.move(downloadDirectoryPath + file, downloadedImagesDirectoryPath)
    
#     x = x + 1

# print("Moved " + str(x) + " files")




         

        


