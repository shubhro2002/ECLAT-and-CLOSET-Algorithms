# Transaction Pattern Mining using ECLAT and CLOSET+

## 📊 Project Overview

This project explores frequent itemset mining and association rule generation using **ECLAT** and **CLOSET+** algorithms. The primary objective is to uncover hidden patterns and relationships within transactional data by extracting frequent itemsets and generating insightful rules that can support decision-making processes in domains such as retail, e-commerce, and market basket analysis.

## 🧠 Algorithms Used

### 1. ECLAT (Equivalence Class Clustering and bottom-up Lattice Traversal)
- A depth-first search algorithm that uses a vertical data format for efficient mining of frequent itemsets.
- Particularly suitable for datasets with many frequent items or dense datasets.

### 2. CLOSET+
- An improved version of the CLOSET algorithm for mining **closed frequent itemsets**.
- Reduces redundancy by focusing only on closed itemsets, which are maximal frequent itemsets with no superset having the same support.
- Offers better performance in terms of space and time complexity compared to classic frequent pattern mining techniques.

## 📁 Dataset

The dataset consists of transactional records where each transaction contains a set of items purchased together.

**Example Format:**

T1: Milk, Bread, Butter

T2: Bread, Butter

T3: Milk, Bread

...


## 🔍 Project Workflow

1. **Data Preprocessing**  
   - Transactions are cleaned and transformed into the required input format for mining algorithms.

2. **Frequent Itemset Mining**  
   - ECLAT is applied to discover frequent itemsets based on minimum support thresholds.
   - CLOSET+ is used to mine **closed** frequent itemsets.

3. **Rule Generation**  
   - From the mined itemsets, association rules are generated.
   - Rules are evaluated using confidence and other relevant metrics.

4. **Output & Analysis**  
   - Frequent itemsets and association rules are stored and visualized for interpretation.
   - Comparative insights between ECLAT and CLOSET+ outputs are discussed.

## 🛠️ Technologies & Tools

- Python
- custom implementations for mining algorithms
- Pandas & NumPy for data manipulation
- Matplotlib / Seaborn for visualization

## 📈 Sample Output

**Frequent Itemsets:**
{Milk, Bread} – Support: 0.6
{Bread, Butter} – Support: 0.5


**Generated Rules:**
{Milk} => {Bread} (Confidence: 0.75)
{Bread, Butter} => {Milk} (Confidence: 0.6)


## 📌 How to Run

Clone the repository:
```bash
 git clone https://github.com/shubhro2002/ECLAT-and-CLOSET-plus-Algorithms.git
 cd transaction-pattern-mining
