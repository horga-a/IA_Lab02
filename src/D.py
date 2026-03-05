import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def generate_iris_report():
    """
    Generează un raport comparativ complet pentru dataset-ul Iris.
    Creează două figuri: un pairplot și un set de violinplots.
    """
    # Încărcarea dataset-ului Iris
    iris = sns.load_dataset('iris') 
 
 # 1. Generarea pairplot-ului complet cu hue='species' și diag_kind='kde'
    print("Generare pairplot...")
    pairplot_fig = sns.pairplot(iris, hue='species', diag_kind='kde')
    pairplot_fig.fig.suptitle('Pairplot Complet - Dataset Iris', y=1.02, fontsize=16)
    
    # Salvare pairplot
    pairplot_fig.savefig('iris_pairplot.png', dpi=300, bbox_inches='tight')
    print("Pairplot salvat ca 'iris_pairplot.png'")
    
    # 2. Crearea figurii cu 4 subploturi (1×4) - violinplots
    print("Generare violinplots...")
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    
    # Lista variabilelor numerice
    numeric_vars = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    labels = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
    
    # Crearea unui violinplot pentru fiecare variabilă
    for idx, (var, label) in enumerate(zip(numeric_vars, labels)):
        sns.violinplot(data=iris, x='species', y=var, hue='species', 
                      split=False, ax=axes[idx], legend=False)
        axes[idx].set_title(label, fontsize=12, fontweight='bold')
        axes[idx].set_xlabel('Species', fontsize=10)
        axes[idx].set_ylabel(label + ' (cm)', fontsize=10)
    
    # Adăugarea titlului general
    fig.suptitle('Comparație Variabile Numerice - Dataset Iris (Violinplot)', 
                 fontsize=16, fontweight='bold', y=1.02)
    
    # Ajustarea layout-ului
    plt.tight_layout()
    
    # Salvarea figurii cu violinplots
    plt.savefig('iris_violinplots.png', dpi=300, bbox_inches='tight')
    print("Violinplots salvate ca 'iris_violinplots.png'")
    
    # Afișarea figurilor
    plt.show()
    
    print("\nRaport finalizat cu succes!")
    print(f"Statistici dataset: {iris.shape[0]} observații, {iris.shape[1]} coloane")
    print(f"Specii: {iris['species'].unique().tolist()}")


if __name__ == "__main__":
    generate_iris_report()
