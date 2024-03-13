def main():
    
    string = input()

    s1 = string.split('|')[0]
    s2 = string.split('|')[2]

    print (s1+s2)


if __name__ == "__main__":
    main()
