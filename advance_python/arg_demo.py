import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )
    # required argument
    parser.add_argument('-x','--execute',action='store',required=True,help ="help text for option x")
    
    # optinal argument
    parser.add_argument('-y',help='help text for option y', default=False)
    
    parser.add_argument('-z',help= "help text for option z",type = int)
    
    print(parser.parse_args())


if __name__ =='__main__':
    get_args()