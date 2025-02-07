def arah (y, x):
    results = []
    if x %  2 :   #Timur
        results.append((y, x-1, 1))
        if x+1 < M*2:
            results.append((y, x+1, 2)) 
    else:   # Barat
        if x > 0:
            results.append((y, x-1, 2)) 
        results.append((y, x+1, 1))
    if y % 2 : #Selatan
        if y+1 < N*2:
            results.append((y+1, x, 2)) 
        results.append((y-1, x, 1))
    else: #Utara
        results.append((y+1, x, 1))
        if y > 0:
            results.append((y-1, x, 2))
    return results

f = open('input1.txt')
C = int(f.readline())
output = ''
for kasus in range(C):
    N, M = list(map(int, f.readline().split())) #Baris dan Kolom
    map_ = [] #persimpangan
    for baris in range(N):
        v = [int(x) for x in f.readline().split(' ')]
        SWT = [(v[i*3], v[i*3+1], v[i*3+2]) for i in range(M)]
        map_.append(SWT)
    min_waktu = [[None, None] * M for Baris in range(2*N)]
    min_waktu[(N-1)*2+1][0] = 0
    susunan = [((N-1)*2+1, 0, 0)]    # Pojok Timur Laut, ketika waktu = 0
    while susunan:
        susunan_baru = []
        for y, x, waktu in susunan:
            S, W, T = map_[y//2][x//2]
            for yn, xn, min_waktu_offset in arah(y, x):
                min_waktu_baru = waktu + min_waktu_offset
                if min_waktu[yn][xn] is None or min_waktu[yn][xn] > min_waktu_baru:
                    if min_waktu_offset == 2:
                        ok = True
                        waktu_baru = min_waktu_baru
                        # jalan antar blok
                    else:
                        # penyeberangan persimpangan
                        siklus = (waktu - T) % (S + W)
                        if siklus < 0:
                            siklus += S + W
                            # penyebrangan Utara-Selatan
                        if yn != y:
                            if siklus < S:
                                tunggu = 0
                            else:
                                tunggu = (S+W) - siklus
                        else:
                            if siklus < S:
                                tunggu = S - siklus
                            else:
                                tunggu = 0
                        waktu_baru = waktu + tunggu + min_waktu_offset
                        ok = min_waktu[yn][xn] is None or min_waktu[yn][xn] > waktu_baru
                    if ok:
                        min_waktu[yn][xn] = waktu_baru
                        susunan_baru.append((yn, xn, waktu_baru))
            susunan = susunan_baru
    output += 'Case #{}: {}'.format(kasus + 1, min_waktu[0][(M-1)*2+1]) + '\n'
    print ('Case #{}: {}'.format(kasus + 1, min_waktu[0][(M-1)*2+1]))

fn=open('output.txt', 'w')
fn.write(str(output))
fn.close()

