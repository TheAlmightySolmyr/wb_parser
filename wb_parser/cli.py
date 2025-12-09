import argparse


def cli_main():
    parser = argparse.ArgumentParser(description='WB parser')
    parser.add_argument('search', type=str, 
                        help='Search query. Input what are you looking for.')
    parser.add_argument('-minp', type=int, help='Input min price')
    parser.add_argument('-maxp', type=int, required=True, 
                        help='Input max price')
    parser.add_argument('-minr', type=float, help='Input min rating')
    parser.add_argument('-maxr', type=float, required=True, 
                        help='Input max rating')
    parser.add_argument('-country', type=str, 
                        help='Input Country of manufacture')
    parser.add_argument('-pages', type=int, default=3,
                        help='Number of pages for parsing. Default value is 3')
    args = parser.parse_args()
    print(f'''
    Search query: {args.search}

    Filters: price {args.minp}-{args.maxp} rub., rating {args.minr}-{args.maxr}

    Parsing {args.pages} pages''')
    if args.country:
        print(f'''
    Country of manufacture: {args.country}''')
