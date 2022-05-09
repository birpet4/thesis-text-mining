import spacy
import spacy
import pandas as pd
import numpy as np
from spacy.util import minibatch, compounding
import json
import random
from pandas import DataFrame
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.utils import shuffle




def save(df, n):
    x = []
    for i in range(100,200):
        x.append(i)

    p_1 = df['prec'].tolist()
    avg_p_1 = sum(p_1) / len(p_1)
    print(len(p_1)) 
    plt.title('Precision range')
    plt.plot(x, p_1, 'b', label='Avg Precision = %0.2f' % avg_p_1)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [100, 200], 'r--')
    plt.xlim([100, 200])
    plt.ylim([0, 1])
    plt.ylabel('Precision')
    plt.xlabel('Sample')
    plt.savefig("test/initcross_prec_sum_" + str(n) +".png")
    plt.clf()

    rec_1 = df['rec'].tolist()
    avg_rec_1 = sum(rec_1) / len(rec_1)
    plt.title('Recall range')
    plt.plot(x, rec_1, 'b', label='Avg Recall = %0.2f' % avg_rec_1)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [100, 200], 'r--')
    plt.xlim([100, 200])
    plt.ylim([0, 1])
    plt.ylabel('Recall')
    plt.xlabel('Sample')
    plt.savefig("test/initcross_rec_sum_" + str(n) +".png")
    plt.clf()

    acc_1 = df['acc'].tolist()
    avg_acc_1 = sum(acc_1) / len(acc_1)
    plt.title('Accuracy range')
    plt.plot(x, acc_1, 'b', label='Avg Accuracy = %0.2f' % avg_acc_1)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [100, 200], 'r--')
    plt.xlim([100, 200])
    plt.ylim([0, 1])
    plt.ylabel('Accuracy')
    plt.xlabel('Sample')
    plt.savefig("test/initcross_acc_sum_" + str(n) +".png")
    plt.clf()

    f1_1 = df['f1'].tolist()
    avg_f1_1 = sum(f1_1) / len(f1_1)
    plt.title('F1 range')
    plt.plot(x, f1_1, 'b', label='Avg F1 = %0.2f' % avg_f1_1)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [100, 200], 'r--')
    plt.xlim([100, 200])
    plt.ylim([0, 1])
    plt.ylabel('F1')
    plt.xlabel('Sample')
    plt.savefig("test/initcross_F1_sum_" + str(n) +".png")
    plt.clf()

    auc = df['auc'].tolist()
    avg_f1_1 = sum(f1_1) / len(f1_1)
    plt.title('AUC range')
    plt.plot(x, auc, 'b', label='Avg AUC = %0.2f' % avg_f1_1)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [100, 200], 'r--')
    plt.xlim([100, 200])
    plt.ylim([0, 1])
    plt.ylabel('AUC')
    plt.xlabel('Sample')
    plt.savefig("test/initcross_AUC_sum_" + str(n) +".png")
    plt.clf()

def average():
    plot_data = pd.read_csv("test/test_plot_eur_init.csv", sep=",", encoding='utf-8')
    auc = []
    dfRange1 = plot_data.iloc[0:100]['auc'].tolist()
    dfRange2 = plot_data.iloc[100:200]['auc'].tolist()
    dfRange3 = plot_data.iloc[200:300]['auc'].tolist()
    dfRange4 = plot_data.iloc[300:400]['auc'].tolist()
    dfRange5 = plot_data.iloc[400:500]['auc'].tolist()

    x = []
    for i in range(100,200):
        x.append(i)

    for i in range(0,100):
        auc.append((dfRange1[i] + dfRange2[i] + dfRange3[i] + dfRange4[i] + dfRange5[i]) / 5)

    avg_f1_1 = sum(auc) / len(auc)
    plt.title('AUC average')
    plt.plot(x, auc, 'b', label='Avg AUC = %0.2f' % avg_f1_1)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [100, 200], 'r--')
    plt.xlim([100, 200])
    plt.ylim([0, 1])
    plt.ylabel('AUC')
    plt.xlabel('Sample')
    plt.savefig("test/initcross_AUCavg_eur_sum.png")
    plt.clf()

def plotos():
    plot_data = pd.read_csv("test/test_plot_eur_init.csv", sep=",", encoding='utf-8')

    dfRange1 = plot_data.iloc[0:100]
    save(dfRange1, 1)
    dfRange2 = plot_data.iloc[100:200]
    save(dfRange2, 2)
    dfRange3 = plot_data.iloc[200:300]
    save(dfRange3, 3)
    dfRange4 = plot_data.iloc[300:400]
    save(dfRange4, 4)
    dfRange5 = plot_data.iloc[400:500]
    save(dfRange5, 5)

if __name__ == "__main__":
    plotos()
    average()

    