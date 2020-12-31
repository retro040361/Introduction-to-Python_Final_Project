class Categories:
    def __init__(self):
        '''
        initialization of the object
        '''
        self._categories =  ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
    

    def view(self):
        '''
        print the categories by inner function view_categories()
        '''
        temp = []
        def view_categories(categories,depth=0):
            '''
            recursively print the categories
            '''
            #temp = []
            for i in categories:
                if type(i) == list:
                    view_categories(i,depth + 1)
                else:
                    #print(f'{" "*2*depth}- {i}')
                    temp.append(str(" "*2*depth+'-'+ str(i)))
            return temp
        return view_categories(self._categories)

    def is_category_valid(self,category):
        '''
        check whether the parameter is in the cateroies of the object
        '''
        def is_valid(category,categories):
            '''
            recursively check
            '''
            if type(categories) == list:
                for i,v in enumerate(categories):
                    p = is_valid(category,v)
                    if p == True:
                        return (i,)
                    if p != False:
                        return (i,) + p
            return categories == category
        return is_valid(category,self._categories)
    
    def find_subcategories(self,category):
        '''
        check whether the parameter has a subcategories in the categories of the object
        '''
        """
        def _flatten(L):
            '''
            return a list which is not a nest-list
            '''
            if type(L) == list:
                result = []
                for element in L:
                    result.extend(_flatten(element))
                return result
            else:
                return [L]
            
        def find_sub(categories,category):
            '''
            recursively find subcategories
            '''
            if type(categories) == list:
                for i in categories:
                    p = find_sub(i,category)
                    if p == True:
                        index = categories.index(i)
                        if index + 1 < len(categories) and type(categories[index + 1]) == list:
                            return _flatten(categories[index:index + 2])
                        else:
                            return [i]
                    if p != []:
                        return p
            return True if categories == category else []
            """
        #categories: menu ,category: input
        def find_sub_gen(categories,category,found = False):
            if type(categories) == list:
                for index,child in enumerate(categories):
                    yield from find_sub_gen(child,category,found) #flatten
                    if child == category and index+1 < len(categories) and type(categories[index+1]) == list:
                        yield from  find_sub_gen(categories[index+1],category,True)
            else:
                if categories == category or found == True:
                    yield categories
                    
        return find_sub_gen(self._categories,category)