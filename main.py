# This is a sample Python script.
from FPgrowth import FPgrowth_transactions,FPgrowth_runtime
from AprioryAlgo import apriori_transactions,apriori_runtime,minsup,minconf
import matplotlib.pyplot as plt

if __name__ == '__main__':
    FT = FPgrowth_transactions
    FR = FPgrowth_runtime
    AT = apriori_transactions
    AR = apriori_runtime
    plt.plot(FT, FR, marker='*', label='Fpgrowth')
    plt.plot(AT, AR, marker='o', label='Apriory')
    plt.xlabel('Transactions')
    plt.ylabel('Runtime (seconds)')
    plt.title(f"Apriory vs FP growth transaction runtime graph input S={minsup} C={minconf}")
    plt.show()
