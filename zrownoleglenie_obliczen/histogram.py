import random
import multiprocessing


def calculate_histogram_w(part_data, data_range):
    part_hist = [0] * (data_range + 1)
    for a in part_data:
        part_hist[a] += 1
    return part_hist


def calculate_histogram(data, data_range):
    cores = 4
    pool = multiprocessing.Pool(cores)
    workers = []
    part_len = int(len(data)/cores)
    for core in range(cores):
        part_data = data[part_len * core: (part_len * (core + 1))]
        workers.append(pool.apply_async(calculate_histogram_w, (part_data, data_range, )))

    hists = []
    for worker in workers:
        while 1:
            try:
                hists.append(worker.get(1))
                break
            except multiprocessing.context.TimeoutError:
                pass
            except KeyboardInterrupt:
                print("Program zakończony")
                pool.terminate()
                pool.close()
                pool.join()
                raise KeyboardInterrupt
    pool.close()
    pool.join()

    histogram_f = [0] * (data_range + 1)
    for histogram in hists:
        for t in range(len(histogram)):
            histogram_f[t] += hists[t]
    return histogram_f


if __name__ == '__main__':
    random.seed()
    data_range = 10
    data = []

    for i in range(0, 100):
        data.append(int(random.random() * data_range))

    histogram = calculate_histogram(data, data_range)
    print(histogram)
