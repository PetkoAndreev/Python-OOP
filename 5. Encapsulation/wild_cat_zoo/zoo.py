class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def is_enough_animal_capacity(self):
        return len(self.animals) < self.__animal_capacity

    def is_enough_budget(self, price):
        return price <= self.__budget

    def is_enough_worker_space(self):
        return len(self.workers) < self.__workers_capacity

    def add_animal(self, animal, price):
        '''
                    -	If you have enough budget and capacity add the animal (instance of Lion/Tiger/Cheetah) to the animals list,
                        reduce the budget and return "{name} the {type of animal (Lion/Tiger/Cheetah)} added to the zoo"
                    -	If you have capacity, but no budget, return "Not enough budget"
                    -	In any other case, you don't have space and you should return "Not enough space for animal"
                    '''
        if not self.is_enough_animal_capacity() and self.is_enough_budget(price):
            return "Not enough space for animal"
        elif not self.is_enough_budget(price):
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        '''
        -	If you have enough space for the worker (instance of Keeper/Caretaker/Vet), add him to the workers and
            return "{name} the {type(Keeper/Vet/Caretaker)} hired successfully"
        -	Otherwise return "Not enough space for worker"
        '''
        if not self.is_enough_worker_space():
            return "Not enough space for worker"
        self.workers.append(worker)
        # self.__budget -= worker.salary
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        '''
        -	If there is a worker with that name in the workers list, remove him and return "{worker_name} fired successfully"
        -	Otherwise return "There is no {worker_name} in the zoo"
        '''
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        '''
        -	If you have enough budget to pay the workers (sum their salaries) pay them and return "You payed your workers.
            They are happy. Budget left: {left_budget}"
        -	Otherwise return "You have no budget to pay your workers. They are unhappy"
        '''
        sum_salaries = 0
        for worker in self.workers:
            sum_salaries += worker.salary
        if not self.is_enough_budget(sum_salaries):
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= sum_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        '''
        -	If you have enough budget to tend the animals reduce the budget and return "You tended all the animals.
            They are happy. Budget left: {left_budget}"
        -	Otherwise return "You have no budget to tend the animals. They are unhappy."
        '''
        sum_needs = 0
        for animal in self.animals:
            sum_needs += animal.get_needs()
        if not self.is_enough_budget(sum_needs):
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= sum_needs
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        # -	Increase the budget with the given amount of profit
        self.__budget += amount

    def animals_status(self):
        '''
        -	Returns the following string:
        You have {total_animals_count} animals
        ----- {amount_of_lions} Lions:
        {lion1}
        …
        ----- {amount_of_tigers} Tigers:
        {tiger1}
        …
        ----- {amount_of_cheetahs} Cheetahs:
        {cheetah1}
        …
        -	Hint: use the __repr__ methods of the animals to print them on the console
        '''
        total_animals_count = len(self.animals)
        lions = [lion.__repr__() for lion in self.animals if lion.__class__.__name__ == 'Lion']
        tigers = [tiger.__repr__() for tiger in self.animals if tiger.__class__.__name__ == 'Tiger']
        cheetahs = [cheetah.__repr__() for cheetah in self.animals if cheetah.__class__.__name__ == 'Cheetah']
        amount_of_lions = len(lions)
        amount_of_tigers = len(tigers)
        amount_of_cheetahs = len(cheetahs)
        animals_status = f"You have {total_animals_count} animals\n"
        animals_status += f"----- {amount_of_lions} Lions:\n"
        if lions:
            for lion in lions:
                animals_status += f"{lion}\n"
        animals_status += f"----- {amount_of_tigers} Tigers:\n"
        if tigers:
            for tiger in tigers:
                animals_status += f"{tiger}\n"
        animals_status += f"----- {amount_of_cheetahs} Cheetahs:\n"
        if cheetahs:
            for cheetah in cheetahs:
                if cheetahs.index(cheetah) == len(cheetahs) - 1:
                    animals_status += f"{cheetah}"
                else:
                    animals_status += f"{cheetah}\n"
        return animals_status

    def workers_status(self):
        '''
        -	Returns the following string:
        You have {total_workers_count} workers
        ----- {amount_of_keepers} Keepers:
        {keeper1}
        …
        ----- {amount_of_caretakers} Caretakers:
        {caretaker1}
        …
        ----- {amount_of_vetes} Vets:
        {vet1}
        …
        -	Hint: use the __repr__ methods of the workers to print them on the console
        '''
        total_workers_count = len(self.workers)
        keepers = [keeper.__repr__() for keeper in self.workers if keeper.__class__.__name__ == 'Keeper']
        caretakers = [caretaker.__repr__() for caretaker in self.workers if caretaker.__class__.__name__ == 'Caretaker']
        vets = [vet.__repr__() for vet in self.workers if vet.__class__.__name__ == 'Vet']
        amount_of_keepers = len(keepers)
        amount_of_caretakers = len(caretakers)
        amount_of_vetes = len(vets)
        workers_status = f"You have {total_workers_count} workers\n"
        workers_status += f"----- {amount_of_keepers} Keepers:\n"
        if keepers:
            for keeper in keepers:
                workers_status += f"{keeper}\n"
        workers_status += f"----- {amount_of_caretakers} Caretakers:\n"
        if caretakers:
            for caretaker in caretakers:
                workers_status += f"{caretaker}\n"
        workers_status += f"----- {amount_of_vetes} Vets:\n"
        if vets:
            for vet in vets:
                if vets.index(vet) == len(vets) - 1:
                    workers_status += f"{vet}"
                else:
                    workers_status += f"{vet}\n"
        return workers_status
