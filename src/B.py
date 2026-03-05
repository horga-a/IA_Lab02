import seaborn as sns


def main():
    tips = sns.load_dataset("tips")

    print("1. Shape:", tips.shape)
    print("Types:\n", tips.dtypes)
    print("Describe:\n", tips.describe(), "\n")

  
    avg_tip = tips.groupby(["day", "sex"])["tip"].mean()
    print("2. Average tip per day and sex:\n", avg_tip, "\n")

    tips_copy = tips.copy()
    tips_copy["procent_bacsis"] = tips_copy["tip"] / tips_copy["total_bill"] * 100

    top5 = tips_copy.nlargest(5, "procent_bacsis")
    print("3-4. Top 5 meals by procent_bacsis:\n", top5, "\n")

    counts = tips.groupby(["day", "smoker"]).size()
    print("5. Counts per day and smoker:\n", counts, "\n")


if __name__ == "__main__":
    main()
