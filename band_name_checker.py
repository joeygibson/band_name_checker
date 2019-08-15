import argparse
import datetime
import sys

import whois
from whois.parser import PywhoisError


def domain_lookup(domain):
    domain = domain.strip()
    result = None
    try:
        result = whois.whois(domain)
    except PywhoisError:
        pass

    return domain, result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='See if possible band names\' domains are already taken')
    parser.add_argument('band_names', metavar='name', type=str, nargs='*', help='possible band names')
    parser.add_argument('--file')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    results = []

    if len(args.band_names) > 0:
        results = map(domain_lookup, args.band_names)
    elif args.file is not None:
        with open(args.file) as file:
            lines = file.readlines()
            results = map(domain_lookup, [line.strip() for line in lines if len(line.strip()) > 0])

    for d, r in results:
        if r is not None:
            creation_date = None

            if isinstance(r.creation_date, datetime.datetime):
                creation_date = str(r.creation_date)
            else:
                creation_date = ', '.join(map(str, r.creation_date))

            print(f'{d} registered on {creation_date}')
        else:
            print(f'{d} not registered')
