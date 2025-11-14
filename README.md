## NICU Patient Simulator

### Overview

This repository hosts the Neonatal Intensive Care Unit (NICU) Patient Simulator, a tool designed to generate realistic, synthetic physiological data and clinical scenarios for neonatal and preterm infants.

The primary goal of this project is to provide a high-fidelity data source for research and algorithm development. The simulator leverages Generative Adversarial Networks (GANs) to create data that accurately reflects both healthy and various pathological physiological states.

---

### Key Features

* Synthetic Data Generation: Produces realistic time-series data for critical NICU vital signs, including Heart Rate (HR), Respiratory Rate (RR) along with Bradycaria and Tachyardia effects.
* GAN-Powered Realism: Utilizes specialized GAN models (located in the `GAN_Codes` directory) to capture the complex statistical distributions and temporal dependencies present in real-world patient data.
* Modular Architecture: Built using Python scripts and interactive Jupyter Notebooks, facilitating an environment optimized for research, data exploration, model training, and scenario customization.
* Final Version Status: This repository represents the stable, culmination of development efforts, providing a reliable platform for simulation and testing.

---

### Setup and Installation

Follow these instructions to set up and run the simulation locally.

#### Prerequisites

| Category | Requirement | Notes |
| :--- | :--- | :--- |
| Software | Python 3.x, pip | Required for execution. |
| | Jupyter Notebook | Required for running `.ipynb` files and GAN training. |
| OS | Windows 10+, Linux (Arch/Ubuntu), macOS | |
| Containerization | Docker | *Optional* for containerized deployment. |
| Network | Stable broadband internet | Required for initial execution of the web GUI. |

#### Minimum Recommended Hardware

| Component | Minimum Specification | Notes |
| :--- | :--- | :--- |
| Processor | Intel i7 or AMD Ryzen 7 equivalent | |
| Memory (RAM) | 16 GB | |
| Storage | 256 GB SSD | Recommended for faster I/O. |
| GPU | NVIDIA RTX 2080 or higher with CUDA | *Optional*, but highly recommended for efficient GAN model training. |

#### Installation Steps

1.  Clone the Repository:
    ```bash
    git clone [https://github.com/GurshanRiarh/NICU_PatientSimulator.git](https://github.com/GurshanRiarh/NICU_PatientSimulator.git)
    cd NICU_PatientSimulator
    ```

2.  Create a Virtual Environment (Recommended):
    ```bash
    # Create the environment
    python -m venv nicu_venv
    
    # Activate the environment
    # Linux/macOS:
    source nicu_venv/bin/activate
    # Windows:
    .\nicu_venv\Scripts\activate
    ```

3.  Install Dependencies:
    Install the core libraries required for running the simulator and training the GANs.
    ```bash
    pip install numpy pandas scipy matplotlib plotly torch torchvision flask
    ```

    *Note: The `scipy.ndimage` dependency is included within the `scipy` installation.*

4.  Run the Simulation:
    The simulator runs on a local Flask server, accessible via a web browser.
    * Ensure your virtual environment is active.
    * Make sure that all paths in the dependant files are pointing to the right location (check csv files in other code files)
    * Execute the main simulation file:
        ```bash
        python Unhealthy_Version/Patient_Simulator_Unhealthy/UH_v25/GUI_Files/ExecuteSimulation.py
        ```
    * The simulator GUI will automatically open in your default web browser.

---

### Usage

#### Running the Simulator

To start the patient simulation:

* Run the file `ExecuteSimulation.py` (as detailed in the Installation steps).
* The simulator interface will open in a browser tab.
* Output Data: All generated patient time-series data is saved in the `Output_Patient_Data` folder, located within `PatientSimulator/Unhealthy_Version/Patient_Simulator_Unhealthy/UH_v25/`.

#### Training the GAN Models

The GANs must be trained and their path files saved before running the simulator to ensure accurate pathological data generation.

1.  Dependencies: Ensure all prerequisites (especially PyTorch and Jupyter Notebook) are installed.
2.  Data Pathing: Verify that the CSV data file paths in the individual GAN Notebooks are correct relative to your installation.
3.  Execution: Navigate to the respective GAN Notebook (`.ipynb` file) inside `PatientSimulator/GAN_Codes/` and execute the cells (e.g., `GAN_Heart_Normalized_TorchFast.ipynb`).
4.  Integration: The generated `.pth` model file must be placed into the `Trained_GAN_Path_Files` folder before running the main simulation.

---

### Repository Structure Highlights

#### Simulator Logic

| File/Module | Location | Description |
| :--- | :--- | :--- |
| `NICU_Simulator_Params_Unhealthy.py` | `.../UH_v25/` | Contains core simulator logic: GAN integration, vital sign generation, intervention, and pain management. |
| `ExecuteSimulation.py` | `.../UH_v25/GUI_Files/` | Manages the Flask server and logic for running the web-based simulation GUI. |
| `Vital_Sign_Interactive_Plots_Unhealthy.py` | `.../UH_v25/` | Logic for interactive plots using the Plotly library. |
| `Vital_Sign_Static_Plots_Unhealthy.py` | `.../UH_v25/` | Logic for static plots using the Matplotlib library. |

#### GAN Model Components

The `GAN_Codes` directory contains the training modules and data for the generative models.

| Component | Location | Description |
| :--- | :--- | :--- |
| `GAN_Heart_Normalized_TorchFast.ipynb` | `.../GAN_Heart_v2/` | Training logic for the normal preterm heart rate GAN. |
| `infant_2_8h_heart_rate_outlierRem.csv` | `.../GAN_Heart_v2/` | Cleaned CSV data used for normal heart rate training. |
| `GAN_Resp_Normalized_TorchFast.ipynb` | `.../GAN_Resp_v2/` | Training logic for the normal preterm respiration rate GAN. |
| `GAN_Bradycardia` folder | `PatientSimulator/GAN_Codes/` | Pre-processing, scaling, and training logic for synthetic Bradycardia generation. |
| `GAN_Tachycardia` folder | `PatientSimulator/GAN_Codes/` | Pre-processing, scaling, and training logic for synthetic Tachycardia generation. |

---

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### Contact

For inquiries or support regarding this project, please contact:

* Gurshan Riarh
* Email: Gurshanriarh@cmail.carleton.ca
* Project Link: [https://github.com/GurshanRiarh/NICU_PatientSimulator](https://github.com/GurshanRiarh/NICU_PatientSimulator)
