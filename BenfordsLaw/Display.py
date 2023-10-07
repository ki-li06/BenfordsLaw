from matplotlib import pyplot as plt

def plot_dataframe(df):
    fig, ax = plt.subplots()
    ax.bar(df.index, df['actual'], label='Actual')
    ax.plot(df.index, df['expected'], label='Expected', color='red')
    ax.set_xlabel('Leading Digit')
    ax.set_ylabel('Frequency')
    ax.set_title('Benford\'s Law')
    ax.legend()
    plt.show()

print("Display.py loaded")
