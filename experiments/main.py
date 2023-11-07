import time
import matplotlib.pyplot as plt
from multiprocessing import Process


import algorithms.merge_algorithm as merge_sorts
import algorithms.tree_algorithm as tree_sort
from get_data.generate_data import GenerateData


class ExperimentMerge:
    def __init__(self, start_count: int, end_count: int, step: int):
        self.array = []
        self.start_count = start_count
        self.end_count = end_count
        self.step = step


    def experiment2(self):
        wfile = open("output/time/merge2.txt", "w")
        wfile.write("")
        merge2_sorter = merge_sorts.KMergeSort(2)
        wfile = open("output/time/merge2.txt", "a")

        for i in range(self.start_count, self.end_count, self.step):
            self.array = GenerateData(i).generate()
            merge2_start = time.time()
            merge2_sorter.k_merge_sort(self.array)
            merge2_end = time.time()
            wfile.write(f"{merge2_end - merge2_start}\n")
            print(f"Merge 2: {i}")
        wfile.close()

        with open("output/time/merge2.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Merge sort 2")
            plt.xlabel(f"Start count: {self.start_count} End count: {self.end_count} Step: {self.step}")
            plt.ylabel("Time")
            plt.savefig("output/graphics/merge2.png")
            plt.clf()
            data.clear()


    def experiment4(self):
        wfile = open("output/time/merge4.txt", "w")
        wfile.write("")
        merge4_sorter = merge_sorts.KMergeSort(4)
        wfile = open("output/time/merge4.txt", "a")

        for i in range(self.start_count, self.end_count, self.step):
            self.array = GenerateData(i).generate()
            merge4_start = time.time()
            merge4_sorter.k_merge_sort(self.array)
            merge4_end = time.time()
            wfile.write(f"{merge4_end - merge4_start}\n")
            print(f"Merge 4: {i}")
        wfile.close()

        with open("output/time/merge4.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Merge sort 4")
            plt.xlabel(f"Start count: {self.start_count} End count: {self.end_count} Step: {self.step}")
            plt.ylabel("Time")
            plt.savefig("output/graphics/merge4.png")
            plt.clf()
            data.clear()


    def experiment8(self):
        wfile = open("output/time/merge8.txt", "w")
        wfile.write("")
        merge8_sorter = merge_sorts.KMergeSort(8)
        wfile = open("output/time/merge8.txt", "a")

        for i in range(self.start_count, self.end_count, self.step):
            self.array = GenerateData(i).generate()
            merge8_start = time.time()
            merge8_sorter.k_merge_sort(self.array)
            merge8_end = time.time()
            wfile.write(f"{merge8_end - merge8_start}\n")
            print(f"Merge 8: {i}")
        wfile.close()

        with open("output/time/merge8.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Merge sort 8")
            plt.xlabel(f"Start count: {self.start_count} End count: {self.end_count} Step: {self.step}")
            plt.ylabel("Time")
            plt.savefig("output/graphics/merge8.png")
            plt.clf()
            data.clear()


class ExperimentTree:
    def __init__(self, start_count: int, end_count: int, step: int):
        self.array = []
        self.start_count = start_count
        self.end_count = end_count
        self.step = step


    def experiment(self):
        wfile = open("output/time/tree.txt", "w")
        wfile.write("")
        wfile = open("output/time/tree.txt", "a")

        for i in range(self.start_count, self.end_count, self.step):
            self.array = GenerateData(i).generate()
            tree_start = time.time()
            tree_sort.tree_sort(self.array)
            tree_end = time.time()
            wfile.write(f"{tree_end - tree_start}\n")
            print(f"Tree: {i}")
        wfile.close()

        with open("output/time/tree.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Tree sort")
            plt.xlabel(f"Start count: {self.start_count} End count: {self.end_count} Step: {self.step}")
            plt.ylabel("Time")
            plt.savefig("output/graphics/tree.png")
            plt.clf()
            data.clear()
    

if __name__ == "__main__":
    start_count = 0
    end_count = 1_000_000
    step = 1_000

    e_merge = ExperimentMerge(start_count, end_count, step)
    e_tree = ExperimentTree(start_count, end_count, step)

    p1 = Process(target=e_merge.experiment2, daemon=True)
    p2 = Process(target=e_merge.experiment4, daemon=True)
    p3 = Process(target=e_merge.experiment8, daemon=True)
    p4 = Process(target=e_tree.experiment, daemon=True)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()