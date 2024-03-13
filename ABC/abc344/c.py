def main():
  
  N = int(input())
  As = list(map(int, input().split()))
  
  M = int(input())
  Bs = list(map(int, input().split()))
  
  L = int(input())
  Cs = list(map(int, input().split()))
  
  Q = int(input())
  Xs = list(map(int, input().split()))
  
  sum_set = set()
  
  for a in As:
      for b in Bs:
          for c in Cs:
              sum_set.add(a+b+c)
              
  for x in Xs:
      if x in sum_set:
          print('Yes')
      else:
          print('No')

if __name__ == "__main__":
    main()
