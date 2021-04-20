'''
EL02 -- TP3 : acquisition de signaux numeriques sur reseau domestique 
@author: SHangyuan Han, Samy Devaud, Matthieu Guinouard
'''
import matplotlib.pyplot as plt

import libprepa

if __name__ == '__main__':
    filename = []
    filename.append('mesure_perceuse.csv')
    filename.append('mesure_perceuse_rapport_3.csv')
    filename.append('mesure_perceuse_rapport_6.csv')

    output_name = 'figure_5.svg'

    # read file
    result = []
    for f in filename:
        result.append(libprepa.extract_signal(f))

    # init figure
    fig = plt.figure(figsize=(16, 16))

    for index, re in enumerate(result):
        # P
        ax_p = fig.add_subplot(3, 1, index + 1)
        line_p_tot, = ax_p.plot(
            re[0].signal, re[1].signal * re[2].signal, label='P', color='red')
        ax_p.legend(bbox_to_anchor=(0, 1, 1, 1), loc='lower left')
        ax_p.grid(True)
        ax_p.set_xlabel('Temps (s)')
        ax_p.set_ylabel('Puissance (W)')

        ax_p.set_title(filename[index])

        # U
        ax_u = ax_p.twinx()
        line_u = ax_u.plot(
            re[0].signal, re[1].signal, label='U', color='purple')
        ax_u.legend(bbox_to_anchor=(-0.25, 1, 1, 1), loc='lower center')
        ax_u.grid(True)
        ax_u.set_xlabel('Temps (s)')
        ax_u.set_ylabel('Tension (V)')

        # I
        ax_i = ax_p.twinx()
        ax_i.spines['right'].set_position(('axes', 1.1))
        line_u = ax_i.plot(
            re[0].signal, re[2].signal, label='I', color='blue')
        ax_i.legend(bbox_to_anchor=(0, 1, 1, 1), loc='lower right')
        ax_i.grid(True)
        ax_i.set_xlabel('Temps (s)')
        ax_i.set_ylabel('Courant (A)')

    fig.tight_layout()
    fig.savefig(output_name)
