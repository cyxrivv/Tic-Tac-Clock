
a1 = ' '
a2 = ' '
a3 = ' '
b1 = ' '
b2 = ' '
b3 = ' '
c1 = ' '
c2 = ' '
c3 = ' '


marked_list = []

xWin = False


board = f'a |{a1}|{a2}|{a3}|\n'\
        f'b |{b1}|{b2}|{b3}|\n'\
        f'c |{c1}|{c2}|{c3}|\n'\
         '   1 2 3'     
print(board)

def x_changeb(m):
    global a1, a2, a3, c1, c2, c3, b1, b2, b3, board, xturn, oturn, marked_list
    valid_input = True
    for mem in marked_list:
        if m == mem:
            print('position taken, try again')
            valid_input = False
        else:
            valid_input == True
    if game_end == False and valid_input == True:
        if m == 'a1':
            a1 = 'x'
            xturn == False
            marked_list.append(m)       
        if m == 'a2':
            a2 = 'x'
            xturn == False
            marked_list.append(m) 
        if m == 'a3':
            a3 = 'x'
            xturn == False
            marked_list.append(m)
        if m == 'b1':
            b1 = 'x'
            xturn == False
            marked_list.append(m) 
        if m == 'b2':
            b2 = 'x'
            xturn == False
            marked_list.append(m) 
        if m == 'b3':
            b3 = 'x'
            xturn == False
            marked_list.append(m) 
        if m == 'c1':
            c1 = 'x'
            xturn == False
            marked_list.append(m) 
        if m == 'c2':
            c2 = 'x'
            xturn == False
            marked_list.append(m) 
        if m == 'c3':
            c3 = 'x'
            xturn == False
            marked_list.append(m) 

        board = f'a |{a1}|{a2}|{a3}|\n'\
        f'b |{b1}|{b2}|{b3}|\n'\
        f'c |{c1}|{c2}|{c3}|\n'\
         '   1 2 3'     
    
       
    
    
def o_changeb(m):
    global a1, a2, a3, c1, c2, c3, b1, b2, b3, board, xturn, oturn, marked_list
    valid_input = True
    for mem in marked_list:
        if m == mem:
            print('position taken, try again')
            valid_input = False
        else:
            valid_input == True
    if game_end == False and valid_input == True:
        if m == 'a1':
            a1 = 'o'
            oturn == False
            marked_list.append(m)       
        if m == 'a2':
            a2 = 'o'
            oturn == False
            marked_list.append(m) 
        if m == 'a3':
            a3 = 'o'
            oturn == False
            marked_list.append(m)
        if m == 'b1':
            b1 = 'o'
            oturn == False
            marked_list.append(m) 
        if m == 'b2':
            b2 = 'o'
            oturn == False
            marked_list.append(m) 
        if m == 'b3':
            b3 = 'o'
            oturn == False
            marked_list.append(m) 
        if m == 'c1':
            c1 = 'o'
            oturn == False
            marked_list.append(m) 
        if m == 'c2':
            c2 = 'o'
            oturn == False
            marked_list.append(m) 
        if m == 'c3':
            c3 = 'o'
            oturn == False
            marked_list.append(m) 

        board = f'a |{a1}|{a2}|{a3}|\n'\
        f'b |{b1}|{b2}|{b3}|\n'\
        f'c |{c1}|{c2}|{c3}|\n'\
         '   1 2 3'     
       

def check_win():
    global game_end

    
    if (
        
        (a1 == 'x' and a2 == 'x' and a3 == 'x') or
        (b1 == 'x' and b2 == 'x' and b3 == 'x') or
        (c1 == 'x' and c2 == 'x' and c3 == 'x') or

        
        (a1 == 'x' and b1 == 'x' and c1 == 'x') or
        (a2 == 'x' and b2 == 'x' and c2 == 'x') or
        (a3 == 'x' and b3 == 'x' and c3 == 'x') or

        
        (a1 == 'x' and b2 == 'x' and c3 == 'x') or
        (a3 == 'x' and b2 == 'x' and c1 == 'x')
    ):
        print("x wins")
        game_end = True
        return


    
    if (
        
        (a1 == 'o' and a2 == 'o' and a3 == 'o') or
        (b1 == 'o' and b2 == 'o' and b3 == 'o') or
        (c1 == 'o' and c2 == 'o' and c3 == 'o') or

        
        (a1 == 'o' and b1 == 'o' and c1 == 'o') or
        (a2 == 'o' and b2 == 'o' and c2 == 'o') or
        (a3 == 'o' and b3 == 'o' and c3 == 'o') or

        
        (a1 == 'o' and b2 == 'o' and c3 == 'o') or
        (a3 == 'o' and b2 == 'o' and c1 == 'o')
    ):
        print("o wins")
        game_end = True
      

                                                                                           
                                                                                           
                                                                                           
                                                                                           



game_end = False
xturn = True
oturn = False

def check_list():
    global game_end, xturn, oturn

    while game_end == False:
        
        if xturn == True:
            print('x turn: ')
            m = input()
            x_changeb(m)
            print(board)
            check_win()
            xturn = False
            oturn = True

        else:
            if oturn == True:
                print('o turn: ')
                m = input()
                o_changeb(m)
                print(board)
                check_win()
                xturn = True
                oturn = False
check_list()



    
    
        
        
        
        
    
        
        






    