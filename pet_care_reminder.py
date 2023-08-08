import datetime

class Pet:
    def __init__(self, name, feeding_interval, pill_day):
        self.name = name
        self.feeding_interval = feeding_interval
        self.pill_day = pill_day
        self.last_fed = datetime.datetime.now()
        self.last_pill_given = None

    def feed(self):
        self.last_fed = datetime.datetime.now()

    def give_pill(self):
        self.last_pill_given = datetime.datetime.now()

    def time_since_last_fed(self):
        return datetime.datetime.now() - self.last_fed

    def days_since_last_pill(self):
        if self.last_pill_given:
            return (datetime.datetime.now() - self.last_pill_given).days
        return None

    def is_hungry(self):
        return self.time_since_last_fed() > self.feeding_interval

    def needs_pill(self):
        if not self.last_pill_given:
            return True
        return datetime.datetime.now().day == self.pill_day and self.days_since_last_pill() >= 30

def main():
    # Create pets with their names, feeding intervals, and pill days
    dez = Pet("Dez", datetime.timedelta(hours=6), 10)
    romo = Pet("Romo", datetime.timedelta(hours=5), 15)
    cooper = Pet("Cooper", datetime.timedelta(hours=8), 20)

    pets = [dez, romo, cooper]

    while True:
        print("\nPet Care Reminder System")
        print("-------------------------")
        for index, pet in enumerate(pets, 1):
            status = "Hungry" if pet.is_hungry() else "Not Hungry"
            pill_status = "Needs pill" if pet.needs_pill() else "Pill given"
            print(f"{index}. {pet.name} - Last fed: {pet.last_fed.strftime('%Y-%m-%d %H:%M:%S')} - Status: {status} - Pill Status: {pill_status}")

        print("\nOptions:")
        print("1. Feed a pet")
        print("2. Give pill to a pet")
        print("3. Quit")

        choice = input("\nChoose an option: ")

        if choice == '3':
            break
        elif choice == '1':
            pet_choice = input("Enter the number of the pet you want to feed: ")
            try:
                selected_pet = pets[int(pet_choice) - 1]
                selected_pet.feed()
                print(f"\n{selected_pet.name} has been fed!")
            except (ValueError, IndexError):
                print("\nInvalid choice. Please select a valid pet number.")
        elif choice == '2':
            pet_choice = input("Enter the number of the pet you want to give a pill: ")
            try:
                selected_pet = pets[int(pet_choice) - 1]
                selected_pet.give_pill()
                print(f"\nPill given to {selected_pet.name}!")
            except (ValueError, IndexError):
                print("\nInvalid choice. Please select a valid pet number.")
        else:
            print("\nInvalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
