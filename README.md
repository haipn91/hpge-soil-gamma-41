# MCNP-Simulated HPGe Soil Spectra

A public release of **6,000 MCNP-simulated HPGe gamma-ray spectra** for **41** common soil radionuclides, designed to accelerate machine-learning research in isotope identification and quantification.

## 📄 Manuscript

A manuscript describing this dataset and benchmarking results is currently **under preparation** for submission. A preprint will be made available here upon acceptance, or contact the authors at [haipn91@ioit.ai.vn] for a draft.

## 📂 Dataset

All data files are located in the `data/` folder:

- **`hpge-soil-gamma-41.npz`**  
  - Contains training and testing splits:  
    - `x_train` (4800×8192), `y_train` (4800×41)  
    - `x_test`  (1200×8192), `y_test`  (1200×41)  

- **`Spectra.csv`**  
  - The full set of 6,000 spectra (each row is an 8192-channel vector).

- **`Activity.csv`**  
  - Corresponding activity labels: columns are radionuclide names (41 columns), rows align with `Spectra.csv`.

The dataset is released under a **CC BY 4.0** license.

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
