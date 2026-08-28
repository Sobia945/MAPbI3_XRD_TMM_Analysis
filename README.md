
# 🔬 MAPbI3_XRD_TMM_Analysis


This project presents a Python-based characterization and optical analysis of methylammonium lead iodide (MAPbI₃) perovskite. It combines two complementary approaches:

1. **XRD Structural Characterization** — analysis of the crystal structure using Bragg's Law and the Scherrer equation.
2. **Optical & Transfer Matrix Method (TMM) Analysis** — analysis of the optical properties using experimental refractive-index data and TMM-based modeling of thin-film optical response.


---
# 1. MAPbI3 XRD Analysis

## Theory

### Bragg's Law

**d = λ / (2 sin θ)**

| Symbol | Meaning             |
| ------ | ------------------- |
| **d**  | Interplanar spacing |
| **λ**  | X-ray wavelength    |
| **θ**  | Diffraction angle   |

### Scherrer Equation
**D = (Kλ) / (β cos θ)**


| Symbol | Meaning                           |
| ------ | --------------------------------- |
| **D**  | Crystallite size                  |
| **K**  | Shape factor (0.94)               |
| **λ**  | X-ray wavelength                  |
| **β**  | Full Width at Half Maximum (FWHM) |
| **θ**  | Diffraction angle                 |

## Constants

* **X-ray source:** Cu Kα radiation
* **Wavelength (λ):** 0.15406 nm
* **Shape factor (K):** 0.94

---

## Workflow

```text
Input XRD Peak Data
        │
        ▼
Apply Bragg's Law
        │
        ▼
Calculate d-spacing
        │
        ▼
Apply Scherrer Equation
        │
        ▼
Estimate Crystallite Size
        │
        ▼
Visualize Results
```

---

## Results

### Input Data

| Peak | 2θ (°) | FWHM (°) |
| ---- | ------ | -------- |
| 1    | 14.02  | 0.15     |
| 2    | 28.42  | 0.18     |
| 3    | 31.85  | 0.20     |

### Calculated Results

| Peak | d-spacing (nm) | Crystallite Size (nm) |
| ---- | -------------- | --------------------- |
| 1    | 0.6312         | 55.73                 |
| 2    | 0.3138         | 47.55                 |
| 3    | 0.2807         | 43.14                 |

The calculated d-spacing values agree well with reported values for the characteristic diffraction planes of tetragonal MAPbI₃. The estimated crystallite sizes range from approximately **43–56 nm**, indicating the polycrystalline nature of the material.

## XRD Analysis Plot

![XRD Analysis Plot](xrd_plot.png)

---

## Features

* Calculates interplanar d-spacing using Bragg's Law
* Estimates crystallite size using the Scherrer Equation
* Processes multiple diffraction peaks
* Generates graphical visualization with Matplotlib
* Clean and well-documented Python implementation

---

 # 2. Optical TMM Analysis

The XRD analysis showed the crystal structure of MAPbI₃, but not how it interacts with light — that is where this part comes in. Using experimentally reported refractive index and extinction coefficient (n, k) data from Phillips et al. (2015), an Air/MAPbI₃/Glass stack was modeled with the Transfer Matrix Method (TMM) to calculate how reflectance, transmittance, and absorptance vary with wavelength, film thickness, and angle of incidence. The simulated absorptance was then compared with experimental EQE data from Lin et al. (2015), showing a similar spectral trend and absorption edge near the MAPbI₃ bandgap.

See the `Optical_TMM/` folder for the full analysis, notebook, and dataset.

## Repository Structure

```text
MAPbI3_XRD_Analysis/
│
├── XRD_Analysis.py
├── XRD_Plot.py
├── xrd_plot.png
└── README.md
```

---

## Installation

Install the required package:

```bash
pip install matplotlib
```

---

## Usage

### Run the structural analysis

```bash
python XRD_Analysis.py
```

Outputs the calculated interplanar spacing and crystallite size for each diffraction peak.

### Generate the visualization

```bash
python XRD_Plot.py
```

Creates and saves the output figure as:

```text
xrd_plot.png
```

---

## Future Improvements

* Read XRD peak data directly from CSV files
* Automatic peak detection
* Miller index assignment
* Williamson–Hall analysis
* Comparison with reported literature values
* Error propagation and uncertainty analysis
* Support for experimental XRD datasets
* Interactive plotting using Plotly

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Author

**Sobia Asghar**

BS Physics, The Islamia University of Bahawalpur, Pakistan

GitHub: https://github.com/Sobia945

