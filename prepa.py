'''
EL02 -- TP3 : acquisition de signaux numeriques sur reseau domestique 
@author: SHangyuan Han, Samy Devaud, Matthieu Guinouard
'''

import argparse
from itertools import combinations

import matplotlib.pyplot as plt

import libprepa

if __name__ == '__main__':
    filename = 'mesure_prepa.csv'
    output_name = 'figure_prepa.svg'

    result = libprepa.extract_signal(filename)

    # Trace des courbes
    fig = plt.figure(figsize=(16, 9))
    fig.suptitle('figure preparation')

    ax_1 = fig.add_subplot()
    ax_1.plot(result[0].signal, result[1].signal,
              label=result[1].name, color='purple')
    ax_1.plot(result[0].signal, result[2].signal*result[3].signal,
              label=f'{result[3].name} * {result[2].name}')
    ax_1.grid(True)
    ax_1.legend(bbox_to_anchor=(0, 1, 1, 1), loc='lower left', ncol=2)
    ax_1.set_ylabel('Tension (V)')

    ax_1.set_xlabel('Temps(s)')

    ax_2 = ax_1.twinx()
    ax_2._get_lines.prop_cycler = ax_1._get_lines.prop_cycler
    ax_2.plot(result[0].signal, result[2].signal, label=result[2].name)
    ax_2.plot(result[0].signal, result[3].signal, label=result[3].name)
    ax_2.plot(result[0].signal, result[2].signal + result[3].signal,
              label=f'{result[3].name} + {result[2].name}')
    ax_2.plot(result[0].signal, result[2].signal-result[3].signal,
              label=f'{result[3].name} - {result[2].name}')
    ax_2.grid(True)
    ax_2.legend(bbox_to_anchor=(0, 1, 1, 1), loc='lower right', ncol=4)
    ax_2.set_ylabel('Courant (A)')

    fig.savefig(output_name)
