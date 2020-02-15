import os
from collections import deque

# depth-first traversal
def depthFirstTraversal(path):
    buffer = []
    buffer.append(path)

    while len(buffer) != 0:
        TempPath = buffer.pop()
        fileList = os.listdir(TempPath)

        for file in fileList:
            fileAbsPath = os.path.join(TempPath, file)

            if os.path.isdir(fileAbsPath):
                print("Directory: %s" % fileAbsPath)
                buffer.append(fileAbsPath)
            else:
                print("Common file: %s" % file)

# breadth-first traversal
def breadthFirstTraversal(path):
    q = deque()
    q.append(path)

    while len(q) != 0:
        TempPath = q.popleft()
        fileList = os.listdir(TempPath)

        for file in fileList:
            fileAbsPath = os.path.join(TempPath, file)

            if os.path.isdir(fileAbsPath):
                print("Directory: %s" % fileAbsPath)
                q.append(fileAbsPath)
            else:
                print("Common file: %s" % file)

# recursion
def getAllFiles(path, sp=""):
    fileList = os.listdir(path)
    sp += "   "
    for file in fileList:
        fileAbsPath = os.path.join(path, file)

        if os.path.isdir(fileAbsPath):
            print(sp + "Directory: %s" % fileAbsPath)
            getAllFiles(fileAbsPath, sp)
        else:
            print(sp + "Common file: %s" % file)