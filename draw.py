import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
def main():
    f = open(sys.argv[1])
    it = []
    val = []
    test = []
    for line in f:
        if line.startswith("N"):
            continue
        token = line.split(",")
        it.append(int(float(token[0])))
        test.append(float(token[3]))

    #plt.plot(it, val, 'r', label="training accuracy")
    plt.plot(it, test, 'r',label="test accuracy")
    plt.xlabel('# of iterations')
    plt.ylabel('Accuracy')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), \
          fancybox=True, shadow=True, ncol=5)
    plt.show()

if __name__ == "__main__":
    main()