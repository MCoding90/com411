import matplotlib.pyplot as plt


def read_data(file_path):
    temp_list = []
    with open("temps.txt") as file:
        for line in file:
            temp_list.append(float(line.strip()))
    return temp_list


def run():
    data = read_data('C:/Users/czerw/PycharmProjects/com411/visual/subplots/temps.txt')
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(range(len(data)), data)
    ax2.bar(range(len(data)), data)
    plt.show()

run()
