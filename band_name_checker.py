import argparse
import datetime
import re
import string
import sys

import whois
from whois.parser import PywhoisError

replace_punctuation = str.maketrans(string.punctuation, ' ' * len(string.punctuation))


def lookup_domain(domain):
    result = None

    try:
        result = whois.whois(domain)

    except PywhoisError:
        pass

    return domain, result


def process_name(name):
    domains = create_domains(name.strip())

    results = map(lookup_domain, domains)
    actual_results = [(d, r) for d, r in results if r]

    return actual_results


def canonicalize(name):
    return name.translate(replace_punctuation).replace(' ', '')


def create_domains(name):
    domains = []

    if re.search(r"\.com|\.net", name) is None:
        canonical_name = canonicalize(name)
        domains.append(f'{canonical_name}.com')
        domains.append(f'{canonical_name}.net')
        domains.append(f'{canonical_name}band.com')
        domains.append(f'{canonical_name}band.net')
    else:
        domains.append(name)

    return domains


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check if domains for possible band names are already taken')
    parser.add_argument('band_names', metavar='name', type=str, nargs='*', help='possible band names')
    parser.add_argument('--file', help="file of possible band names, one per line")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    results = []

    if len(args.band_names) > 0:
        results = map(process_name, args.band_names)
    elif args.file is not None:
        with open(args.file) as file:
            lines = file.readlines()
            results = map(process_name, [line.strip() for line in lines if len(line.strip()) > 0])

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
