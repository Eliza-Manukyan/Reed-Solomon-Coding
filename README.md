# Reed-Solomon Error Correction Encoder & Decoder

![Project Status](https://img.shields.io/badge/Status-Complete-green)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Topic](https://img.shields.io/badge/Coding_Theory-Reed--Solomon-purple)

---

## Project Overview

This project provides a Python implementation of a **Reed-Solomon (RS) error-correcting code system**. Reed-Solomon codes are powerful non-binary cyclic codes used to detect and correct multiple symbol errors in a block of data. They are widely used in digital communications and data storage systems where errors are common, such as:

- **Data Storage:** CDs, DVDs, Blu-ray Discs, QR codes
- **Broadcast Systems:** DVB and ATSC
- **High-Speed Modems:** ADSL, xDSL

This implementation demonstrates the core mathematical principles of RS codes, including polynomial representation over a **Galois Field (GF)**, encoding, and the complete decoding process to recover the original message from a corrupted one.

---

## How It Works

The process is broken down into three main stages:

1.  **Encoding**:

    - The input message is treated as a polynomial `m(x)` over a Galois Field (typically `GF(2^8)`).
    - A generator polynomial `g(x)` is created based on the desired error-correction capability (`t`).
    - The message polynomial is multiplied by `x^(2t)` and then divided by the generator polynomial to find the remainder `b(x)`.
    - The transmitted codeword `c(x)` is the sum of the shifted message and the remainder: `c(x) = m(x) * x^(2t) + b(x)`. This ensures that the codeword is perfectly divisible by `g(x)`.

2.  **Error Simulation**:

    - To test the decoder, errors are intentionally introduced into the transmitted codeword `c(x)` to create a received (and corrupted) polynomial `r(x)`.

3.  **Decoding**:
    The decoding algorithm is the most complex part and follows these steps to find and correct the errors:
    - **Syndrome Calculation**: The received polynomial `r(x)` is evaluated at the roots of the generator polynomial `g(x)`. If all syndromes are zero, there are no errors. Non-zero syndromes indicate the presence of errors.
    - **Berlekamp-Massey Algorithm**: The syndromes are used to find the **error locator polynomial**, `σ(x)`. The roots of this polynomial reveal the _locations_ of the errors in the received message.
    - **Chien Search**: This is an efficient algorithm to find the roots of the error locator polynomial, thus identifying the positions of the corrupted symbols.
    - **Forney's Algorithm**: Once the error locations are known, this algorithm calculates the _values_ of the errors at those positions.
    - **Correction**: The calculated error values are subtracted from the received polynomial `r(x)` at the identified error locations, successfully restoring the original codeword `c(x)` and recovering the original message.

---

## Prerequisites

You need **Python 3.x** and the following library:

- **NumPy**: For numerical operations, particularly with polynomial representations.

### Installation

If you do not have NumPy installed, you can install it via pip:

```bash
pip install numpy
```

---

## How to Run

1.  Clone or download the repository.
2.  Navigate to the project directory.
3.  Run the main script from your terminal:
    ```bash
    python main.py
    ```

The script will execute a complete encode-decode cycle with a sample message. It will print the original message, the encoded codeword, the corrupted codeword (after adding errors), and the final decoded message, demonstrating that the errors were successfully corrected.
