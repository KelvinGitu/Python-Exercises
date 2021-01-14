from __future__ import print_function

def main():
    f = open("data.txt", "w+")

    print("Nama file\t:", f.name)
    print("Tertutup?\t:", f.closed)
    print("Mode akses\t:", f.mode)

if __name__ == '__main__':
    main()