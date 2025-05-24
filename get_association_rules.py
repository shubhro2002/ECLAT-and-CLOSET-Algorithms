import pandas as pd
import numpy as np
from itertools import combinations

def generate_association_rules(frequent_itemsets, transactions, min_confidence):
    rules = []
    total_transactions = len(transactions)

    for itemset in frequent_itemsets:
        if len(itemset) < 2:
            continue

        for i in range(1, len(itemset)):
            for antecedent in combinations(itemset, i):
                antecedent = frozenset(antecedent)
                consequent = itemset - antecedent

                support_itemset = frequent_itemsets[itemset] / total_transactions
                support_antecedent = frequent_itemsets.get(antecedent, 0) / total_transactions
                support_consequent = frequent_itemsets.get(consequent, 0) / total_transactions

                if support_antecedent == 0:
                    continue

                confidence = support_itemset / support_antecedent
                if confidence < min_confidence:
                    continue

                lift = confidence / support_consequent if support_consequent > 0 else 0
                leverage = support_itemset - (support_antecedent * support_consequent)
                conviction = (1 - support_consequent) / (1 - confidence) if confidence < 1 else np.inf
                jaccard = support_itemset / (support_antecedent + support_consequent - support_itemset) if (support_antecedent + support_consequent - support_itemset) != 0 else 0
                kulczynski = 0.5 * (support_itemset / support_antecedent + support_itemset / support_consequent) if support_consequent > 0 else 0
                zhang = leverage / max(support_itemset * (1 - support_antecedent), support_antecedent * (support_consequent - support_itemset)) if max(support_itemset * (1 - support_antecedent), support_antecedent * (support_consequent - support_itemset)) != 0 else 0
                certainty = (support_itemset - support_antecedent * support_consequent) / (support_antecedent * (1 - support_consequent)) if (support_antecedent * (1 - support_consequent)) != 0 else 0
                representativity = support_itemset / support_antecedent if support_antecedent > 0 else 0

                rules.append({
                    'antecedents': antecedent,
                    'consequents': consequent,
                    'antecedent support': support_antecedent,
                    'consequent support': support_consequent,
                    'support': support_itemset,
                    'confidence': confidence,
                    'lift': lift,
                    'leverage': leverage,
                    'conviction': conviction,
                    'jaccard': jaccard,
                    'kulczynski': kulczynski,
                    'zhangs_metric': zhang,
                    'certainty': certainty,
                    'representativity': representativity,
                })

    return pd.DataFrame(rules).sort_values(by='lift', ascending=False).reset_index(drop=True)
