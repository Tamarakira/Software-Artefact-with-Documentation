import matplotlib.pyplot as plt

def plot_reviews_distribution(data):
    data['Branch'].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title('Review Distribution by Park')
    plt.show()
