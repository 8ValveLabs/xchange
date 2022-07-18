import sys

def main():
    if len(sys.argv) > 0 : handle_args()
    else : print("No args passed.")

def handle_args():
    for counter, argument in enumerate(sys.argv):
        print("ARG#{} = ".format(counter)+argument)


if __name__ == '__main__':
    main()