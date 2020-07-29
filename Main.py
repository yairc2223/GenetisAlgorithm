import random
from tkinter import *
from tkinter import messagebox

import matplotlib.pyplot as plt
import numpy as np

from Cell import *
from Map import *

popsize = 100
# neighbors matrix
r, c = 12, 12
Matrix = [[0 for x in range(r)] for y in range(c)]
# fill neighbors
Matrix[0] = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
Matrix[1] = [1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0]
Matrix[2] = [0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0]
Matrix[3] = [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
Matrix[4] = [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0]
Matrix[5] = [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1]
Matrix[6] = [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
Matrix[7] = [0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0]
Matrix[8] = [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1]
Matrix[9] = [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1]
Matrix[10] = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1]
Matrix[11] = [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0]

maptodraw = 8


def run1():
    global p
    global pop
    global g
    global window
    try:
        gen_size = int(pop.get())
        prob = float(p.get())
        crossover_frequency = int(g.get())
        avg_file_str = "avg {0}; {1}, {2}.txt".format(gen_size, prob, crossover_frequency)
        best_file_str = "best {0}; {1}, {2}.txt".format(gen_size, prob, crossover_frequency)

        file_avg_graph = "avg {0}; {1}, {2}.png".format(gen_size, prob, crossover_frequency)
        file_best_graph = "best {0}; {1}, {2}.png".format(gen_size, prob, crossover_frequency)

        avg_output = open(avg_file_str, "w")
        best_output = open(best_file_str, "w")

        count = 0
        # create a generation of gen_size maps
        init_population = initialize_generation(gen_size)
        # perform fitness check and crossover every "crossover_frequency" iterations
        mutated_gen = mutate(init_population, prob)
        t = 8
        while t > 0:
            mutated_gen = mutate(mutated_gen, prob)
            if count % crossover_frequency == 0:
                init_gen = mutated_gen
                crossed_gen = crossover(mutated_gen)
                fit_sum, fit_avg = calculate_fitness(mutated_gen)
                export_results(avg_output, best_output, count, fit_sum, fit_avg, t)
            # crossed_gen = crossover(mutated_gen)
            mutated_gen = crossed_gen
            mutated_gen.sort(key=lambda x: x.fitness_score)
            crossed_gen.sort(key=lambda x: x.fitness_score)
            count += 1
            maptodraw = mutated_gen[0]

            t = mutated_gen[0].fitness_score

        export_results(avg_output, best_output, count, fit_sum, fit_avg, t)
        calculate_fitness(mutated_gen)
        mutated_gen.sort(key=lambda x: x.fitness_score)
        printMap(mutated_gen[0].formation)
        labelgenval = Label(window, text=str(count), bg="LightSkyBlue1", fg="blue", font=("arial", 14, "bold"))
        labelgenval.place(x=365, y=360)
        avg_output.close()
        best_output.close()
        graphCreator(avg_file_str, best_file_str, file_avg_graph, file_best_graph)

    except:
        messagebox.showerror("error", "Fill the Input correctly !")


def export_results(avg_file, best_file, generations, f_sum, f_avg, f_best):
    out_str = ""
    out_str += "{0},{1}\n".format(generations, f_avg)
    avg_file.write(out_str)

    out_str = ""
    out_str += "{0},{1}\n".format(generations, f_best)
    best_file.write(out_str)


def graphCreator(avg_str, best_str, avg_graph, best_graph):
    x1, y1 = np.loadtxt(best_str, delimiter=',', unpack=True)
    x2, y2 = np.loadtxt(avg_str, delimiter=',', unpack=True)

    plt.subplot(2, 1, 1)
    plt.plot(x1, y1)
    plt.savefig(best_graph, bbox_inches="tight", padinches=2, transperent=True)
    plt.title("Best Fitness Score Vs Generation")
    plt.ylabel("Best Fitness")

    plt.subplot(2, 1, 2)
    plt.plot(x2, y2)
    plt.savefig(avg_graph, bbox_inches="tight", padinches=2, transperent=True)
    plt.xlabel("Generations")
    plt.title("Average Fitness Score Vs Generation")
    plt.ylabel("Average Fitness")

    plt.subplots_adjust(None, None, None, None, None, 0.5)
    plt.show()


def initialize_generation(size):
    maps_list = []

    # populate maps list
    for i in range(0, size):
        cells_list = []

        # populate cells list according to given map
        """
        for j in range(1, 13):
            cells_list[j] = Cell(j, random.randint(1, 4))
        """

        cell_1 = Cell(1, random.randint(1, 4))
        cell_2 = Cell(2, random.randint(1, 4))
        cell_3 = Cell(3, random.randint(1, 4))
        cell_4 = Cell(4, random.randint(1, 4))
        cell_5 = Cell(5, random.randint(1, 4))
        cell_6 = Cell(6, random.randint(1, 4))
        cell_7 = Cell(7, random.randint(1, 4))
        cell_8 = Cell(8, random.randint(1, 4))
        cell_9 = Cell(9, random.randint(1, 4))
        cell_10 = Cell(10, random.randint(1, 4))
        cell_11 = Cell(11, random.randint(1, 4))
        cell_12 = Cell(12, random.randint(1, 4))

        cells_list.append(cell_1)
        cells_list.append(cell_2)
        cells_list.append(cell_3)
        cells_list.append(cell_4)
        cells_list.append(cell_5)
        cells_list.append(cell_6)
        cells_list.append(cell_7)
        cells_list.append(cell_8)
        cells_list.append(cell_9)
        cells_list.append(cell_10)
        cells_list.append(cell_11)
        cells_list.append(cell_12)

        # create a single map
        m = Map(cells_list, 100)
        m.set_fit(fit_check(m))
        maps_list.append(m)
    return maps_list


def mutate(gen, p):
    # randomize a cell index to mutate (change color) in each map
    # rand_index = random.randint(0, 11)
    # for each map, mutate the specific cell
    for map_obj in gen:
        rand_index = random.randint(0, 11)
        cell_to_mutate = map_obj.formation[rand_index]
        # calculate probability of mutation
        temp = random.randint(1, 1000)
        if temp <= (p * 1000):
            # change color of the cell
            new_color = random.randint(1, 4)
            while new_color == cell_to_mutate.color:
                new_color = random.randint(1, 4)
            cell_to_mutate.set_color(new_color)
    return gen


def fit_check(map):
    global Matrix
    count = 0
    for cell in map.formation:
        for i in range(0, 11):
            if Matrix[cell.index - 1][i] == 1:
                if cell.color == map.formation[i].color:
                    count += 1
    return count


def calculate_fitness(gen):
    fit_sum = 0
    for each_map in gen:
        # traverse graph and count same colored neighbors
        counter = fit_check(each_map)
        # print("custom: ", counter)
        each_map.fitness_score = counter
        fit_sum += counter
    fit_avg = fit_sum / len(gen)
    return fit_sum, fit_avg


def crossover(gen):
    # sort the generation by fitness score of each map, in descending order
    gen.sort(key=lambda x: x.fitness_score)
    # crossover 2 highest-fit maps with given indexes

    indexes1 = [0, 1, 2, 3, 4, 5]
    indexes2 = [6, 7, 8, 9, 10, 11]
    first = [gen[0].formation[x] for x in indexes1]
    second = [gen[1].formation[x] for x in indexes2]
    new_formation = first + second

    third = [gen[2].formation[x] for x in indexes1]
    fourth = [gen[3].formation[x] for x in indexes2]
    new_formation2 = third + fourth

    # crossover logic: first parent dies and replaced by its child
    gen[0].formation = new_formation
    gen[2].formation = new_formation2

    return gen


def index2color(index):
    if index == 1:
        return "black"
    if index == 2:
        return "blue"
    if index == 3:
        return "green"
    if index == 4:
        return "red"


def printMap2():
    # polygon11:
    canvas.create_polygon(50, 50, 250, 50, 250, 80, 80, 80, 80, 300, 200, 300, 200, 330, 50, 330, 50, 50,
                          fill=index2color(maptodraw[10].color), outline="white")
    # polygon1:
    canvas.create_polygon(80, 80, 220, 80, 220, 120, 80, 120, fill=index2color(maptodraw[0].color), outline="white")
    # polygon2:
    canvas.create_polygon(80, 120, 220, 120, 220, 215, 185, 215, 185, 150, 80, 150,
                          fill=index2color(maptodraw[1].color), outline="white")
    # polygon3:
    canvas.create_polygon(80, 150, 185, 150, 185, 270, 155, 270, 155, 245, 110, 245, 110, 235, 80, 235,
                          fill=index2color(maptodraw[2].color), outline="white")
    # polygon5:
    canvas.create_polygon(135, 270, 205, 270, 205, 300, 135, 300, fill=index2color(maptodraw[4].color), outline="white")
    # polygon4:
    canvas.create_polygon(80, 235, 110, 235, 110, 245, 155, 245, 155, 270, 135, 270, 135, 300, 80, 300,
                          fill=index2color(maptodraw[3].color), outline="white")
    # polygon12:
    canvas.create_polygon(200, 300, 200, 330, 500, 330, 500, 50, 250, 50, 250, 80, 450, 80, 450, 300,
                          fill=index2color(maptodraw[11].color), outline="white")
    # polygon6:
    canvas.create_polygon(220, 80, 450, 80, 450, 160, 340, 160, 340, 120, 220, 120,
                          fill=index2color(maptodraw[5].color),
                          outline="white")
    # polygon7:
    canvas.create_polygon(220, 120, 340, 120, 340, 180, 220, 180, fill=index2color(maptodraw[6].color), outline="white")
    # polygon8:
    canvas.create_polygon(220, 180, 340, 180, 340, 160, 360, 160, 360, 280, 320, 280, 320, 265, 300, 265, 300, 215, 220,
                          215, fill=index2color(maptodraw[7].color), outline="white")
    # polygon10:
    canvas.create_polygon(360, 280, 360, 160, 450, 160, 450, 300, 320, 300, 320, 280,
                          fill=index2color(maptodraw[9].color),
                          outline="white")
    # polygon9:
    canvas.create_polygon(320, 300, 320, 265, 300, 265, 300, 215, 185, 215, 185, 270, 205, 270, 205, 300, 265, 300,
                          fill=index2color(maptodraw[8].color), outline="white")
    canvas.pack()


def printMap(map):
    # polygon11:
    canvas.create_polygon(50, 50, 250, 50, 250, 80, 80, 80, 80, 300, 200, 300, 200, 330, 50, 330, 50, 50,
                          fill=index2color(map[10].color), outline="white")
    # polygon1:
    canvas.create_polygon(80, 80, 220, 80, 220, 120, 80, 120, fill=index2color(map[0].color), outline="white")
    # polygon2:
    canvas.create_polygon(80, 120, 220, 120, 220, 215, 185, 215, 185, 150, 80, 150,
                          fill=index2color(map[1].color), outline="white")
    # polygon3:
    canvas.create_polygon(80, 150, 185, 150, 185, 270, 155, 270, 155, 245, 110, 245, 110, 235, 80, 235,
                          fill=index2color(map[2].color), outline="white")
    # polygon5:
    canvas.create_polygon(135, 270, 205, 270, 205, 300, 135, 300, fill=index2color(map[4].color), outline="white")
    # polygon4:
    canvas.create_polygon(80, 235, 110, 235, 110, 245, 155, 245, 155, 270, 135, 270, 135, 300, 80, 300,
                          fill=index2color(map[3].color), outline="white")
    # polygon12:
    canvas.create_polygon(200, 300, 200, 330, 500, 330, 500, 50, 250, 50, 250, 80, 450, 80, 450, 300,
                          fill=index2color(map[11].color), outline="white")
    # polygon6:
    canvas.create_polygon(220, 80, 450, 80, 450, 160, 340, 160, 340, 120, 220, 120, fill=index2color(map[5].color),
                          outline="white")
    # polygon7:
    canvas.create_polygon(220, 120, 340, 120, 340, 180, 220, 180, fill=index2color(map[6].color), outline="white")
    # polygon8:
    canvas.create_polygon(220, 180, 340, 180, 340, 160, 360, 160, 360, 280, 320, 280, 320, 265, 300, 265, 300, 215, 220,
                          215, fill=index2color(map[7].color), outline="white")
    # polygon10:
    canvas.create_polygon(360, 280, 360, 160, 450, 160, 450, 300, 320, 300, 320, 280, fill=index2color(map[9].color),
                          outline="white")
    # polygon9:
    canvas.create_polygon(320, 300, 320, 265, 300, 265, 300, 215, 185, 215, 185, 270, 205, 270, 205, 300, 265, 300,
                          fill=index2color(map[8].color), outline="white")
    canvas.pack()


def printInitMap():
    # polygon11:
    canvas.create_polygon(50, 50, 250, 50, 250, 80, 80, 80, 80, 300, 200, 300, 200, 330, 50, 330, 50, 50,
                          fill="white", outline="black")
    # polygon1:
    canvas.create_polygon(80, 80, 220, 80, 220, 120, 80, 120, fill="white", outline="black")
    # polygon2:
    canvas.create_polygon(80, 120, 220, 120, 220, 215, 185, 215, 185, 150, 80, 150,
                          fill="white", outline="black")
    # polygon3:
    canvas.create_polygon(80, 150, 185, 150, 185, 270, 155, 270, 155, 245, 110, 245, 110, 235, 80, 235,
                          fill="white", outline="black")
    # polygon5:
    canvas.create_polygon(135, 270, 205, 270, 205, 300, 135, 300, fill="white", outline="black")
    # polygon4:
    canvas.create_polygon(80, 235, 110, 235, 110, 245, 155, 245, 155, 270, 135, 270, 135, 300, 80, 300,
                          fill="white", outline="black")
    # polygon12:
    canvas.create_polygon(200, 300, 200, 330, 500, 330, 500, 50, 250, 50, 250, 80, 450, 80, 450, 300,
                          fill="white", outline="black")
    # polygon6:
    canvas.create_polygon(220, 80, 450, 80, 450, 160, 340, 160, 340, 120, 220, 120, fill="white",
                          outline="black")
    # polygon7:
    canvas.create_polygon(220, 120, 340, 120, 340, 180, 220, 180, fill="white", outline="black")
    # polygon8:
    canvas.create_polygon(220, 180, 340, 180, 340, 160, 360, 160, 360, 280, 320, 280, 320, 265, 300, 265, 300, 215, 220,
                          215, fill="white", outline="black")
    # polygon10:
    canvas.create_polygon(360, 280, 360, 160, 450, 160, 450, 300, 320, 300, 320, 280, fill="white",
                          outline="black")
    # polygon9:
    canvas.create_polygon(320, 300, 320, 265, 300, 265, 300, 215, 185, 215, 185, 270, 205, 270, 205, 300, 265, 300,
                          fill="white", outline="black")
    canvas.pack()


window = Tk()
window.geometry("580x600")
window.title("Welcome To Our ColorGene Model")
window.configure(bg="LightSkyBlue1")
canvas = Canvas(window, width=580, height=400, highlightthickness=0, bg="LightSkyBlue1", bd=0, relief="ridge")

buttonstart = Button(window, text="Start", bg="SlateBlue1", fg="white", font=("arial", 14, "bold"), command=run1)
labelfitnees = Label(window, text="Generations Count:", bg="LightSkyBlue1", fg="blue",
                     font=("arial", 14, "bold")).place(x=180, y=360)
buttonstart.place(x=240, y=550)
printInitMap()
pop = Entry(window, width=10, borderwidth=4)
pop.place(x=350, y=420)
labepop = Label(window, text="Enter the size of Population:", bg="LightSkyBlue1", font=("arial", 12, "bold")).place(
    x=110, y=420)
p = Entry(window, width=10, borderwidth=4)
p.place(x=350, y=450)
labep = Label(window, text="Enter probability of Mutation:", bg="LightSkyBlue1", font=("arial", 12, "bold")).place(
    x=110, y=450)
g = Entry(window, width=10, borderwidth=4)
g.place(x=350, y=480)
labep = Label(window, text="Enter fruquency of Crossover:", bg="LightSkyBlue1", font=("arial", 12, "bold")).place(x=110,
                                                                                                                  y=480)

window.mainloop()
