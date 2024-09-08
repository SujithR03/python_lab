def animal_sounds(animal):
    switcher={
            'dog':'bark',
            'cat':'meow',
            'cow':'moo',
            'lion':'roar'
            }
    return switcher.get(animal,"unknown sound")
print(animal_sounds('dog'))
print(animal_sounds('cow'))
print(animal_sounds('cheetah'))
                
                

