#Step 1 Welcoming the user
name=input("Hello! what is your name? ")
print(f"Hello {name} nice to meet you!")
#Step 2 Budget
budget=int(input("What is your budget.$ "))
item_cost=int(input("What is the cost of one item. "))
if budget>=item_cost:
    print("You can afford the item!")
else:
    print("Sorry! you cannot afford the item. ")
#Step 3 Shopping list + decoration colors
itemlist=[]
for i in range(3):
    items=input("Tell me 3 items to buy ")
    itemlist.append(items)
colors=("Red","blue","Cyan")
# Step 4 Drawing the decorations(using turtle)
import turtle
t=turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.goto(-220,0)
t.pendown()
t.color("blue")
t.begin_fill()
for u in range(5):#Draw star
    t.fd(100)
    t.left(72)
    t.fd(100)
    t.right(144)
t.end_fill()
t.color("red")
t.penup()
t.goto(220,-20)
t.begin_fill()
t.pendown
t.circle(100)  # Draw the balloon body
t.end_fill()
# Draw the balloon string
t.color("Grey")
t.right(90)
t.penup()
t.forward(190)
t.pendown()
t.right(180)
t.forward(200)
t.penup()
t.goto(160,35)
t.pendown()
t.color("cyan")
t.write("Im enjoying\n this party\n So much!",font=("Curlz MT","20","bold"))
turtle.done()
#Step 5 Total costs
outputs=[]
Itemscost=0
for money in range(3):
    cost=int(input("Enter the cost of your 3 items "))
    outputs.append(cost)
Itemscost=sum(outputs)
#Bonus Challenge budget check
if budget>=Itemscost:
    print("Your budget is enough. You are ready!")
else:
    print("Warning!. Your budget is not enough to buy the items.")
#Step 6 summary 
print(f"So {name} this is your party summary!")
print("Your shopping list: ")
for  list in itemlist:
    print(list)
print("Your total cost: ")
print(f"${Itemscost}")
print("And finally your decoration colors")
for decoration in colors:
    print(decoration)
print("You are ready to go!!!")