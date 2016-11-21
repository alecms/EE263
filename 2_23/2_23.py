import matrix_a
import matplotlib.pyplot as plt
import numpy as np
# while(True):




class PerturbationVector(object):
    def __init__(self, initial_perturbation):
        self.data = initial_perturbation
        self.epoch = 0
        self.species_list = SpeciesList()
        self.record_species_history()

    def propagate(self):
        self.data = matrix_a.A.dot(self.data) 
        self.epoch += 1
        self.record_species_history()

    def record_species_history(self):
        for species_index, species in enumerate(self.species_list.data):
            species.history.append(self.data[species_index])

    def check_for_newly_perturbed_species(self):
        species_index = 0
        for species in self.species_list.data:
            if species.epochs_until_perturbation < 0 and abs(self.data[species_index]) > 0:
                species.epochs_until_perturbation =  self.epoch
            species_index += 1    
    
    def check_for_unperturbed_species(self):
        for species in self.species_list.data:
            if species.epochs_until_perturbation < 0:
                return True
        return False

class SpeciesList(object):

    SPECIES_NAMES = ['bear', 'cougar', 'deer', 
            'rabbit', 'mouse', 'raccoon', 'frog', 
            'worm', 'robin', 'eagle']


    def __init__(self):
        self.data = []
        species_index = 0
        for species_name in self.SPECIES_NAMES:
            self.data.append(Species(species_name))
            species_index += 1

class Species(object):

    def __init__(self, species_name):

        self.name = species_name
        self.epochs_until_perturbation = -1
        self.history = []





def run_simulation(initial_perturbation, epochs_to_simulate):

    perturbation = PerturbationVector(initial_perturbation)

    all_species_perturbed_flag = False

    while(True):
        perturbation.check_for_newly_perturbed_species()
        
        if not(perturbation.check_for_unperturbed_species()):
            if not all_species_perturbed_flag:
                # print ("At epoch {0} there are no more unperturbed " 
                #     "species.\n".format(perturbation.epoch))
                all_species_perturbed_flag = True

        perturbation.propagate()

        if perturbation.epoch > epochs_to_simulate:
            break
    
    return perturbation

initial_perturbation = [0] * len(SpeciesList.SPECIES_NAMES)
initial_perturbation[3] = 1
perturbation = run_simulation(initial_perturbation, 10)

s = []
for species in perturbation.species_list.data:
    s.append(species.epochs_until_perturbation)

print("a) Vector showing how long it takes each species to be perturbed: s ="
        " {0}\n".format(s))

def find_optimal_ic(species_to_maximize, epoch):

    Apow = np.linalg.matrix_power(matrix_a.A, epoch)
    a = Apow[species_to_maximize,:]
    x = []
    for element in a:
        if element < 0:
            x.append(-1.0)
        else:
            x.append(1.0)

    return x

x = find_optimal_ic(0, 10)
perturbation = run_simulation(x, 40)

print("b) Initial perturbation satisfying |xi(0)| < 1 for each x,"
        " which maximizes population of species 1 at t "
        "= 10: x(0) = {0}\n"
        "Population of species 1 at t = 10: x1(10) = {1}"
        .format(x, perturbation.species_list.data[0].history[10]))


plt.close("all")

species = perturbation.species_list.data[0]
plt.plot(species.history, label = species.name)
plt.legend()
plt.title('Pop. Perturbation vs. Epoch')
plt.xlabel('Epoch')
plt.ylabel('Perturbation (Thousands)')
plt.show()

"""
number_of_species = len(perturbation.species_list.data)

for species_index in range(0, round(number_of_species / 2)):
    species = perturbation.species_list.data[species_index]
    plt.plot(species.history, label = species.name)

plt.legend()
plt.title('Pop. Perturbation vs. Epoch')
plt.xlabel('Epoch')
plt.ylabel('Perturbation (Thousands)')
plt.show()

plt.figure()
for species_index in range(round(number_of_species / 2), number_of_species):
    species = perturbation.species_list.data[species_index]
    plt.plot(species.history, label = species.name)

plt.legend()
plt.title('Pop. Perturbation vs. Epoch')
plt.xlabel('Epoch')
plt.ylabel('Perturbation (Thousands)')
plt.show()
"""
