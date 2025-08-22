from small import main as smain
from glob import arr

def main() -> None:
    print("big before:" + str(arr))
    smain()
    print("big after:" + str(arr))

if __name__ == "__main__":
    main()
