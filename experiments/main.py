import time
import matplotlib.pyplot as plt
from multiprocessing import Process


import algorithms.kmerge as merge
import algorithms.avl_tree as avl
from get_data.generate_data import GenerateData


class ExperimentMerge(object):

    def __init__(self, start: int, end: int, step: int, count: int, exp: int):
        self.start = start
        self.end = end
        self.step = step
        self.count = count
        self.exp = exp
        self.array = []


    def rand_experiment(self) -> None:
        f_rm = open(f"output/time/kmerge/rand_exp{self.exp}.txt", "w")
        merge4_sorter = merge.KMergeSort(4)

        for i in range(1, self.count // self.step + 1):
            self.arr1 = GenerateData(self.start, self.end, self.count).generate()[:self.step * i]
            print(f"Random merge exp{self.exp}: {i}")
            merge4_start = time.time()
            merge4_sorter.k_merge_sort(self.arr1)
            merge4_end = time.time()
            f_rm.write(f"{merge4_end - merge4_start}\n")
        f_rm.close()
        

    def incr_experiment(self) -> None:
        f_im = open(f"output/time/kmerge/inc_exp{self.exp}.txt", "w")
        merge4_sorter = merge.KMergeSort(4)

        for i in range(1, self.count // self.step + 1):
            self.arr2 = GenerateData(self.start, self.end, self.count).generate()[:self.step * i]
            print(f"Increasing merge exp{self.exp}: {i}")
            merge4_start = time.time()
            merge4_sorter.k_merge_sort(sorted(self.arr2))
            merge4_end = time.time()
            f_im.write(f"{merge4_end - merge4_start}\n")
        f_im.close()
            

    def decr_experiment(self) -> None:
        f_dm = open(f"output/time/kmerge/dec_exp{self.exp}.txt", "w")
        merge4_sorter = merge.KMergeSort(4)

        for i in range(1, self.count // self.step + 1):
            self.arr3 = GenerateData(self.start, self.end, self.count).generate()[:self.step * i]
            print(f"Decreasing merge exp{self.exp}: {i}")
            merge4_start = time.time()
            merge4_sorter.k_merge_sort(sorted(self.arr3)[::-1])
            merge4_end = time.time()
            f_dm.write(f"{merge4_end - merge4_start}\n")
        f_dm.close()


class ExperimentTree(object):

    def __init__(self, start: int, end: int, step: int, count: int, exp: int):
        self.start = start
        self.end = end
        self.step = step
        self.count = count
        self.exp = exp
        self.arr1, self.arr2, self.arr3 = [], [], []        


    def rand_experiment(self) -> None:
        f_rt = open(f"output/time/avl_tree/rand_exp{self.exp}.txt", "w")

        for i in range(1, self.count // self.step + 1):
            self.arr1 = GenerateData(self.start, self.end, self.count).generate()[:self.step * i]
            tree = avl.AVLTree()
            for elem in self.arr1:
                tree.insert(elem)
            print(f"Random tree exp{self.exp}: {i}")
            tree_start = time.time()
            tree.inorder_traverse()
            tree_end = time.time()
            f_rt.write(f"{tree_end - tree_start}\n")
        f_rt.close()

    
    def incr_experiment(self) -> None:
        f_it = open(f"output/time/avl_tree/inc_exp{self.exp}.txt", "w")

        for i in range(1, self.count // self.step + 1):
            self.arr2 = GenerateData(self.start, self.end, self.count).generate()[:self.step * i]
            tree = avl.AVLTree()
            for elem in sorted(self.arr2):
                tree.insert(elem)
            print(f"Increasing tree exp{self.exp}: {i}")
            tree_start = time.time()
            tree.inorder_traverse()
            tree_end = time.time() 
            f_it.write(f"{tree_end - tree_start}\n")
        f_it.close()

    
    def decr_experiment(self) -> None:
        f_dt = open(f"output/time/avl_tree/dec_exp{self.exp}.txt", "w")

        for i in range(1, self.count // self.step + 1):
            self.arr3 = GenerateData(self.start, self.end, self.count).generate()[:self.step * i]
            tree = avl.AVLTree()
            for elem in sorted(self.arr3)[::-1]:
                tree.insert(elem)
            print(f"Decreasing tree exp{self.exp}: {i}")
            tree_start = time.time()
            tree.inorder_traverse()
            tree_end = time.time()
            f_dt.write(f"{tree_end - tree_start}\n")
        f_dt.close()


class Experiment1(object):

    def __init__(self):
        self.start: int = 1
        self.end: int = 10**9
        self.step: int = 10**4
        self.count = 10**6
        self.exp: int = 1

    
    def kmerge_experiment(self) -> None:
        e1_kmerge = ExperimentMerge(self.start, self.end, self.step, self.count, self.exp)
        processes = [Process(target=e1_kmerge.rand_experiment, daemon=True), 
                     Process(target=e1_kmerge.incr_experiment, daemon=True),
                     Process(target=e1_kmerge.decr_experiment, daemon=True)]
        
        for process in processes:
            process.start()
        
        for process in processes:
            process.join()


    def  tree_experiment(self) -> None:
        e1_tree = ExperimentTree(self.start, self.end, self.step, self.count, self.exp)
        processes = [Process(target=e1_tree.rand_experiment, daemon=True), 
                     Process(target=e1_tree.incr_experiment, daemon=True),
                     Process(target=e1_tree.decr_experiment, daemon=True)]
        
        for process in processes:
            process.start()
        
        for process in processes:
            process.join()


class Experiment2(object):

    def __init__(self):
        self.start: int = 1
        self.end: int = 100
        self.step: int = 10000
        self.count = 10**6
        self.exp: int = 2

    
    def kmerge_experiment(self) -> None:
        e2_kmerge = ExperimentMerge(self.start, self.end, self.step, self.count, self.exp)
        processes = [Process(target=e2_kmerge.rand_experiment, daemon=True), 
                     Process(target=e2_kmerge.incr_experiment, daemon=True),
                     Process(target=e2_kmerge.decr_experiment, daemon=True)]
        
        for process in processes:
            process.start()
        
        for process in processes:
            process.join()

    
    def tree_experiment(self) -> None:
        e2_tree = ExperimentTree(self.start, self.end, self.step, self.count, self.exp)

        processes = [Process(target=e2_tree.rand_experiment, daemon=True), 
                     Process(target=e2_tree.incr_experiment, daemon=True),
                     Process(target=e2_tree.decr_experiment, daemon=True)]
        
        for process in processes:
            process.start()
        
        for process in processes:
            process.join()


if __name__ == "__main__":
    Experiment1().kmerge_experiment()
    Experiment2().kmerge_experiment()

    Experiment1().tree_experiment()
    Experiment2().tree_experiment()