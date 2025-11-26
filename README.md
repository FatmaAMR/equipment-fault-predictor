# Equipment Fault Detector

**Anomaly & Failure Prediction Using Machine Learning + FastAPI + Streamlit**
A a complete end-to-end system for detecting potential equipment failures using IoT sensor data (temperature, pressure, vibration, humidity).

## Tech Stack
### Backend

- FastAPI

- Uvicorn

- Pydantic\

- Scikit-learn

- Pandas

### Frontend

- Streamlit

- Requests (HTTP client)

### ML

- RandomForestClassifier (Acc: 98%)

- IoT sensor [dataset](https://www.kaggle.com/datasets/dnkumars/industrial-equipment-monitoring-dataset) (temp/pressure/vibration/humidity)

## Setup

### 1. Environment Setup

To ensure smooth development and avoid Python version or package conflicts, please follow the setup instructions below.

---

#### Option 1: Windows (Local Development)

Install Miniconda **once** on Windows and create your project environment:


**1.1. Download and install Miniconda for Windows from [Anacona website](https://docs.anaconda.com/miniconda/install/)**

**1.2. Create the project environment**
`conda create -n egypt_travel_assistant python=3.8`

**1.3. Activate the environment**
`conda activate egypt_travel_assistant`


💡 If you plan to run everything only on Windows, no further installations are required.

#### Option 2: WSL / Ubuntu (Linux-like Environment)

For production compatibility or Linux-based development, use WSL with a separate Miniconda installation inside Ubuntu.


##### Step 1: Install WSL
Run in PowerShell as Administrator:
`wsl --install`

> 🐧 Ubuntu will be installed by default. After 
> installation, open Ubuntu and navigate to your
> project folder.


##### Step 2: Open the Project in VS Code

```
cd /mnt/c/path/to/project
code .
```


##### Step 3: Download Miniconda

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

##### Step 4: Make Installer Executable

`chmod +x Miniconda3-latest-Linux-x86_64.sh`

##### Step 5: Install Miniconda

`./Miniconda3-latest-Linux-x86_64.sh`

When prompted: 
> You can undo this by running 'conda init --reverse $SHELL'? [yes|no]

Enter **yes**.


⚠️ Now Restart your terminal.

You now have a separate Miniconda environment inside Ubuntu. Create your project environment as usual:

```
conda create -n egypt_travel_assistant python=3.8
conda activate egypt_travel_assistant
```

**Notes**
- Each system (Windows / WSL) maintains its own Conda installation.

- Always activate the appropriate environment before installing dependencies or running the project.


### 2. Installations
Installing required packages by implementing the command 
```bash
$ pip install -r requirements.txt
```

### 3. Environments variables Setup

```bash
$ cp .env.examples .env
```

### 4. Run the API

```bash
$ uvicorn app.main:app 
```


### 5. Frontend Setup (Streamlit UI)
```bash
streamlit client/run ui.py
```