import numpy as np
import pandas as pd
from scipy.optimize import linprog

def solve_delivery():
    # --- 1. PARAMETERS ---
    P = 5.00  # Cost per unit distance
    depot_labels = ["D1", "D2", "D3"]
    store_labels = ["Store 1", "Store 2", "Store 3"]

    # Distance matrix (Depots x Stores)
    distances = np.array([
        [22, 33, 40],
        [27, 30, 22],
        [36, 20, 25],
    ])

    # Constraints
    supply_fixed = [2500, 3100, 1250]  # Total: 6850
    store_caps = [2000, 3000, 2000]    # Total: 7000

    # --- 2. OBJECTIVE FUNCTION ---
    # We want to minimize costs: distance * rate
    c = (distances * P).flatten()

    # --- 3. CONSTRAINTS ---
    # Equality Constraints: Every unit in the depots MUST be shipped
    A_eq = np.zeros((3, 9))
    for i in range(3):
        A_eq[i, 3*i : 3*i+3] = 1
    
    # Inequality Constraints: Cannot exceed store capacity
    A_ub = np.zeros((3, 9))
    for j in range(3):
        for i in range(3):
            A_ub[j, 3*i + j] = 1

    # --- 4. SOLVE ---
    res = linprog(
        c=c, 
        A_ub=A_ub, b_ub=store_caps, 
        A_eq=A_eq, b_eq=supply_fixed, 
        method="highs"
    )

    return res, depot_labels, store_labels, store_caps

if __name__ == "__main__":
    result, d_labels, s_labels, caps = solve_delivery()

    if result.success:
        optimal_x = result.x.reshape(3, 3).round(0)
        df = pd.DataFrame(optimal_x, index=d_labels, columns=s_labels)

        print(f"Total Minimum Cost (Z): £{result.fun:,.2f}")
        print("\nOptimal Shipping Matrix:")
        print(df)
        
        print("\n" + "="*30)
        print("CAPACITY VS ACTUAL DELIVERY")
        summary = pd.DataFrame({
            "Capacity": caps,
            "Delivered": optimal_x.sum(axis=0),
            "Slack": np.array(caps) - optimal_x.sum(axis=0)
        }, index=s_labels)
        print(summary)
    else:
        print("Optimization failed:", result.message)
