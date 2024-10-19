import multiprocessing.pool
import threading
import multiprocessing
import os
import time


def count_words_in_file(path):
    """Counts all the words in a file.

    Args:
        path (string): file path

    Returns:
        int: word count
    """
    try:
        with open(path, 'r') as file:
            text = file.read()
            word_count = len(text.split())
            print(f"{path} contains {word_count} words.")
            return word_count
        pass
    except Exception as e:
        print(e)
        return 0


def process_files_with_threads(files):
    for file in files:
        count_words_in_file(file)


def monitor_progress():
    while True:
        print("Counting in progress... (daemon monitoring)")
        time.sleep(1e-2)


def process_files_with_processes(files):
    with multiprocessing.Pool() as pool:
        pool.map(count_words_in_file, files)


def main():
    folder_path = 'intermediate\\assets'
    files = [os.path.join(folder_path, file) for file in os.listdir(
        folder_path) if file.endswith('.txt')]

    if not files:
        print("No files found here.")
        return

    daemon_thread = threading.Thread(target=monitor_progress, daemon=True)
    daemon_thread.start()

    print("\nMultithreading to count words in file")
    thread1 = threading.Thread(target=count_words_in_file, args=(files[0],))
    thread2 = threading.Thread(target=count_words_in_file, args=(files[1],))
    thread3 = threading.Thread(target=count_words_in_file, args=(files[2],))
    thread4 = threading.Thread(target=count_words_in_file, args=(files[3],))
    thread5 = threading.Thread(target=count_words_in_file, args=(files[4],))

    tic = time.time()
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    print(f"\nMultithreading took {(time.time()-tic)} seconds")

    print("\nMultiprocessing to count words in file")
    tic = time.time()
    process_files_with_processes(files)
    print(f"\nMultiprocessing took {(time.time()-tic)} seconds")


if __name__ == '__main__':
    main()
