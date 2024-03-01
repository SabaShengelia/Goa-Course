"""day 5:
homework:

შექმენით ცვლადები 10 წიგნისთვის ( სახელი ცალკე, ფასი ცალკე, 
5 წიგნს გაუკეთეთ 10%იანი ფასდაკლება, 5 წიგნს გაუკეთეთ 20%იანი ფასდაკლება) 

იგივე წესებით, რაც გაკვეთილზე ავხსენით""" 

#Declaring Value Of Books Price
book1_first_price = 20
book2_first_price = 40
book3_first_price = 60 
book4_first_price = 80 
book5_first_price = 100 
book6_first_price = 120
book7_first_price = 140
book8_first_price = 160
book9_first_price = 180
book10_first_price = 200 

#Declaring Value Of Small Discount
ten_percent_discount = 10

#Declaring Value Of Large Discount
twenty_percent_discount = 20

#Declaring Values After Small Discount
book1_price_after_discount = book1_first_price - (book1_first_price * ten_percent_discount/100)
book2_price_after_discount = book2_first_price - (book2_first_price * ten_percent_discount/100)
book3_price_after_discount = book3_first_price - (book3_first_price * ten_percent_discount/100)
book4_price_after_discount = book4_first_price - (book4_first_price * ten_percent_discount/100)
book5_price_after_discount = book5_first_price - (book5_first_price * ten_percent_discount/100)
#Declaring Values After Large Discount
book6_price_after_discount = book6_first_price - (book6_first_price * twenty_percent_discount/100)
book7_price_after_discount = book7_first_price - (book7_first_price * twenty_percent_discount/100)
book8_price_after_discount = book8_first_price - (book8_first_price * twenty_percent_discount/100)
book9_price_after_discount = book9_first_price - (book9_first_price * twenty_percent_discount/100)
book10_price_after_discount = book10_first_price - (book10_first_price * twenty_percent_discount/100)

#Displaying Final Prices Of Small Discount Books
print("Book 1 Price Is:" ,book1_price_after_discount, "Book 2 Price Is:" 
      ,book2_price_after_discount, "Book 3 Price Is:" ,book3_price_after_discount,
       "Book 4 Price Is:" ,book4_price_after_discount, "Book 5 Price Is:"
        ,book5_price_after_discount,)

#Displaying Final Prices Of Large Discount Books
print("Book 6 Price Is:" ,book6_price_after_discount, "Book 7 Price Is:" 
      ,book7_price_after_discount, "Book 8 Price Is:" ,book8_price_after_discount,
      "Book 9 Price Is:" ,book9_price_after_discount, "Book 10 Price Is:"
      ,book10_price_after_discount,)

