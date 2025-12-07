import argparse


def cli_main():
    parser = argparse.ArgumentParser(description='WB parser')
    parser.add_argument('search', type=str, 
                        help='Search query. Input what are you looking for.')
    parser.add_argument('-minp', type=int, help='Input min price')
    parser.add_argument('-maxp', type=int, required=True, 
                        help='Input max price')
    parser.add_argument('-minrate', type=float, help='Input min rating')
    parser.add_argument('-maxrate', type=float, required=True, 
                        help='Input max rating')
    parser.add_argument('-country', type=str, 
                        help='Input Country of manufacture')
    args = parser.parse_args()
    print(args)