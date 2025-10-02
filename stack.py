class Stack:
    stack_items = []
    def push(self, item):
        Stack.stack_items.append(item)
    def pop(self):
        if len(Stack.stack_items):
            Stack.stack_items.pop()
        else:
            print('no item in stack')
    def peek(self):
        if len(Stack.stack_items):
            return Stack.stack_items[-1]
        else:
            print('no item in stack')
    def isEmpty(self):
        if not len(Stack.stack_items):
            print('yes')
        else:
            print('no')


    def reversed_string(self, string):
        for item in string:
            Stack.push(self, item)

        new_str = ''
        for i in range(len(Stack.stack_items)):
            new_str += self.peek()
            self.pop()

        return new_str


    def balanced(self, entry):
        pairs = {']': '[', '}': '{', ')': '(', '>': '<'}
        last_added = []
        for i in entry:

            if i in '[{(<':
                Stack.push(self, i)
                last_added.append(i)

            elif i in ']})>':
                last_added.append(i)
                if Stack.stack_items:
                    last = Stack.peek(self)
                else:
                    return 'Not balanced'

                if last == pairs[i] and last in last_added:
                    Stack.pop(self)
                    last_added.pop()
                    last_added.pop()
                else:
                    return 'Not balanced'

        if not last_added and not Stack.stack_items:
            return 'balanced'




