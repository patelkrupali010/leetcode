def restoreString(s, indices):
        # res = [''] * len(s)
        # for i in indices:
        #     res[indices[i]] = s[i]
        # return ''.join(res)

        res = ''
        for i in range(len(indices)):
                print(indices.index(i)) #i=0 => 4, i=1 => 6.. position of index in indices
                res += s[indices.index(i)]

print(restoreString("codeleet", [4,5,6,7,0,2,1,3]))

