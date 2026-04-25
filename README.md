# Delivery Route Optimization (Linear Programming)

This repository contains a Python implementation of a **Transportation Problem** solved using Linear Programming. The project focuses on minimizing logistics costs while adhering to depot supply constraints and retail store capacities.

## Project Overview

The model optimizes the delivery of **6,850 units** of inventory from three regional depots to three retail locations. It calculates the most cost-effective shipping matrix based on distance-based pricing.

### Key Features
* **Cost Optimization:** Minimizes the total shipping expenditure using the `Highs` optimization solver.
* **Constraint Management:** * **Fixed Supply:** Ensures 100% of depot inventory is distributed.
    * **Store Capacity:** Respects the upper limits of receiving retail locations.
* **Automated Reporting:** Generates a shipping matrix and a slack analysis report (Capacity vs. Actual Delivery).

## Technical Specifications

* **Language:** Python 3
* **Libraries:** `SciPy` (Optimization), `NumPy` (Matrix operations), `Pandas` (Data reporting).
* **Algorithm:** Linear Programming (Simplex/Interior-Point via SciPy `linprog`).

## Results Summary
The model achieves an optimal solution with a total minimum cost of **£812,500.00**. It successfully identifies the most efficient routes while ensuring that depot inventory is fully cleared and store capacities are not exceeded.

## Repository Structure
* `app.py`: The core optimization script containing the logic and solver.
* `requirements.txt`: List of necessary Python packages.
* `README.md`: Project documentation.

## Setup & Usage
1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
