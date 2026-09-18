trans_map = {
    ord('Я'): 'Ya',
    ord('н'): 'n',
    ord('а'): 'a',
    ord('о'): 'o',
}

text = "Hello Wоrld" # о - українська

idx = text.find('World')

print(idx) # -1

new_idx = text.translate(trans_map).find('World')

print(new_idx) # 6