# Jasueng Ku
# kirssQ is a python package for qubit measurement and related useful libraries.
# Below I outline things that I'd like to include in the package

# General rules for design 
    - Design for interface.
    - How to configure experiments
    - Make it modular
    - Make it easy for scripting
    - Make it easy to extend
    - Obey SOLID principle as much as possible
        - Single responsibility principle
        - Open-closed principle: open for  extension, close for modification
        - Liskov substitution principle
        - Interface segregation principle
        - Dependency inversion principle
    - Obey PEP8

1. krissqgl: kriss Quantum Gate Language package
   - Act as an interface layer between gate layer and physical hardware's API to define pulse sequences
     (no need to know each AWG's language/API)
   - Use gates in most cases (without knowing how to create them in reality) in defining pulse seqs.
   - Would this be practical for ZI and QM?

   Modules:
        - Channels: qubit(), readout(), logical channel, physical channel, channelmapper
        - Pulseprimatives (Utheta, Xtheta, Ytheta, CR, echoCR, rotaryCR, ...)
        - Pulsequencer : define pulse sequences
        - Pulseshapes: define shapes of pulses
        - Pulsecollection (collections of functions or classes) 
            - characterization: spec, Rabi, Ramsey, Echo, T1, decoupling..
            - calibration: RabiampCal, PiCal, Pi2Cal, DragCal, CR ... 
            - verification: RB, QST, QPT, HamiltonianTomo, GST,...
        - PulseSeqPlotter
    Directory:
        - drivers: ZI, QM, ...

2. krissqm: kriss quantum measurement package 
    
    # package/module/class
    - experiment (FileHandler, Sweeper, ...)
    - instruments
          - various instrument drivers here
          - AgilentE8257D
          - SIM928
    - analysis
        - fitting (T1, Ramsey,...)
        - characterization
    - utility (load_data, plotting, ...)
    - plotter
    - pulse
    - calibration

3. krissanalysis: kriss analysis library
   - Fittings
        - T1, Ramsey, DragFit, CRFit, ...
        - Resonator fit, ...
        - QST, QPT,... fits
        - HamiltonianTomoFit, 

3. krisslib: library of experiments for calibration, characterization and verification
             sort of list of standard toolkit, something that can be used routinely.
    A. calibration
        -PulseCal
            - FreqCal
            - RabiAmpCal
            - DragCal
            - Pi2Cal
            - PiCal
            - CRAmpCal
            - CRPhaseCal
            - CRLengthCal
    B. characterization
        - spectroscopy
        - T1, Ramsey, Echo
        - readout assignment fidelity
        - Effective temperature meas
    C. verification: tomography, benchmarking,  ...
        - QST: 1Q, 2Q
        - QPT: 1Q, 2Q
        - RB:1Q, 2Q
        - Leakage RB
        - Purity RB
        - Cycle benchmarking (CB)
        - Cross entropy benchmarking (XEB)
        - GST
        - QV (Quantum Volume)

