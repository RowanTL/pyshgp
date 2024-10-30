from glob import arr

def main() -> None:
    print("small before:" + str(arr))
    arr.append(10)
    print("small after:" + str(arr))

if __name__ == "__main__":
    main()
