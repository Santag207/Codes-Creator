# Codes-Creator (QR and BarCode Creator)

## Description
**Codes-Creator** is a collection of Python scripts designed to generate and manage QR codes and barcodes for the management and development of the inventory of the JaVex Robotics seedbed of the Pontificia Universidad Javeriana, This is complemented by the application JaVex App. In addition, it includes tools to convert PNG images to PDF format, facilitating the organization and distribution of the generated codes.

## Team (Developer)
Santiago Castro Zuluaga

## Features
- **QR Code Generation:** Create custom QR codes from user-provided data.
- **Barcode Generation:** Create standard barcodes based on specific information.
- **PNG to PDF Conversion:** Convert PNG images into PDF documents for better management and sharing.

## Project Structure
The repository is organized as follows:

```
Codes-Creator
├── Documentation
├── Graphic_Resources
├── Designs
└── Code
    ├── qr-pruebas.py
    ├── BarCode.py
    ├── PNG-to-PDF.py
    ├── utils
    └── examples
```

### Explanation:

- Documentation: This folder contains all the documentation related to the project, including manuals, guides, and other reference materials.​

- Graphic_Resources: This directory holds graphical assets such as images, icons, and other visual elements used in the project.​

- Designs: This folder includes design files, mockups, and prototypes related to the project's development.​

- Code: This is the main directory containing the source code of the project.​

- qr-pruebas.py: Script for generating QR codes.​

- BarCode.py: Script for generating barcodes.​

- PNG-to-PDF.py: Script for converting PNG images to PDF documents.​

- utils: A subdirectory containing utility functions and helper scripts to support the main functionalities.​

- examples: A subdirectory with example codes and sample data demonstrating the usage of the main scripts.


## Requirements
- **Python 3.x:** Ensure you have a recent version of Python installed.
- **Additional Libraries:** Some functionalities require additional libraries such as `qrcode`, `PIL` (```Pillow```), and `reportlab`. You can install them using pip:

  ```
  pip install qrcode[pil] pillow reportlab
  ```
  
## Detailed Usage
### 1. QR Code Generation
The ```qr-pruebas.py``` script allows you to create QR codes from user-provided data.

#### Steps:
1) Open the terminal or command line and navigate to the directory containing ```qr-pruebas.py```.

2) Run the script by entering the following command:

  ```
  python qr-pruebas.py
  ```

3) Enter the data to encode when prompted.

4) View and save the QR code in the current directory as ```codigo_qr.png```.

### 2. Barcode Generation
The ```BarCode.py``` script facilitates the creation of barcodes based on specific information.

#### Steps:
1) Open the terminal or command line and navigate to the directory containing ```BarCode.py```.

2) Run the script by entering the following command:

```
python BarCode.py
```

3) Provide the necessary information as prompted.

4) View and save the barcode in the current directory as ```codigo_barras.png```.

### 3. PNG to PDF Conversion
The ```PNG-to-PDF.py``` script allows you to convert PNG images into PDF documents.

#### Steps:
1) Prepare the images by placing them in a specific folder, such as images/.

2) Open the terminal or command line and navigate to the directory containing ```PNG-to-PDF.py```.

3) Run the script by entering:

```
python PNG-to-PDF.py
```

Select the images to include in the PDF.

Generate and save the PDF in the current directory as ```document.pdf```.

Note: Ensure you have installed the necessary libraries (```qrcode```, ```Pillow```, ```reportlab```, etc.) before running the scripts:

```
pip install qrcode[pil] pillow reportlab
```

## Additional Notes
- Inventory: The Inventory/ directory may contain examples of generated codes or sample test data.

- Customization: The scripts are designed to be easily modified according to the user's specific needs.

## Contributions
Contributions are welcome. If you wish to improve or add new features, please follow these steps:

1) Fork the repository.

2) Create a new branch for your feature:

```
git checkout -b new-feature
```

3) Make your changes and commit them:

```
git commit -m 'Add new feature'
```

4) Push your changes to the remote repository:

```
git push origin new-feature
```

5) Open a pull request for review.
