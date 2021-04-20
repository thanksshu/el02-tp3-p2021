'''
useful functions for el02 tp3
'''

import csv
from types import SimpleNamespace as SN

import numpy as np


# def add(signal_1: np.ndarray, signal_2: np.ndarray) -> np.ndarray:
#     ''' calculate addtion of two signal '''
#     return signal_1 + signal_2


# def minus(signal_1: np.ndarray, signal_2: np.ndarray) -> np.ndarray:
#     ''' calculate difference of two signal '''
#     return signal_1 - signal_2


# def multiply(signal_1: np.ndarray, signal_2: np.ndarray) -> np.ndarray:
#     ''' calculate multiplication of two signal '''
#     return signal_1 * signal_2


def get_mean(signal: np.ndarray) -> np.ndarray:
    ''' calculate moyenne of a signal. '''
    return signal.mean()


def get_peak(signal: np.ndarray) -> np.ndarray:
    ''' calculate peak value of a signal. '''
    return max(max(signal), - min(signal))


def get_eff(signal: np.ndarray) -> np.ndarray:
    ''' calculate efficace value of a signal. '''
    return np.sqrt(signal.dot(signal) / len(signal))


def extract_signal(filename: str) -> list:
    ''' 
    read a signal csv file then extract signals inside.

    return a list containing multiple namespace, namespace has 'name' and 'signal'
    
    e.g.
        [namespace(name='TIME', signal=array([5,2,4])),
        namespace(name='CH1', signal=array([1,2,3))]
    '''
    # read file
    result = list()
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        array_signal = np.loadtxt(
            filename, delimiter=',', skiprows=1).transpose()
        for i, name in enumerate(reader.__next__()):
            result.append(SN(name=name, signal=array_signal[i].copy()))
    return result
