import psi4
import numpy as np
import matplotlib.pyplot as plt

har2kcalmol = 627.509
psi4.core.set_output_file('bz_dimer_sapt.out')
psi4.set_memory("60 GB")
psi4.set_num_threads(6)
psi4.set_options({"basis" : "jun-cc-pvdz"})

def run_sapt(mol):

    psi4.energy('sapt2', molecule=mol)
    return (har2kcalmol * psi4.variable('SAPT TOTAL ENERGY'),
            har2kcalmol * psi4.variable('SAPT ELST ENERGY'),
            har2kcalmol * psi4.variable('SAPT EXCH ENERGY'),
            har2kcalmol * psi4.variable('SAPT IND ENERGY'),
            har2kcalmol * psi4.variable('SAPT DISP ENERGY'))


if __name__ == '__main__':

    rs = np.linspace(3.7, 7.0, 15)
    energies = []
    for r_cc in rs:
        bz_dimer = psi4.geometry(f"""
        0 1
        C      0.000000000000     {r_cc}     1.391500000000
        H      0.000000000000     {r_cc}     2.471500000000
        C      1.205074349366     {r_cc}     0.695750000000
        H      2.140381785453     {r_cc}     1.235750000000
        C      1.205074349366     {r_cc}    -0.695750000000
        H      2.140381785453     {r_cc}    -1.235750000000
        C     -0.000000000000     {r_cc}    -1.391500000000
        H     -0.000000000000     {r_cc}    -2.471500000000
        C     -1.205074349366     {r_cc}    -0.695750000000
        H     -2.140381785453     {r_cc}    -1.235750000000
        C     -1.205074349366     {r_cc}     0.695750000000
        H     -2.140381785453     {r_cc}     1.235750000000
        --
        0 1
        C     -1.205074349366     0.000000000000    -0.695750000000
        H     -2.140381785453     0.000000000000    -1.235750000000
        C     -0.000000000000     0.000000000000    -1.391500000000
        H     -0.000000000000     0.000000000000    -2.471500000000
        C      1.205074349366     0.000000000000    -0.695750000000
        H      2.140381785453     0.000000000000    -1.235750000000
        C      1.205074349366     0.000000000000     0.695750000000
        H      2.140381785453     0.000000000000     1.235750000000
        C     -0.000000000000     0.000000000000     1.391500000000
        H     -0.000000000000     0.000000000000     2.471500000000
        C     -1.205074349366     0.000000000000     0.695750000000
        H     -2.140381785453     0.000000000000     1.235750000000
        """)
        energies.append(run_sapt(bz_dimer))
        print(f'\nDistance {r_cc:.2f}') 
        print(f'  Total={energies[-1][0]:.4f}')
        print(f'  Elst={energies[-1][1]:.2f}') 
        print(f'  Exch={energies[-1][2]:.2f}') 
        print(f'  Ind={energies[-1][3]:.2f}') 
        print(f'  Disp={energies[-1][4]:.2f}') 

    
    labels = ['Total', 'Elst', 'Exch', 'Ind', 'Disp']
    colors = ['k', 'red', 'green', 'blue', 'orange']

    for i, label in enumerate(colors):
        plt.plot(rs, [energy[i] for energy in energies], color=colors[i])
    plt.xlabel('Benzene Dimer Separation ($\mathrm{\AA}$)')
    plt.xlim(rs[0], rs[-1])
    plt.ylabel('Interaction Energy (kcal / mol)')
    plt.savefig('bz_dimer_sapt.pdf')
