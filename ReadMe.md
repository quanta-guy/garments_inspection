# Garments Inspection System

Welcome to the Vision based Garments Inspection! This repository contains scripts and resources for inspecting garments using computer vision techniques. This guide provides instructions on how to set up the environment, run the scripts, and contribute to the repository.

## Setup

1. **Clone the Repository**: Clone the **garments_inspection** repository to your local machine:

```bash

git clone https://github.com/quanta-guy/garments_inspection.git 
cd garments_inspection 
```

2. **Create Conda Environment**: Create a new conda environment and install the required packages listed in **requirements.txt**:

```bash

conda create --name garments_inspection python=3.9.16 
conda activate garments_inspection 
pip install -r requirements.txt 
```
3. **Edit Scripts**: Edit the scripts (**Canny.py**, **defect.py**, **color_defect.py**) to configure the video camera source link:
   1. Open **Canny.py**, **defect.py**, and **color_defect.py** in a text editor.
   2. Find the video camera source link configuration and modify it to your camera source.
4. **Download**: Download this [file](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8x-pose-p6.pt) and copy it into measurement_stain>models directory

## Usage

**Running Scripts**

1. **Defect Detection**: Run the defect detection script from the **measurement_stain** directory:

```bash
cd measurement_stain 
python defect.py 
```
2. **Color Defect Detection**: Run the color defect detection script from the root directory:

```bash
cd .. 
python color_defect.py 
```
3. **Edge Detection**: Run the edge detection script from the **Overlapper** directory:

```bash
cd Overlapper 
python canny.py 
```
##Contribution

This project is still under development. If you would like up to add something please mail to us @[Vishnukanth.S](mailto:vkanthishnu@gmail.com)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

