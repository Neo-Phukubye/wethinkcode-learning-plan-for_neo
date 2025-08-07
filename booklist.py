book_list=[]

firstbook= input("What are your first favorite books?")
secondbook= input("What are your second favorite books?")
thirdbook= input("What are your third favorite books?")

book_list.append(firstbook)
book_list.append(secondbook)
book_list.append(thirdbook)

book_list.sort()
print(book_list)