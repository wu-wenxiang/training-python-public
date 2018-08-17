from stack_SStack import *
from myQueue.SQueue import *

'''
迷宫问题
'''
maze1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 记录一个点薰衣草东南西北的位置点
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# 给迷宫 maze 的位置 pos 标 2 表示“到过了”
def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2


# 检查迷宫 maze 的位置 pos 是否可行
def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0


############################################
########## A recursive maze path finder ####

def maze_solver_rec(maze, start, end):
    """ A maze solver using a recursive procedure to find the path.
    递归实现
    """

    def find_path(maze, start, end):
        mark(maze, start)
        if start == end:  # 已到达出口
            print(start, end=' ')  # 输出这个位置
            return True  # 成功结束
        for i in range(4):  # 否则按四个方向顺序探查
            nextp = start[0] + dirs[i][0], start[1] + dirs[i][1]  # 下一个考虑
            if passable(maze, nextp):  # 不可行的相邻位置不管
                if find_path(maze, nextp, end):  # 如果从 nextp 可达出口
                    print(start, end=' ')  # 输出这个点
                    return True  # 成功结束
        return False

    print("If find, print the path from end to start:")
    if find_path(maze, start, end):
        print("\n")
    else:
        print("No path exists.")


# end maze_solver_rec


##################################################
####### A non-recursive maze path finder #########
####### which use a stack as temprary storage ####
'''
使用栈
'''
def print_path(end, last, st):
    print(end, last, sep=" ", end=' ')
    while not st.is_empty():
        print(st.pop()[0], end=' ')
    print('\n')


def print_path_rev(end, last, st):  # print the path from start to end
    path = [end, last]
    while not st.is_empty():
        path.append(st.pop())
    path.reverse()
    for pos in path:
        print(pos, end=" ")
    print('\n')


def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)
    st.push((start, 0))  # start position into stack 入口和方向 0 的序对入栈
    while not st.is_empty():  # have possibility to try 走不通时回退
        pos, nxt = st.pop()  # get last branch position 取栈顶及其探查方向
        for i in range(nxt, 4):  # try to find unexploring dir(s) 依次检查未探查方向
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])  # next point 算出下一点
            if nextp == end:  # find end, great! :-) 到达出口,打印路径
                print_path(end, pos, st)
                return
            if passable(maze, nextp):  # new position is passable 遇到未探查的新位置
                st.push((pos, i + 1))  # original position in stack 原位置和下一方向入栈
                mark(maze, nextp)
                st.push((nextp, 0))  # new position into stack 新位置入栈
                break # 退出内层循环，下次迭代将以新栈顶为当前位置继续
    print("No path.")  # :-( 找不到路径


####### Search a maze using a queue ##############
####### No path record ###########################
'''
使用队列
'''
def maze_solver_queue(maze, start, end):
    if start == end:
        print("Path finds.")
        return
    qu = SQueue()
    mark(maze, start)
    qu.enqueue(start)  # start position into queue
    while not qu.is_empty():  # have possibility to try
        pos = qu.dequeue()  # take next try position
        for i in range(4):  # chech each direction
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])  # next position
            if passable(maze, nextp):  # find new position
                if nextp == end:  # end position, :-)
                    print("Path finds.")  # where is the path??
                    return
                mark(maze, nextp)
                qu.enqueue(nextp)  # new position into queue
    print("No path.")  # :-(


####### Search a maze using a queue ###############
####### recording the path precedent relation #####

def build_path(start, pos, end, precedent):
    path = [end]
    while pos != start:
        path.append(pos)
        pos = precedent[pos]
    path.append(start)
    path.reverse()
    return path


def maze_solver_queue1(maze, start, end):
    if start == end:
        return [start]
    qu = SQueue()
    precedent = dict()
    mark(maze, start)
    qu.enqueue(start)  # start position into queue
    while not qu.is_empty():  # have possibility to try
        pos = qu.dequeue()  # take next try position
        for i in range(4):  # chech each direction
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])  # next position
            if passable(maze, nextp):  # find new position
                if nextp == end:  # end position, :-)
                    return build_path(start, pos, end, precedent)
                mark(maze, nextp)
                precedent[nextp] = pos  # set precedent of nextp
                qu.enqueue(nextp)  # new position into queue
    print("No path.")  # :-(


#### Another implementation using a stack.
#### A pos and a stack hold the information used in searching.
#### It seems that this implementation is not really better,
#### not clearer, nor shorter, nor conceptly better.
def print_path1(end, st):
    print(end, end=' ')
    while not st.is_empty():
        print(st.pop()[0], end=' ')
    print('\n')


def maze_solver1(maze, start, end):
    st = SStack()
    pos, nxt = start, 0
    while True:
        if pos == end:
            print_path1(pos, st)
            return
        mark(maze, pos)
        for i in range(nxt, 4):  # 依次检查潜在探索方向
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1])  # 算出下一点
            if passable(maze, nextp):  # 遇到未探查点
                st.push((pos, i + 1))  # 原位置进栈
                pos, nxt = nextp, 0
                break
        else:
            if st.is_empty():
                break
            pos, nxt = st.pop()
    print("No path found.")  # 找不到路径


# end of maze_solver


if __name__ == "__main__":
#     print(maze_solver_rec(maze1, (1, 1), (18, 18)))
#     print(maze_solver1(maze1, (1,1), (18,18)))
#     print(maze_solver_queue(maze1, (1,1), (18,18)))
    print(maze_solver_queue1(maze1, (1, 1), (18, 18)))
