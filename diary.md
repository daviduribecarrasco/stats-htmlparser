# design diary
I struggled at first to get the data that I wanted from the page. Even if I used the class name for data that I wanted, my program would return None. After some googling, I somewhat better understood how to get the info I wanted. The information I wanted was already conveniently in a table, so what I did was find all the table rows, and for each table row retrieve all the info in the td elements. This worked when it came to retrieving the data, which I stored in a dictionary. My program can print out all the data correctly, but I was having trouble understanding how to store it in a csv file. I still haven't gotten that part to work properly, but I hope to be able to fix it soon. It was cool to learn how to get data from a website, even if I don't have all of it quite figured out yet. I can see how scripts like this would be useful or applicable for more practical stuff.

2-27-20 Update

It's now able to correctly input the information into a csv file. The keys did not match what was in csv_columns (I had slightly different words). Once they matched
it began to work. There's still stuff I need to fix in my for loop, but it's working better than before.

