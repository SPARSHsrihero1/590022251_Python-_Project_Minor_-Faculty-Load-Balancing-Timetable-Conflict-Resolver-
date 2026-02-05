VALID_DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
MAX_LOAD = 18
faculty_data = {}
# ---------- Helper ----------
def expand_day_input(day_input):
    day_input = day_input.strip()

    if day_input.lower() == "all":
        return VALID_DAYS.copy()
    if "-" in day_input:
        start, end = day_input.split("-")
        start = start.strip()
        end = end.strip()
        if start in VALID_DAYS and end in VALID_DAYS:
            return VALID_DAYS[
                VALID_DAYS.index(start): VALID_DAYS.index(end) + 1
            ]

    if day_input in VALID_DAYS:
        return [day_input]
    return None


# ---------- Core Features ----------

def add_faculty():
    name = input("\nEnter faculty name: ").strip()

    if name in faculty_data:
        print("Faculty already exists.")
        return

    day_input = input(
        "Enter teaching days (Mon / Mon-Fri / Mon-Sat / All): "
    )
    days = expand_day_input(day_input)

    if not days:
        print("Invalid day input.")
        return

    faculty_data[name] = {}

    for day in days:
        hours = int(input(f"Enter teaching hours on {day}: "))
        faculty_data[name][day] = hours

    print("\nFaculty data added successfully.")


def update_faculty():
    name = input("\nEnter faculty name to update: ").strip()

    if name not in faculty_data:
        print("Faculty not found.")
        return

    while True:
        print("\n--- UPDATE MENU ---")
        print("1. Update all existing days")
        print("2. Update a specific existing day")
        print("3. Add new day(s)")
        print("4. Go back")

        choice = input("Choose update option: ")

        if choice == "1":
            for day in faculty_data[name]:
                new_hours = int(
                    input(f"Enter new teaching hours for {day}: ")
                )
                faculty_data[name][day] = new_hours
            print("All days updated successfully.")

        elif choice == "2":
            day = input("Enter day to update (Mon/Tue/...): ")

            if day not in faculty_data[name]:
                print("This day does not exist.")
                continue

            new_hours = int(
                input(f"Enter new teaching hours for {day}: ")
            )
            faculty_data[name][day] = new_hours
            print(f"{day} updated successfully.")

        elif choice == "3":
            day_input = input(
                "Enter new day(s) to add (Mon / Mon-Fri / Mon-Sat): "
            )
            days = expand_day_input(day_input)

            if not days:
                print("Invalid day input.")
                continue

            for day in days:
                if day in faculty_data[name]:
                    print(f"{day} already exists. Skipping.")
                else:
                    hours = int(
                        input(f"Enter teaching hours for {day}: ")
                    )
                    faculty_data[name][day] = hours
                    print(f"{day} added successfully.")

        elif choice == "4":
            break

        else:
            print("Invalid option.")


def view_faculty():
    if not faculty_data:
        print("\nNo data available.")
        return

    for faculty, days in faculty_data.items():
        print(f"\nFaculty: {faculty}")
        for day, hours in days.items():
            print(f"  {day}: {hours} hours")


def calculate_workload():
    print("\nFaculty Workload:")
    workload = {}

    for faculty, days in faculty_data.items():
        total = sum(days.values())
        workload[faculty] = total
        print(f"{faculty}: {total} hours/week")

    return workload


def suggest_load_balance(workload):
    print("\nLoad Balancing Suggestions:")

    overloaded = {f: h for f, h in workload.items() if h > MAX_LOAD}
    underloaded = {f: h for f, h in workload.items() if h < MAX_LOAD}

    if not overloaded:
        print("No faculty is overloaded.")
        return

    suggestion_no = 1

    for ofac, ohours in overloaded.items():
        extra = ohours - MAX_LOAD

        # Suggestion 1: Shift load
        for ufac, uhours in underloaded.items():
            print(
                f"{suggestion_no}. Shift {extra} hour(s) "
                f"from {ofac} to {ufac}."
            )
            suggestion_no += 1
            break

        # Suggestion 2: Redistribute schedule
        print(
            f"{suggestion_no}. Redistribute {ofac}'s classes "
            f"across fewer days to reduce daily workload."
        )
        suggestion_no += 1

        # Suggestion 3: Guest/Adjunct faculty
        print(
            f"{suggestion_no}. Assign some sessions of {ofac} "
            f"to guest or visiting faculty."
        )

        return


def generate_report():
    with open("report.txt", "w") as f:
        f.write("FACULTY LOAD BALANCING REPORT\n")
        f.write("=" * 35 + "\n\n")

        for faculty, days in faculty_data.items():
            total = sum(days.values())
            f.write(f"Faculty: {faculty}\n")
            f.write(f"Total Load: {total} hours/week\n")
            for day, hours in days.items():
                f.write(f"{day}: {hours} hours\n")
            f.write("\n")
    print("\nReport generated successfully (report.txt).")

# ---------- Menu ----------

def menu():
    while True:
        print("\n====== MENU ======")
        print("1. Add Faculty Data")
        print("2. Update Faculty Data")
        print("3. View Faculty Details")
        print("4. Calculate Faculty Workload")
        print("5. Suggest Load Balancing")
        print("6. Generate Report")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_faculty()
        elif choice == "2":
            update_faculty()
        elif choice == "3":
            view_faculty()
        elif choice == "4":
            calculate_workload()
        elif choice == "5":
            workload = calculate_workload()
            suggest_load_balance(workload)
        elif choice == "6":
            generate_report()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
print("\nFaculty Load Balancing System")
menu()