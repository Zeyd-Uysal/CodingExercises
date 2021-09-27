def page_digits(pages):
    total = 0
    for i in range(len(str(pages)), 0, -1):
        max_val =  int(10**(i-1) -1)
        current_val = pages - max_val
        pages = max_val
        total += (current_val *i)
    return(total)
if __name__ == '__main__':
    page_digits(12)
    