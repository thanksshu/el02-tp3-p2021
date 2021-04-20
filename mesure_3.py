'''
EL02 -- TP3 : acquisition de signaux numeriques sur reseau domestique 
@author: SHangyuan Han, Samy Devaud, Matthieu Guinouard
'''
import matplotlib.pyplot as plt

import libprepa

if __name__ == '__main__':
    filename = 'mesure_3.csv'

    # read file
    result = libprepa.extract_signal(filename)

    time = result[0].signal
    u_edf = result[1].signal
    i_l = result[2].signal
    i_r = result[3].signal
    u_s = result[4].signal

    print(f'valeur moy Uedf-Us {libprepa.get_mean(u_edf - u_s)}')
    print(f'valeur eff Uedf {libprepa.get_eff(u_edf)}')
    print(f'valeur eff Us {libprepa.get_eff(u_s)}')
    i_sum = i_r + i_l
    print(f'valeur eff Ir {libprepa.get_eff(i_r)}')
    print(f'valeur eff Il {libprepa.get_eff(i_l)}')
    print(f'valeur max de Ir+Il {libprepa.get_peak(i_sum)}')
    print(f'valeur eff de Ir+Il {libprepa.get_eff(i_sum)}')
