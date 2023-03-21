def to_float(price_str: str | None) -> float | None:
    if not price_str:
        return
    processed_price_str = ''
    for char in price_str:
        if char in ' ' or char.isalpha():
            break
        processed_price_str += char
    return float(processed_price_str)
