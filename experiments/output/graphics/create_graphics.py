import matplotlib.pyplot as plt


class Experiment1(object):

    def __init__(self, start: int, end: int, step: int, count: int):
        self.start = start
        self.end = end
        self.step = step
        self.count = count


    def rand_experiment(self):
        with open("F:/university/sorting_algorithms_app/experiments/output/time/kmerge/rand_exp1.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Random merge exp1")
            plt.xlabel(f"start: {self.start} end: {self.end} step: {self.step} count: {self.count}")
            plt.ylabel("Time")
            plt.savefig("F:/university/sorting_algorithms_app/experiments/output/graphics/kmerge/rand_exp1.png")
            plt.clf()
            data.clear()

        with open("F:/university/sorting_algorithms_app/experiments/output/time/avl_tree/rand_exp1.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Random tree exp1")
            plt.xlabel(f"start: {self.start} end: {self.end} step: {self.step} count: {self.count}")
            plt.ylabel("Time")
            plt.savefig("F:/university/sorting_algorithms_app/experiments/output/graphics/avl_tree/rand_exp1.png")
            plt.clf()
            data.clear()


    def inc_experiment(self):
        with open("F:/university/sorting_algorithms_app/experiments/output/time/kmerge/inc_exp1.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Increasing merge exp1")
            plt.xlabel(f"start: {self.start} end: {self.end} step: {self.step} count: {self.count}")
            plt.ylabel("Time")
            plt.savefig("F:/university/sorting_algorithms_app/experiments/output/graphics/kmerge/inc_exp1.png")
            plt.clf()
            data.clear()

        with open("F:/university/sorting_algorithms_app/experiments/output/time/avl_tree/inc_exp1.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Increasing tree exp1")
            plt.xlabel(f"start: {self.start} end: {self.end} step: {self.step} count: {self.count}")
            plt.ylabel("Time")
            plt.savefig("F:/university/sorting_algorithms_app/experiments/output/graphics/avl_tree/inc_exp1.png")
            plt.clf()
            data.clear()


    def dec_experiment(self):
        with open("F:/university/sorting_algorithms_app/experiments/output/time/kmerge/dec_exp1.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Decreasing merge exp1")
            plt.xlabel(f"start: {self.start} end: {self.end} step: {self.step} count: {self.count}")
            plt.ylabel("Time")
            plt.savefig("F:/university/sorting_algorithms_app/experiments/output/graphics/kmerge/dec_exp1.png")
            plt.clf()
            data.clear()
        
        with open("F:/university/sorting_algorithms_app/experiments/output/time/avl_tree/dec_exp1.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Decreasing tree exp1")
            plt.xlabel(f"start: {self.start} end: {self.end} step: {self.step} count: {self.count}")
            plt.ylabel("Time")
            plt.savefig("F:/university/sorting_algorithms_app/experiments/output/graphics/avl_tree/dec_exp1.png")
            plt.clf()
            data.clear()


    def all_experiments(self):
        self.rand_experiment()
        self.inc_experiment()
        self.dec_experiment()


class Experiment2(object):
    def __init__(self, start: int, end: int, step: int, count: int):
        self.start = start
        self.end = end
        self.step = step
        self.count = count


    def rand_experiment(self):
        with open("F:/university/sorting_algorithms_app/experiments/output/time/kmerge/rand_exp2.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Random merge exp2")
            plt.xlabel(f"start: {self.start} end: {self.end} step: {self.step} count: {self.count}")
            plt.ylabel("Time")
            plt.savefig("F:/university/sorting_algorithms_app/experiments/output/graphics/kmerge/rand_exp2.png")
            plt.clf()
            data.clear()

        with open("F:/university/sorting_algorithms_app/experiments/output/time/avl_tree/rand_exp2.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Random tree exp2")
            plt.xlabel(f"start: {self.start} end: {self.end} step: {self.step} count: {self.count}")
            plt.ylabel("Time")
            plt.savefig("F:/university/sorting_algorithms_app/experiments/output/graphics/avl_tree/rand_exp2.png")
            plt.clf()
            data.clear()


    def inc_experiment(self):
        with open("F:/university/sorting_algorithms_app/experiments/output/time/kmerge/inc_exp2.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Increasing merge exp2")
            plt.xlabel(f"start: {self.start} end: {self.end} step: {self.step} count: {self.count}")
            plt.ylabel("Time")
            plt.savefig("F:/university/sorting_algorithms_app/experiments/output/graphics/kmerge/inc_exp2.png")
            plt.clf()
            data.clear()

        with open("F:/university/sorting_algorithms_app/experiments/output/time/avl_tree/inc_exp2.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Increasing tree exp2")
            plt.xlabel(f"start: {self.start} end: {self.end} step: {self.step} count: {self.count}")
            plt.ylabel("Time")
            plt.savefig("F:/university/sorting_algorithms_app/experiments/output/graphics/avl_tree/inc_exp2.png")
            plt.clf()
            data.clear()


    def dec_experiment(self):
        with open("F:/university/sorting_algorithms_app/experiments/output/time/kmerge/dec_exp2.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Decreasing merge exp2")
            plt.xlabel(f"start: {self.start} end: {self.end} step: {self.step} count: {self.count}")
            plt.ylabel("Time")
            plt.savefig("F:/university/sorting_algorithms_app/experiments/output/graphics/kmerge/dec_exp2.png")
            plt.clf()
            data.clear()
        
        with open("F:/university/sorting_algorithms_app/experiments/output/time/avl_tree/dec_exp2.txt", "r") as wfile:
            data = wfile.readlines()
            data = [float(n) for n in data]
            plt.plot(data)
            plt.title("Decreasing tree exp2")
            plt.xlabel(f"start: {self.start} end: {self.end} step: {self.step} count: {self.count}")
            plt.ylabel("Time")
            plt.savefig("F:/university/sorting_algorithms_app/experiments/output/graphics/avl_tree/dec_exp2.png")
            plt.clf()
            data.clear()


    def all_experiments(self):
        self.rand_experiment()
        self.inc_experiment()
        self.dec_experiment()


if __name__ == "__main__":
    Experiment1(start=1, end=10**9, step=10**4, count=10**6).all_experiments()
    Experiment2(start=1, end=100, step=1, count=10**6).all_experiments()
