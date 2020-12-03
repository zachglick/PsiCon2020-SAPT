import psi4
psi4.core.set_output_file('h2o_dimer_sapt2p3.out')
psi4.set_num_threads(6)

psi4.set_memory("60 GB")

h2o_dimer = psi4.geometry("""
0 1
O  -1.551007  -0.114520   0.000000
H  -1.934259   0.762503   0.000000
H  -0.599677   0.040712   0.000000
--
0 1
O   1.350625   0.111469   0.000000
H   1.680398  -0.373741  -0.758561
H   1.680398  -0.373741   0.758561
""")

psi4.set_options({"basis" : "jun-cc-pvdz"})
psi4.energy('sapt2+3', molecule=h2o_dimer)
