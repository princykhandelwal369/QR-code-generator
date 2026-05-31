# QR Code Generator

A simple Python project that generates QR codes from user-provided text or URLs. The program encodes the input data, applies error correction, and saves the generated QR code as an image.

## Features

* Accepts any text or URL as input
* Encodes data into QR code format
* Applies high-level error correction
* Generates a PNG image of the QR code
* Simple and beginner-friendly implementation

## Project Workflow

```text
User Input
    ↓
Data Encoding
    ↓
Error Correction
    ↓
QR Code Generation
    ↓
Image Creation
    ↓
Save as PNG
```

## Technologies Used

* Python 3
* qrcode library
* Pillow (PIL) for image handling

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/qr-code-generator.git
cd qr-code-generator
```

2. Install dependencies:

```bash
pip install qrcode pillow
```

## Usage

Run the program:

```bash
python main.py
```

Enter the text or URL when prompted:

```text
Enter text or URL to generate QR Code:
https://github.com
```

The generated QR code will be saved as:

```text
qrcode.png
```

## Example

Input:

```text
https://github.com
```

Output:

```text
QR Code generated successfully!
Saved as 'qrcode.png'
```

## How It Works

### 1. Data Input

The user enters text, a URL, or any information to be encoded.

### 2. QR Encoding

The input data is converted into a QR-compatible format.

### 3. Error Correction

Additional recovery data is added to the QR code. This allows scanners to read the code even if a portion of it is damaged.

### 4. Image Generation

The QR matrix is converted into a PNG image.

### 5. Save Output

The generated QR code is saved locally for sharing or printing.

## Error Correction Levels

| Level | Recovery Capacity |
| ----- | ----------------- |
| L     | 7%                |
| M     | 15%               |
| Q     | 25%               |
| H     | 30%               |

This project uses **Level H**, providing the highest error recovery capability.

## Project Structure

```text
qr-code-generator/
│
├── main.py
├── qrcode.png
└── README.md
```

## Future Improvements

* Custom QR colors
* Logo embedding
* GUI version using Tkinter
* Batch QR generation
* Different image formats (JPG, SVG)


