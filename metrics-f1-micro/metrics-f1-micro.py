import numpy as np
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_true=np.array(y_true, dtype=float)
    y_pred=np.array(y_pred, dtype=float)
    tp=np.sum(y_true==y_pred)
    
    total=len(y_true)

    fp = total - tp
    fn = total - tp
    f1 = (2 * tp) / (2 * tp + fp + fn)
    return float(f1)
    pass