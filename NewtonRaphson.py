def newton_method(f, df, x0, tol=1e-5, max_iter=100):
    """
    Υλοποίηση της μεθόδου Newton-Raphson για την εύρεση ριζών μιας συνάρτησης.

    :param f: Η συνάρτηση της οποίας θέλουμε να βρούμε τη ρίζα.
    :param df: Η παράγωγος της συνάρτησης f.
    :param x0: Η αρχική προσέγγιση.
    :param tol: Το αποδεκτό όριο σφάλματος.
    :param max_iter: Ο μέγιστος αριθμός επαναλήψεων.
    :return: Η προσέγγιση της ρίζας.
    """
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        
        if dfx == 0:
            print("Η παράγωγος είναι μηδέν, σταματά η εκτέλεση.")
            return None

        x1 = x0 - fx / dfx
        
        if abs(x1 - x0) < tol:
            print(f"Η ρίζα βρέθηκε μετά από {i+1} επαναλήψεις: x = {x1}")
            return x1
        
        x0 = x1

    print(f"Η ρίζα δεν βρέθηκε μετά από {max_iter} επαναλήψεις.")
    return None

# Παράδειγμα χρήσης
def f(x):
    return x**2 - 4

def df(x):
    return 2 * x

root = newton_method(f, df, x0=2)
print("Προσέγγιση της ρίζας:", root)
