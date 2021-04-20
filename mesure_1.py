'''
EL02 -- TP3 : acquisition de signaux numeriques sur reseau domestique 
@author: SHangyuan Han, Samy Devaud, Matthieu Guinouard
'''
import matplotlib.pyplot as plt

import libprepa

if __name__ == '__main__':
    filename = 'mesure_1.csv'
    output_name = 'figure_1.svg'

    # read file
    result = libprepa.extract_signal(filename)

    fig = plt.figure(figsize=(16, 9))

    # U
    ax_u = fig.add_subplot()
    line_u, = ax_u.plot(
        result[0].signal, result[1].signal, label='U', color='purple')
    ax_u.legend(bbox_to_anchor=(0, 1, 1, 1), loc='lower left')
    ax_u.grid(True)
    ax_u.set_xlabel('Temps (s)')
    ax_u.set_ylabel('Tension (V)')

    # I
    ax_i = ax_u.twinx()
    line_i_tot, = ax_i.plot(result[0].signal, result[2].signal, label='Itot')
    line_i_tot_p, = ax_i.plot(
        result[0].signal, result[3].signal, label='Itot\'')
    line_i_diff, = ax_i.plot(
        result[0].signal, result[2].signal - result[3].signal, label='Itot - Itot\'')
    ax_i.legend(bbox_to_anchor=(0, 1, 1, 1), loc='lower right', ncol=3)
    ax_i.grid(True)
    ax_i.set_xlabel('Temps (s)')
    ax_i.set_ylabel('Courant (A)')

    fig.tight_layout()
    fig.savefig(output_name)
