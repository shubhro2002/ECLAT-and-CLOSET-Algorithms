import matplotlib.pyplot as plt
import seaborn as sns

def plot_rules_scatter(rules_df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=rules_df,
                    x='confidence',
                    y='lift',
                    size='support',
                    hue='support',
                    sizes=(50, 500),
                    palette='viridis',
                    legend='full')

    plt.title('Association Rules: Confidence vs Lift')
    plt.xlabel('Confidence')
    plt.ylabel('Lift')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
