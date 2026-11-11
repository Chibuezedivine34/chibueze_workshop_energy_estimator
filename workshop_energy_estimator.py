# WORKSHOP ENERGY COST ESTIMATOR
# Student: Chibueze Divine Somtochukwu
# Department: Mechatronics Engineering
# Level: ND2

student_name = "Chibueze Divine Somtochukwu"

# Preloaded workshop machine catalogue.
# These are illustrative suggested ratings; check actual machine nameplates.
machines_list = [
    {"name": "Electric Motor", "power": 1500},
    {"name": "Drilling Machine", "power": 750},
    {"name": "Lathe Machine", "power": 2000},
    {"name": "Milling Machine", "power": 3000},
    {"name": "Grinding Machine", "power": 1000},
    {"name": "Welding Machine", "power": 5000},
    {"name": "Air Compressor", "power": 2200},
    {"name": "Bench Grinder", "power": 500},
    {"name": "Hydraulic Press", "power": 4000},
    {"name": "CNC Machine", "power": 7500},
]

selected_machines = []


def calculate_energy(power_watts, hours_per_day):
    """Return daily energy consumption in kilowatt-hours."""
    return (power_watts * hours_per_day) / 1000


def calculate_cost(energy_kwh, tariff_per_kwh):
    """Return electricity cost in naira."""
    return energy_kwh * tariff_per_kwh


def classify_usage(hours_per_day):
    """Classify a machine's daily operating time."""
    if hours_per_day <= 4:
        return "Light Usage"
    elif hours_per_day <= 8:
        return "Moderate Usage"
    return "Heavy Usage"


def main():
    print("=" * 50)
    print("       WORKSHOP ENERGY COST ESTIMATOR")
    print("=" * 50)
    print("Student:", student_name)
    print("Department: Mechatronics Engineering")
    print("Level: ND2")

    print("\nAVAILABLE WORKSHOP MACHINES")
    for index, machine in enumerate(machines_list, start=1):
        print(f"{index}. {machine['name']} - {machine['power']} W")

    try:
        number = int(input("\nHow many machines do you want to calculate? "))
        if number < 1 or number > len(machines_list):
            print(f"Please enter a number from 1 to {len(machines_list)}.")
            return

        # Collect valid machine selections.
        while len(selected_machines) < number:
            choice = int(input("\nEnter machine number: "))
            if choice < 1 or choice > len(machines_list):
                print("Invalid selection. Choose a number from the list.")
                continue

            machine = machines_list[choice - 1]
            if any(item["name"] == machine["name"] for item in selected_machines):
                print("That machine has already been selected. Choose another.")
                continue

            power = machine["power"]
            print(f"\nSelected: {machine['name']}")
            print(f"Suggested power rating: {power} W")
            change = input("Change the suggested power rating? (yes/no): ").strip().lower()

            if change == "yes":
                power = float(input("Enter the actual power rating in watts: "))
            elif change != "no":
                print("Please enter yes or no.")
                continue

            if power <= 0:
                print("Power rating must be greater than zero.")
                continue

            hours = float(input("Enter daily operating hours (0-24): "))
            if hours < 0 or hours > 24:
                print("Operating hours must be between 0 and 24.")
                continue

            selected_machines.append({
                "name": machine["name"],
                "power": power,
                "hours": hours,
            })

        tariff = float(input("\nEnter electricity tariff (Naira per kWh): "))
        if tariff < 0:
            print("Tariff cannot be negative.")
            return

        total_daily_energy = 0
        total_monthly_cost = 0

        print("\n" + "=" * 50)
        print("                  ENERGY REPORT")
        print("=" * 50)

        for machine in selected_machines:
            daily_energy = calculate_energy(machine["power"], machine["hours"])
            monthly_energy = daily_energy * 30
            daily_cost = calculate_cost(daily_energy, tariff)
            monthly_cost = calculate_cost(monthly_energy, tariff)

            machine["daily_energy"] = daily_energy
            total_daily_energy += daily_energy
            total_monthly_cost += monthly_cost

            print(f"\nMachine: {machine['name']}")
            print(f"Power rating: {machine['power']:.2f} W")
            print(f"Daily energy: {daily_energy:.2f} kWh")
            print(f"Monthly energy (30 days): {monthly_energy:.2f} kWh")
            print(f"Daily cost: N{daily_cost:,.2f}")
            print(f"Monthly cost: N{monthly_cost:,.2f}")
            print(f"Usage classification: {classify_usage(machine['hours'])}")

        # Own feature: rank selected machines by daily energy use.
        print("\n" + "=" * 50)
        print("           MACHINE ENERGY RANKING")
        print("=" * 50)
        ranked_machines = sorted(
            selected_machines,
            key=lambda item: item["daily_energy"],
            reverse=True,
        )

        for position, machine in enumerate(ranked_machines, start=1):
            print(
                f"{position}. {machine['name']} - "
                f"{machine['daily_energy']:.2f} kWh/day"
            )

        print(f"\nHighest energy consumer: {ranked_machines[0]['name']}")

        total_monthly_energy = total_daily_energy * 30
        print("\n" + "=" * 50)
        print("              WORKSHOP SUMMARY")
        print("=" * 50)
        print(f"Total daily energy: {total_daily_energy:.2f} kWh")
        print(f"Total monthly energy: {total_monthly_energy:.2f} kWh")
        print(f"Estimated monthly cost: N{total_monthly_cost:,.2f}")
        print("\nThank you for using this program!")
        print("Developed by:", student_name)

    except ValueError:
        print("\nInvalid input. Please enter numbers where required.")


if __name__ == "__main__":
    main()
