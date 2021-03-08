class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    # def subscription_info(self, subscription_id):
    #     result = ''
    #     for subscription in self.subscriptions:
    #         if subscription.id == subscription_id:
    #             current_subscription = subscription
    #             result += f"{current_subscription.__repr__()}\n"
    #             customer_id = current_subscription.customer_id
    #             trainer_id = current_subscription.trainer_id
    #             exercise_id = current_subscription.exercise_id
    #             for customer in self.customers:
    #                 if customer.id == customer_id:
    #                     result += f"{customer.__repr__()}\n"
    #             for trainer in self.trainers:
    #                 if trainer.id == trainer_id:
    #                     result += f"{trainer.__repr__()}\n"
    #             for exercise in self.plans:
    #                 if exercise.id == exercise_id:
    #                     current_exercise = exercise
    #                     equipment_id = current_exercise.equipment_id
    #                     for equipment in self.equipment:
    #                         if equipment.id == equipment_id:
    #                             result += f"{equipment.__repr__()}\n"
    #                     result += f"{current_exercise.__repr__()}"
    #     return result
    def subscription_info(self, subscription_id):
        subscription = [subscription for subscription in self.subscriptions if subscription.id == subscription_id][0]
        customer = [customer for customer in self.customers if customer.id == subscription.customer_id][0]
        trainer = [trainer for trainer in self.trainers if trainer.id == subscription.trainer_id][0]
        exercise_plan = \
        [exercise_plan for exercise_plan in self.plans if exercise_plan.trainer_id == subscription.trainer_id][0]
        equipment = [equipment for equipment in self.equipment if equipment.id == exercise_plan.equipment_id][0]
        return f'{subscription.__repr__()}\n{customer.__repr__()}\n{trainer.__repr__()}\n{equipment.__repr__()}\n{exercise_plan.__repr__()}'
        return result