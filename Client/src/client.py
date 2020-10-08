from argparse import ArgumentParser

from models.part import Part
from dao import part_request


if __name__ == "__main__":
    
    parser = ArgumentParser()

    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=None)

    args = parser.parse_args()

    if not args.port:
        url = f"http://{args.host}/api/part"
    else:
        url = f"http://{args.host}:{args.port}/api/part"

    while True:

        print("1. Add Part")
        print("2. Get Part")
        print("3. List Parts")
        print("4. Exit")
        print()

        while True:
            try:
                choice = int(input("Choice: "))
                if choice < 1 or choice > 4:
                    continue
            except ValueError:
                continue
            break

        print()

        if choice == 1:

            name = input("Name: ")
            description = input("Description: ")
            components = []

            component_count = 0
            while True:
                choice_part = input(f"Add a {'another' if component_count else ''} component? [Y/n]: ").lower()

                if choice_part:
                    if choice_part == "n":
                        break
                    if choice_part != "y" and choice_part != "n":
                        continue

                component_name = input("Name: ")
                component_description = input("Description: ")
                

                while True:
                    try:
                        component_ammount = int(input("Ammount: "))
                        if choice < 0:
                            continue
                    except ValueError:
                        continue
                    break

                components.append((Part(component_name, component_description, []), component_ammount))

                component_count += 1

            part = Part(name, description, [component for component in components])

            part_request.create_part(part, url)

        elif choice == 2:
            
            while True:
                try:
                    part_id = int(input("Part ID: "))
                    if part_id < 0:
                        continue
                except ValueError:
                    continue
                break
                
            response = part_request.get_part(part_id, url)

            if not response:
                print("Part not found")
                continue

            part = Part.from_dict(response)

            print("Name:", part.name)
            print("Description:", part.description)
            print("Components:")
            for component in part.components:
                print("\tUnique ID:", component["unique_id"])
                print("\tAmmount:", component["ammount"])
                print()

        elif choice == 3:
            results = part_request.list_parts(url)

            if not results:
                print("The repository is empty!")
                continue

            for result in results:

                part = Part.from_dict(result)

                print("Name:", part.name)
                print("Description:", part.description)
                print("Components:")
                for component in part.components:
                    print("\tUnique ID:", component["unique_id"])
                    print("\tAmmount:", component["ammount"])
                    print()
                print()

        elif choice == 4:
            break
            