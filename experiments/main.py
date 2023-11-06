import time
import matplotlib.pyplot as plt


import algorithms.merge_algorithm as merge_sorts
import algorithms.tree_algorithm as tree_sort
import get_data.generate_data as generate


class ExperimentMerge:
    def __init__(self, array: list):
        self.array = array


    def experiment2(self):
        merge2_sorter = merge_sorts.KMergeSort(2)
        merge2_start = time.time()
        merge2_sorter.k_merge_sort(self.array)
        merge2_end = time.time()
        return merge2_end - merge2_start


    def experiment4(self):
        merge4_sorter = merge_sorts.KMergeSort(4)
        merge4_start = time.time()
        merge4_sorter.k_merge_sort(self.array)
        merge4_end = time.time()
        return merge4_end - merge4_start


    def experiment8(self):
        merge8_sorter = merge_sorts.KMergeSort(8)
        merge8_start = time.time()
        merge8_sorter.k_merge_sort(self.array)
        merge8_end = time.time()
        return merge8_end - merge8_start


class ExperimentTree:
    def __init__(self, array: list):
        self.array = array


    def experiment(self):
        sarray = [n for n in self.array]
        avl_start = time.time()
        tree_sort.tree_sort(sarray)
        avl_end = time.time()
        return avl_end - avl_start
    

if __name__ == "__main__":
    try:
        with open("output/time/merge2.txt", "r") as merge2_file:
            merge2_file.close()
            with open("output/time/merge2.txt", "w") as merge2_file:
                merge2_file.write("")
    except FileNotFoundError:
        with open("output/time/merge2.txt", "w") as merge2_file:
            merge2_file.write("")
    
    try:
        with open("output/time/merge4.txt", "r") as merge4_file:
            merge4_file.close()
            with open("output/time/merge4.txt", "w") as merge4_file:
                merge4_file.write("")
    except FileNotFoundError:
        with open("output/time/merge4.txt", "w") as merge4_file:
            merge4_file.write("")
    try:
        with open("output/time/merge8.txt", "r") as merge8_file:
            merge8_file.close()
            with open("output/time/merge8.txt", "w") as merge8_file:
                merge8_file.write("")
    except FileNotFoundError:
        with open("output/time/merge8.txt", "w") as merge8_file:
            merge8_file.write("")
    try:
        with open("output/time/tree.txt", "r") as tree_file:
            tree_file.close()
            with open("output/time/tree.txt", "w") as tree_file:
                tree_file.write("")
    except FileNotFoundError:
        with open("output/time/tree.txt", "w") as tree_file:
            tree_file.write("")
    
    merge2 = open("output/time/merge2.txt", "a")
    merge4 = open("output/time/merge4.txt", "a")
    merge8 = open("output/time/merge8.txt", "a")
    tree = open("output/time/tree.txt", "a")

    start_count = 0
    end_count = 100_000
    step = 1_000

    for i in range(start_count, end_count, step):
        array = generate.GenerateData(i).generate()
        e_merge = ExperimentMerge(array)
        e_tree = ExperimentTree(array)

        merge2.write(f"{e_merge.experiment2()}\n")
        merge4.write(f"{e_merge.experiment4()}\n")
        merge8.write(f"{e_merge.experiment8()}\n")
        tree.write(f"{e_tree.experiment()}\n")

        print(f"Experiment {i} finished")

    merge2.close()
    merge4.close()
    merge8.close()
    tree.close()

    # merge2
    with open("output/time/merge2.txt", "r") as merge2_file:
        merge2_data = merge2_file.readlines()
        merge2_data = [float(n) for n in merge2_data]
        plt.plot(merge2_data)
        plt.title("Merge sort 2")
        plt.xlabel(f"Start count: {start_count} End count: {end_count} Step: {step}")
        plt.ylabel("Time")
        plt.savefig("output/graphics/merge2.png")
        plt.clf()
        merge2_data.clear()
    
    # merge4
    with open("output/time/merge4.txt", "r") as merge4_file:
        merge4_data = merge4_file.readlines()
        merge4_data = [float(n) for n in merge4_data]
        plt.plot(merge4_data)
        plt.title("Merge sort 4")
        plt.xlabel(f"Start count: {start_count} End count: {end_count} Step: {step}")
        plt.ylabel("Time")
        plt.savefig("output/graphics/merge4.png")
        plt.clf()
        merge4_data.clear()

    # merge8
    with open("output/time/merge8.txt", "r") as merge8_file:
        merge8_data = merge8_file.readlines()
        merge8_data = [float(n) for n in merge8_data]
        plt.plot(merge8_data)
        plt.title("Merge sort 8")
        plt.xlabel(f"Start count: {start_count} End count: {end_count} Step: {step}")
        plt.ylabel("Time")
        plt.savefig("output/graphics/merge8.png")
        plt.clf()
        merge8_data.clear()

    # tree
    with open("output/time/tree.txt", "r") as tree_file:
        tree_data = tree_file.readlines()
        tree_data = [float(n) for n in tree_data]
        plt.plot(tree_data)
        plt.title("Tree sort")
        plt.xlabel(f"Start count: {start_count} End count: {end_count} Step: {step}")
        plt.ylabel("Time")
        plt.savefig("output/graphics/tree.png")
        plt.clf()
        tree_data.clear()
