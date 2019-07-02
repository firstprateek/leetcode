text = 'adfkjnsdkjfmsgkjaskjfndskajlfnsdakj flnsdkja fndskj nfksajd nfsdajnf ckjsdancjksdna fjkn sdakjfn sdajklfn djksa fnk'

def generatePrefix(pattern):
  prefix = [0 for _ in range(len(pattern))]
  j = 0
  for i in range(1, len(pattern)):
    while j > 0 and pattern[j] != pattern[i]:
      j = prefix[j - 1]

    if pattern[i] == pattern[j]:
      j += 1

    prefix[i] = j

  return prefix

def kmp(text, pattern):
  ptable = generatePrefix(pattern)
  print('ptable: {}'.format(ptable))
  j = 0
  res = []
  for i in range(len(text)):
    while j > 0 and pattern[j] != text[i]:
      j = ptable[j - 1]

    if text[i] == pattern[j]:
      j += 1

    if j == len(pattern):
      res.append(i + 1 - j)
      j = ptable[j - 1]

  return res


for pattern in ['fn']:
  print(kmp(text, pattern))