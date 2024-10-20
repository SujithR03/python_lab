import turtle 

def draw_bear(): 
    turtle.speed(2) 
    turtle.bgcolor("lightblue") 
    
    turtle.penup() 
    turtle.goto(0, -100) 
    turtle.pendown() 
    turtle.color("brown") 
    turtle.begin_fill() 
    turtle.circle(80) 
    turtle.end_fill() 
     
    turtle.penup() 
    turtle.goto(-30, 50) 
    turtle.pendown() 
    turtle.color("brown") 
    turtle.begin_fill() 
    turtle.circle(20) 
    turtle.end_fill() 
    
    turtle.penup() 
    turtle.goto(30, 50) 
    turtle.pendown() 
    turtle.color("brown") 
    turtle.begin_fill() 
    turtle.circle(20) 
    turtle.end_fill() 
   
    turtle.penup() 
    turtle.goto(-20, 10) 
    turtle.pendown() 
    turtle.color("black") 
    turtle.begin_fill() 
    turtle.circle(8) 
    turtle.end_fill() 
    
    turtle.penup() 
    turtle.goto(20, 10) 
    turtle.pendown() 
    turtle.color("black") 
    turtle.begin_fill() 
    turtle.circle(8) 
    turtle.end_fill() 
    
    turtle.penup() 
    turtle.goto(0, -5) 
    turtle.pendown() 
    turtle.color("black") 
    turtle.begin_fill() 
    turtle.circle(3) 
    turtle.end_fill() 
    
    turtle.penup() 
    turtle.goto(-20, -20) 
    turtle.pendown() 
    turtle.color("black") 
    turtle.width(3) 
    turtle.right(90)  
    turtle.circle(20, 180)  
    
    turtle.hideturtle()  
    turtle.done()  
draw_bear()
