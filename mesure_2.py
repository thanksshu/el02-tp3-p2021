'''
EL02 -- TP3 : acquisition de signaux numeriques sur reseau domestique 
@author: SHangyuan Han, Samy Devaud, Matthieu Guinouard
'''
import matplotlib.pyplot as plt

import libprepa

if __name__ == '__main__':
    filename = 'mesure_2.csv'
    output_name = 'figure_2.svg'

    # read file
    result = libprepa.extract_signal(filename)

    fig = plt.figure(figsize=(16, 9))

    # I
    ax_i = fig.add_subplot(2, 1, 1)
    line_i_tot, = ax_i.plot(result[0].signal, result[2].signal, label='Itot')
    line_i_l, = ax_i.plot(result[0].signal, result[3].signal, label='Il')
    line_i_r, = ax_i.plot(result[0].signal, result[4].signal, label='Ir')
    line_i_diff, = ax_i.plot(
        result[0].signal, result[3].signal + result[4].signal - result[2].signal, label='Itot + Il - Ir')
    ax_i.legend(bbox_to_anchor=(0, 1, 1, 1), loc='lower left', ncol=2)
    ax_i.set_title('Temps - Courant')
    ax_i.grid(True)
    ax_i.set_xlabel('Temps (s)')
    ax_i.set_ylabel('Courant (A)')

    # P
    ax_p = fig.add_subplot(2, 1, 2)
    p_tot = result[1].signal * result[2].signal
    line_p_tot, = ax_p.plot(
        result[0].signal, p_tot, label='Ptot')
    p_l = result[1].signal * result[3].signal
    line_p_l, = ax_p.plot(
        result[0].signal, p_l, label='Pl')
    p_r = result[1].signal * result[4].signal
    line_p_r, = ax_p.plot(
        result[0].signal, p_r, label='Pr')
    ax_p.legend(bbox_to_anchor=(0, 1, 1, 1), loc='lower left', ncol=3)
    ax_p.set_title('Temps - Puissance')
    ax_p.grid(True)
    ax_p.set_xlabel('Temps (s)')
    ax_p.set_ylabel('Puissance (W)')

    fig.tight_layout()
    fig.savefig(output_name)

    print(f'valeur eff U {libprepa.get_eff(result[1].signal)}')
    print(f'valeur eff Itot {libprepa.get_eff(result[2].signal)}')
    print(f'valeur eff Il {libprepa.get_eff(result[3].signal)}')
    print(f'valeur eff Ir {libprepa.get_eff(result[4].signal)}')

    print(f'valeur moy Ptot {libprepa.get_mean(p_tot)}')
    print(f'valeur moy Pl {libprepa.get_mean(p_l)}')
    print(f'valeur moy Pr {libprepa.get_mean(p_r)}')
