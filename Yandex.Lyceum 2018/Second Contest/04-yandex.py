def get_composers(lines):
    d = {}
    for line in lines:
        tmp = line.split(' (')
        tmp[1] = tmp[1].replace(')', '')
        composer = tmp[1].replace('\n', '')
        music = tmp[0]
        if d.get(composer, 1) == 1: 
            d[composer] = list()
        d[composer].append(music)
        d[composer].sort()
    return d


def main():
    result = get_composers(['Щелкунчик (Чайковский)',
                            'Симфония №6 «Патетическая» (Чайковский)',
                            'Времена года (Чайковский)',
                            'Лебединое озеро (Чайковский)',
                            'Спящая красавица (Чайковский)'
                            ])
    key, value = result.popitem()
    print(key + ':')
    for elem in value:
        print(elem)


if __name__ == "__main__":
    main()
