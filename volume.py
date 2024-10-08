def converter_volume(litro, milimetro):
    litro = milimetro * 1000
    milimetro = litro // 1000
    return litro, milimetro
