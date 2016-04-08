




class PerturbationVector(object):
    def __init__(self, initial_perturbation):
        self.data = initial_perturbation
        self.epoch = 0
        self.species_list = new SpeciesList()

    def propagate(self):
        data = A.dot(data) 
        self.epoch += 1

    def check_for_newly_perturbed_species(self):
        species_index = 0
        for species in self.species_list.data:
            if species.epochs_until_perturbation < 0 and self.data[species_index] > 0:
                species.epochs_until_perturbation ==  self.epoch
            species_index += 1    
    
