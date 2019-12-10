a_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u','v','w','x','y','z','.']

offset_list = [1,19,13,15,24,21,22,12,25,11,6,27,20,3,28,10,16,14,5,8,7,17,4,18,23,2,9,26]

offset_index = 0
jiami_list = 'xxyrkf.lqzfdksrogennf'
s_str = ''
for i in range(len(jiami_list)):
    if jiami_list[i] in a_list:
        num_enc = a_list.index(jiami_list[i])
    else:
        num_enc = 27
    
    tmp2 = offset_list[offset_index]
    if tmp2 == 28:
        num = num_enc
    elif num_enc < tmp2:
        num = num_enc + 28 - tmp2
    elif num_enc > tmp2:
        num = num_enc - tmp2
    offset_index += 1
    offset_index = offset_index%len(offset_list)
    if num == 27:
        s_str += ' '
    else:
        s_str += a_list[num]

print(s_str)
        


