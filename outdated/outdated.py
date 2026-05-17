months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
            m, d, y = date.split("/")
            m, d, y = int(m), int(d), int(y)
        elif "," in date:
            m_name, d, y = date.replace(",", "").split()
            m = months.index(m_name) + 1
            d, y = int(d), int(y)
        else:
            raise ValueError

        if 1 <= m <= 12 and 1 <= d <= 31:
            print(f"{y:04}-{m:02}-{d:02}")
            break
    except (ValueError, AttributeError):
        pass
