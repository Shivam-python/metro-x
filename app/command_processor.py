class CommandProcessor:
    def __init__(self, travel_service):
        self.service = travel_service

    def process(self, line, accounting):
        parts = line.split()
        cmd = parts[0]

        if cmd == "BALANCE":
            self.service.add_card(parts[1], int(parts[2]))
        elif cmd == "CHECK_IN":
            self.service.check_in(parts[1], parts[2], parts[3])
        elif cmd == "PRINT_SUMMARY":
            # Print summary
            for station, data in accounting.stats.items():
                print(f"TOTAL_COLLECTION {station} {data['income']} {data['discount']}")
                print("PASSENGER_TYPE_SUMMARY")
                for k, v in data.items():
                    if k not in ("income", "discount") and v > 0:
                        print(f"{k} {v}")
    
