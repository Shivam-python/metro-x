from sys import argv
from app.command_processor import CommandProcessor
from services.travel_service import TravelService
from services.accounting_service import AccountingService
from pricing.fixed_fare import FixedFareStrategy
from config.constants import STATIONS

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    accounting = AccountingService(STATIONS)
    travel_service = TravelService(FixedFareStrategy(), accounting)
    processor = CommandProcessor(travel_service)

    with open(argv[1]) as f:
        for line in f:
            processor.process(line.strip(), accounting)
    

if __name__ == "__main__":
    main()
