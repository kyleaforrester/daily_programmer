#!/usr/binenv python3

def fold_paper(seq):
    new_seq = []
    ones = [0,1]
    for s in range(len(seq)):
        new_seq.append(ones[(s+1)%2])
        new_seq.append(seq[s])
    new_seq.append(0)
    return new_seq


if __name__=='__main__':
    seq = [1]
    for i in range(8):
        seq = fold_paper(seq)
    for s in seq:
        print(s, end='')
