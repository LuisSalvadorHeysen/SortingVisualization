import pygame
from tkinter import *
import os
import random
import tkinter.font as font

class SortingVisualization:
    def __init__(self, root, WIDTH, HEIGHT):
        self.width = WIDTH # Width of the pygame window
        self.height = HEIGHT # Height of the pygame window

        self.root = root # Tkinter Tk() object

        self.root.title('Sorting Algorithms Visualization') # Set title
        self.root.state('zoomed') # Full screen
        embed = Frame(self.root, width=self.width, height=self.height) # creates embed frame for pygame window
        embed.grid(columnspan=(600), rowspan=500) # Adds grid
        embed.pack(side=RIGHT) # Pack window to the right
        os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'
        self.wn = pygame.display.set_mode((self.width, self.height)) # Pygame window
        self.wn.fill(pygame.Color(0, 0, 0)) # Black background
        pygame.display.init()
        pygame.display.update()

        # Buttons and labels
        self.myFont1 = font.Font(family='Helvetica', size=11, weight='bold')
        self.title = Label(self.root, text='Sorting Algorithms Visualization')
        self.title['font'] = self.myFont1
        self.title.place(x=130, y=10, anchor='center')

        self.myFont2 = font.Font(family='Helvetica', size=10)

        self.label_algorithm = Label(self.root, text='Select Algorithm:')
        self.label_algorithm['font'] = self.myFont2
        self.label_algorithm.place(x=15, y=50)

        self.algo = StringVar()
        self.algo.set('Bubble Sort')
        self.algo_drop = OptionMenu(self.root, self.algo, 'Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort')
        self.algo_drop['font'] = self.myFont2
        self.algo_drop.place(x=140, y=45)

        self.num_label = Label(self.root, text='Number of elements:')
        self.num_label['font'] = self.myFont2
        self.num_label.place(x=15, y=80)

        self.num_entry = Entry(self.root, width=17)
        self.num_entry.place(x=142, y=80)

        self.sort_button = Button(self.root, text='SORT', width=25, command=self.initiate)
        self.sort_button['font'] = self.myFont1
        self.sort_button.place(x=15, y=145)

        self.reset_button = Button(self.root, text='New Array', width=25, command=self.reset_array)
        self.reset_button['font'] = self.myFont1
        self.reset_button.place(x=15, y=110)

        self.comp_label = Label(self.root, text='Time Complexity (Worst Case): ')
        self.comp_label['font'] = self.myFont2
        self.comp_label.place(x=5, y=190)

        self.comp_val = Label(self.root, text='')
        self.comp_val['font'] = self.myFont1
        self.comp_val.place(x=190, y=190)

        self.comp_label_av = Label(self.root, text='Time Complexity (Average): ')
        self.comp_label_av['font'] = self.myFont2
        self.comp_label_av.place(x=5, y=220)

        self.comp_val_av = Label(self.root, text='')
        self.comp_val_av['font'] = self.myFont1
        self.comp_val_av.place(x=190, y=220)

    # Method to reset array
    def reset_array(self):
        self.num = int(self.num_entry.get())
        self.arr = self.create_array()
        self.plot_array(-1, '')

    # Method to start sorting
    def initiate(self):
        selection = self.algo.get()

        if selection == 'Bubble Sort':
            self.comp_val.config(text='O(N^2)')
            self.comp_val_av.config(text='O(N^2)')
            self.bubble_sort()

        elif selection == 'Insertion Sort':
            self.comp_val.config(text='O(N^2)')
            self.comp_val_av.config(text='O(N^2)')
            self.insertion_sort()
            
        elif selection == 'Quick Sort':
            self.comp_val.config(text='O(N^2)')
            self.comp_val_av.config(text='O(N logN)')
            self.quick_sort()
            self.plot_array('final', '')

        elif selection == 'Merge Sort':
            self.comp_val.config(text='O(N logN)')
            self.comp_val_av.config(text='O(N logN)')
            self.mergeSort(0, len(self.arr))
            self.plot_array('final', '')

    # Bubble sort algorithm
    def bubble_sort(self):
        for _ in range(len(self.arr) - 1):
            for i in range(len(self.arr) - 1):
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                pygame.event.pump()
                self.plot_array(i, 'bubble')
        self.plot_array('final', '')

    # Insertion sort algorithm
    def insertion_sort(self):
        for i in range(len(self.arr)):
            curr = self.arr.pop(i)
            j = i - 1
            while j >= 0 and self.arr[j] > curr:
                self.plot_array(j, 'insertion')
                j -= 1
            self.plot_array(i, 'insertion')
            
            self.arr.insert(j + 1, curr)
        self.plot_array('final', '')

    # Merge method for merge sort
    def MERGE(self, start, mid, end):
        L = self.arr[start:mid]
        R = self.arr[mid:end]
        i = 0
        j = 0
        k = start
        for l in range(k, end):
            self.plot_array(l, 'merge')
            if j >= len(R) or (i < len(L) and L[i] < R[j]):
                self.arr[l] = L[i]
                i += 1
            else:
                self.arr[l] = R[j]
                j += 1  

    # Merge sort algorithm
    def mergeSort(self, p, r):
        if r - p > 1:
            mid = int((p+r)/2)
            self.mergeSort(p, mid)
            self.mergeSort(mid, r)
            self.MERGE(p, mid, r)

    # Quick sort algorithm
    def quick_sort(self, start=0, end=None):
        if end is None:
            end = len(self.arr) - 1

        if start < end:
            pivot = self.partition(start, end)
            self.quick_sort(start, pivot - 1)
            self.quick_sort(pivot + 1, end)

    # Partition method for quick sort
    def partition(self, start=0, end=None):
        if end is None:
            end = len(self.arr) - 1

        l, r = start, end - 1

        while r > l:
            if self.arr[l] <= self.arr[end]:
                l += 1
            elif self.arr[r] > self.arr[end]:
                r -= 1
            else:
                self.arr[l], self.arr[r] = self.arr[r], self.arr[l]
                self.plot_array((l, r), 'quicksort')

        if self.arr[l] > self.arr[end]:
            self.arr[l], self.arr[end] = self.arr[end], self.arr[l]
            return l
        else:
            return end

    # Method to show array as bars
    def plot_array(self, check, curr_algo):

        self.wn.fill((0, 0, 0))

        for i in range(len(self.arr)):

            color = (255, 255, 255)
            
            if curr_algo == 'bubble':
                if check == i or check == i + 1:
                    color = (255, 0, 0)

            elif curr_algo == 'merge' or curr_algo == 'insertion':
                if check == i:
                    color = (255, 0, 0)
                
            elif isinstance(check, tuple) and curr_algo == 'quicksort':
                if i == check[0] or i == check[1]:
                    color = (255, 0, 0)
                
            elif check == 'final':
                color = (0, 255, 0)            
                
            if len(self.arr) > 450 and len(self.arr) <= self.width:
                pygame.draw.line(self.wn, color, [i*self.width//self.num, self.height - int(self.arr[i])], [i*self.width//self.num, self.height], self.width//self.num)

            elif len(self.arr) > self.width:
                pygame.draw.line(self.wn, color, [i*self.width//self.num, self.height - int(self.arr[i])], [i*self.width//self.num, self.height], 1)

            else:
                pygame.draw.rect(self.wn, color, [i*self.width//self.num, self.height - int(self.arr[i]), self.width//self.num, int(self.arr[i])])
                if len(self.arr) <= 350:
                    pygame.draw.rect(self.wn, (0, 0, 0), [i*self.width//self.num, self.height - int(self.arr[i]), self.width//self.num, int(self.arr[i])], 1)

        pygame.display.update()
        self.root.update()

    # Method to create numeric array
    def create_array(self):
        adding_value = self.height/self.num
        arr = [adding_value]

        index = 1

        for i in range(self.num - 1):
            arr.insert(index, arr[index - 1] + adding_value)
            index  += 1

        random.shuffle(arr)    

        return arr


if __name__ == '__main__':
    main_window = Tk()
    Program = SortingVisualization(main_window, 1100, 700)

