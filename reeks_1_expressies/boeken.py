book_price = 24.95
discount_rate = 0.4
nb_book = 60
shipping_cost = 3 + 0.75 * (nb_book-1)
total_price = (nb_book * book_price) * (1-discount_rate) + shipping_cost
print(total_price)