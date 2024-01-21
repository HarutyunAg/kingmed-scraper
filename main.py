from downloader.downloader import Downloader

if __name__ == "__main__":
    path = input("Enter the path where you want to download files: \n")
    Downloader(path=path).download_files()
