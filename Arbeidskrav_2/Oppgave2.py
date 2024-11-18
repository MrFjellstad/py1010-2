"""
Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen. 
Alle før 1/4 pizza hver
"""
import math

antall_elever = int(input('Skriv inn antall elever:'))
antall_elever_pr_pizza = 4
antall_pizza = math.ceil(antall_elever / antall_elever_pr_pizza)

print(f'Det må handles inn {antall_pizza} pizzaer til festen')
