# MCNP-Simulated HPGe Soil Spectra

A public release of **6,000 MCNP-simulated HPGe gamma-ray spectra** for **41** common soil radionuclides, designed to accelerate machine-learning research in isotope identification and quantification.

## 📄 Manuscript

A manuscript describing this dataset and benchmarking results is currently **under preparation** for submission. A preprint will be made available here upon acceptance, or contact the authors at [haipn91@ioit.ai.vn] for a draft.

## 📂 Dataset

Due to GitHub file size limits, the large spectral files are hosted externally.  
All dataset components are freely available under a **CC BY 4.0** license:

- [**Spectra.csv**](https://drive.google.com/file/d/1pwHIeBFBW0vxcsvZKDMRbV3zPk6LtDF1/view?usp=sharing)  
  - Full set of 6,000 spectra (each row is an 8192-channel vector).

- [**hpge-soil-gamma-41.npz**](https://drive.google.com/file/d/16Bxfsa7TMqq65eRUCAdNwGt-UYQaiB1c/view?usp=sharing)  
  - Pre-split training/testing arrays:  
    - `x_train` (4800×8192), `y_train` (4800×41)  
    - `x_test`  (1200×8192), `y_test`  (1200×41)  

- **`Activity.csv`** (included in this repository)  
  - Corresponding activity labels: columns are radionuclide names (41 columns), rows align with `Spectra.csv`.

👉 For convenience, a text file [`link_download.txt`](./data/link_download.txt) is also provided in the `data/` folder containing the same download links.

## ⚛️ MCNP Input Decks

To ensure full reproducibility, we also provide the **MCNP input files** used to generate the dataset:

- **`Out0000`**  
  - Defines the HPGe detector and soil-container geometry.  
  - Material compositions (Ge, soil matrix, polystyrene, aluminum, copper, air).  
  - Photon source definitions (energies and branching ratios from NuDat 3.0 and Nucléide-Lara).  
  - Tally settings (F8:P pulse-height tally, 8192 channels).  
  - Physics cards (photoelectric effect, Compton scattering, pair production; 10 keV cut-off).  
  - Explicit random-number seed.

These input decks allow researchers to regenerate spectra under the same simulation conditions or extend the setup to new scenarios.

## 🚀 Quickstart

```bash
# Clone the repo
git clone https://github.com/haipn91/hpge-soil-gamma-41.git
cd hpge-soil-gamma-41


# Load the data in Python
import numpy as np

data = np.load('../data/hpge-soil-gamma-41.npz')
x_train, y_train = data['x_train'], data['y_train']
x_test,  y_test  = data['x_test'],  data['y_test']
```

## 📊 Benchmarks
We include example notebooks under `examples/` to reproduce our baseline results:

- **Ridge Regression** and **XGBoost**: `examples/Machine_learning_regression.ipynb`  
- **MLP** and **CNN**: `examples/Neural_net_pytorch_regression.ipynb`

## License

### Dataset  
The MCNP-simulated HPGe soil gamma-ray spectra are released under the  
[Creative Commons Attribution 4.0 International Public License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/legalcode).

### Code  
All example code and notebooks in this repository are released under the  
[MIT License](https://opensource.org/licenses/MIT).  
