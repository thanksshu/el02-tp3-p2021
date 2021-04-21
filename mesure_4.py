'''
EL02 -- TP3 : acquisition de signaux numeriques sur reseau domestique 
@author: SHangyuan Han, Samy Devaud, Matthieu Guinouard
'''
import matplotlib.pyplot as plt

import libprepa

if __name__ == '__main__':
    filename = 'mesure_4.csv'
    output_name = 'figure_4.svg'

    # read file
    result = libprepa.extract_signal(filename)

    fig = plt.figure(figsize=(16, 9))

    # P
    ax_p = fig.add_subplot()
    p_tot = result[1].signal * result[2].signal
    line_p_tot, = ax_p.plot(
        result[0].signal, p_tot, label='Ptot')
    p_c = result[1].signal * result[3].signal
    line_p_c, = ax_p.plot(
        result[0].signal, p_c, label='Pc')
    p_rl = result[1].signal * result[4].signal
    line_p_rl, = ax_p.plot(
        result[0].signal, p_rl, label='Prl')
    ax_p.legend(bbox_to_anchor=(0, 1, 1, 1), loc='lower left', ncol=3)
    ax_p.grid(True)
    ax_p.set_xlabel('Temps (s)')
    ax_p.set_ylabel('Puissance (W)')

    # U
    ax_u = ax_p.twinx()
    ax_u._get_lines.prop_cycler = ax_p._get_lines.prop_cycler
    line_u = ax_u.plot(
        result[0].signal, result[1].signal, label='U')
    ax_u.legend(bbox_to_anchor=(0, 1, 1, 1), loc='lower right')
    ax_u.grid(True)
    ax_u.set_xlabel('Temps (s)')
    ax_u.set_ylabel('Tension (V)')

    fig.tight_layout()
    fig.savefig(output_name)

    print(f'valeur eff U {libprepa.get_eff(result[1].signal)}')
    print(f'valeur eff Itot {libprepa.get_eff(result[2].signal)}')
    print(f'valeur eff Ic {libprepa.get_eff(result[3].signal)}')
    print(f'valeur eff Irl {libprepa.get_eff(result[4].signal)}')

    print(f'valeur eff Ptot {libprepa.get_eff(p_tot)}')
    print(f'valeur eff Prl {libprepa.get_eff(p_rl)}')
    print(f'valeur eff Pc {libprepa.get_eff(p_c)}')
