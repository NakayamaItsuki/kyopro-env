def main():
    
    lines = []

    while True:
        line = input()
        lines.append(line)
        
        if line == "0":
          break
        
    for line in reversed(lines):
        print(line)
    
    

if __name__ == "__main__":
    main()
