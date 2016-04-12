import matrix_a

# while(True):




class PerturbationVector(object):
    def __init__(self, initial_perturbation):
        self.data = initial_perturbation
        self.epoch = 0
        self.species_list = SpeciesList()

    def propagate(self):
        self.data = matrix_a.A.dot(self.data) 
        self.epoch += 1

    def check_for_newly_perturbed_species(self):
        species_index = 0
        for species in self.species_list.data:
            if species.epochs_until_perturbation < 0 and self.data[species_index] > 0:
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



max_epochs_to_simulate = 3

initial_perturbation = [0] * len(SpeciesList.SPECIES_NAMES)
initial_perturbation[7] = 1

perturbation = PerturbationVector(initial_perturbation)

max_epochs_to_simulate = 10

while(True):
    perturbation.check_for_newly_perturbed_species()
    
    if not(perturbation.check_for_unperturbed_species()):
        print ("At epoch {0} there are no more unperturbed " 
                "species").format(perturbation.epoch)
        break

    perturbation.propagate()

    if perturbation.epoch > max_epochs_to_simulate:
        print ("Simulated {0} epochs but there are "
                "still some unperturbed " 
                "species.").format(perturbation.epoch - 1)
        break

for species in perturbation.species_list.data:

    print species.name
    print species.epochs_until_perturbation



