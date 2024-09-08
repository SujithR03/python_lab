def traffic_lights(action):
    switcher={
            'red':'stop',
            'yellow':'slow',
            'green':'go'
            }
    return switcher.get(action,"invalid action")
print(traffic_lights('red'))
print(traffic_lights('yellow'))
print(traffic_lights('green'))
print(traffic_lights('blue'))

