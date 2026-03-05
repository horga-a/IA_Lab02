import seaborn as sns
import matplotlib.pyplot as plt



def main():
    tips = sns.load_dataset("tips")

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    ax = axes[0, 0]
    sexes = tips['sex'].unique()
    for sex in sexes:
        subset = tips[tips['sex'] == sex]
        ax.scatter(subset['total_bill'], subset['tip'], label=sex, alpha=0.7)
    ax.set_title('Total bill vs Tip (color by sex)')
    ax.set_xlabel('Total bill')
    ax.set_ylabel('Tip')
    ax.legend(title='Sex')

    ax = axes[0, 1]
    order = ['Thur', 'Fri', 'Sat', 'Sun']
    sns.boxplot(x='day', y='total_bill', data=tips, order=order, ax=ax)
    ax.set_title('Distribuție total_bill per zi')
    ax.set_xlabel('Ziua')
    ax.set_ylabel('Total bill')

    ax = axes[1, 0]
    sns.histplot(data=tips, x='tip', hue='time', kde=True, ax=ax)
    ax.set_title('Histograma bacșiș tip (hue=time)')
    ax.set_xlabel('Tip')
    ax.set_ylabel('Densitate')

    ax = axes[1, 1]
    sns.barplot(x='day', y='tip', data=tips, order=order, ci='sd', ax=ax)
    ax.set_title('Bacșiș mediu per zi')
    ax.set_xlabel('Ziua')
    ax.set_ylabel('Tip mediu')

    plt.tight_layout()
    plt.savefig('tips_grid.png', dpi=300)
    print("Figura a fost salvată ca tips_grid.png")


if __name__ == '__main__':
    main()
