import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping... {seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1]
    results = executor.map(do_something, seconds)

    for result in results:
        print(result)

# processes = []
# for _ in range(10):
#     p = multiprocessing.Process(target=do_something, args=[1.5])
#     p.start()

#     processes.append(p)

# for p in processes:
#     p.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')