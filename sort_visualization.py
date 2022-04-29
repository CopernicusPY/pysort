import pygame, time

pygame.init()

conf = {
    'bar.width': 30,
    'bar.height': None,
    'bar.x': 0,
    'bar.y': 0,
    'bar.color': (255, 255, 255),
    'screen.size': (800, 800),
    'screen.bg_color': (0, 0, 0),
    'sort.delay': 1,
    'sort.algorithm': 'bubblesort'
}
screen = pygame.display.set_mode(conf['screen.size'])
pygame.display.set_caption('Sort Visualization')

array = [
    10, 9 , 8, 7, 6, 5, 4, 3, 2, 1
]
def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                show(array, screen)
            time.sleep(conf['sort.delay'])
# Still trying to figure out how to visualize this thing :P
def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        mergesort(left)
        show(left, screen)
        mergesort(right)
        show(right, screen)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

def show(array, screen):
    screen.fill(conf['screen.bg_color'])
    for i in range(len(array)):
        conf['bar.x'] = i * conf['bar.width']
        conf['bar.y'] = conf['bar.y']
        conf['bar.height'] = array[i]
        pygame.draw.rect(screen, conf['bar.color'], pygame.Rect(conf['bar.x'], conf['bar.y'], conf['bar.width'], conf['bar.height']))
    pygame.display.update()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        show(array, screen)
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if conf['sort.algorithm'] == 'bubblesort':
                bubblesort(array)
            if conf['sort.algorithm'] == 'mergesort':
                mergesort(array)
  
        pygame.display.update()


main()
