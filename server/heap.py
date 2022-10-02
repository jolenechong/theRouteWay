def return_elem(x):
    return x

class MinHeap:
    def __init__(self, key=return_elem):
        self.heap_list = []
        self.size = 0
        self.comparison_func = key
        self.elem_dict = {}
    
    def sift_up(self, i):
        while i//2 >= 0:
            if self.comparison_func(self.heap_list[i]) < self.comparison_func(self.heap_list[i//2]):
            # if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]
                self.elem_dict[self.heap_list[i][0]] = i
                i = i//2
            else:
                break
        return i
    
    def find_min_child(self, i):
        if i*2+1 >= self.size or self.comparison_func(self.heap_list[i*2]) < self.comparison_func(self.heap_list[i*2+1]):
        # if i*2+1 >= self.size or self.heap_list[i*2] < self.heap_list[i*2+1]:
            return i*2
        else:
            return i*2+1   

    def sift_down(self, i):
        while i*2 < self.size:
            min_child = self.find_min_child(i)
            if self.comparison_func(self.heap_list[i]) > self.comparison_func(self.heap_list[min_child]):
            # if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[i]
                self.elem_dict[self.heap_list[i][0]] = i
                i = min_child
            else:
                break
        return i
    
    def push(self, elem):
        self.heap_list.append(elem)
        self.size += 1
        self.elem_dict[elem[0]] = self.sift_up(self.size-1)
    
    def pop(self):
        if self.size == 0:
            raise IndexError('Tried to pop from an empty heap')
        self.heap_list[0], self.heap_list[self.size-1] = self.heap_list[self.size-1], self.heap_list[0]
        min_elem = self.heap_list.pop()
        del self.elem_dict[min_elem[0]]
        self.size -= 1
        if self.size > 0:
            moved_elem = self.heap_list[0][0]
            self.elem_dict[moved_elem] = self.sift_down(0)
        return min_elem[0]

    def remove(self, elem):
        if elem in self.elem_dict:
            idx = self.elem_dict[elem]
            del self.elem_dict[elem]
            self.heap_list[idx], self.heap_list[self.size-1] = self.heap_list[self.size-1], self.heap_list[idx]
            self.heap_list.pop()
            self.size -= 1
            if self.size > 0 and idx < self.size:
                moved_elem = self.heap_list[idx][0]
                self.elem_dict[moved_elem] = self.sift_down(idx)
        else:
            raise KeyError('Tried to remove an element that is not present in heap')

    def peek(self):
        return self.heap_list[0][0]

    def isEmpty(self):
        return self.size == 0

    def get_elem(self, elem):
        if elem in self.elem_dict:
            return self.heap_list[self.elem_dict[elem]]
        return None
        # raise KeyError('Tried to access an element that is not present in heap')
