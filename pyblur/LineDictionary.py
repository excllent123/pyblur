class LineDictionary:
    def __init__(self):
        self.lines = {}
        self.Create3x3Lines()
        self.Create5x5Lines()
        self.Create7x7Lines()
        self.Create9x9Lines()
        self.Create11x11Lines()
        return
    
    def Create3x3Lines(self):
        lines = {}
        # 4
        lines[0]      = [1,0,1,2]
        lines[45]     = [2,0,0,2]
        lines[90]     = [0,1,2,1]
        lines[135]    = [0,0,2,2]
        self.lines[3] = lines
        return
    
    def Create5x5Lines(self):
        lines = {}        
        # 8
        lines[0]      = [2,0,2,4]
        lines[22.5]   = [3,0,1,4]
        lines[45]     = [0,4,4,0]
        lines[67.5]   = [0,3,4,1]
        lines[90]     = [0,2,4,2]
        lines[112.5]  = [0,1,4,3]
        lines[135]    = [0,0,4,4]
        lines[157.5]  = [1,0,3,4]
        self.lines[5] = lines
        return
        
    def Create7x7Lines(self):
        lines = {}
        # 12
        lines[0]      = [3,0,3,6]
        lines[15]     = [4,0,2,6]
        lines[30]     = [5,0,1,6]
        lines[45]     = [6,0,0,6]
        lines[60]     = [6,1,0,5]
        lines[75]     = [6,2,0,4]
        lines[90]     = [0,3,6,3]
        lines[105]    = [0,2,6,4]
        lines[120]    = [0,1,6,5]
        lines[135]    = [0,0,6,6]
        lines[150]    = [1,0,5,6]
        lines[165]    = [2,0,4,6]
        self.lines[7] = lines 
        return
    
    def Create9x9Lines(self):
        lines = {}
        # 16
        lines[0]      = [4,0,4,8]
        lines[11.25]  = [5,0,3,8]
        lines[22.5]   = [6,0,2,8]
        lines[33.75]  = [7,0,1,8]
        lines[45]     = [8,0,0,8]
        lines[56.25]  = [8,1,0,7]
        lines[67.5]   = [8,2,0,6]
        lines[78.75]  = [8,3,0,5]
        lines[90]     = [8,4,0,4]
        lines[101.25] = [0,3,8,5]
        lines[112.5]  = [0,2,8,6]
        lines[123.75] = [0,1,8,7]
        lines[135]    = [0,0,8,8]
        lines[146.25] = [1,0,7,8]
        lines[157.5]  = [2,0,6,8]
        lines[168.75] = [3,0,5,8]
        self.lines[9] = lines
        return

    def Create11x11Lines(self):
        lines = {}
        # 20 
        lines[0]   =  [5,0,5,10]
        lines[9]   =  [6,0,4,10]
        lines[18]  =  [7,0,3,10]
        lines[27]  =  [8,0,2,10]
        lines[36]  =  [9,0,1,10]
        lines[45]  =  [10,0,0,10]
        lines[54]  =  [10,1,0,9]
        lines[63]  =  [10,2,0,8]
        lines[72]  =  [10,3,0,7]
        lines[81]  =  [10,4,0,6]
        lines[90]  =  [10,5,0,5]
        lines[99]  =  [0,4,10,6]
        lines[108] =  [0,3,10,7]
        lines[117] =  [0,2,10,8]
        lines[126] =  [0,1,10,9]
        lines[135] =  [0,0,10,10]
        lines[144] =  [1,0,9,10]
        lines[153] =  [2,0,8,10]
        lines[162] =  [3,0,7,10]
        lines[171] =  [4,0,6,10]
        self.lines[11] = lines
        return

    def CreateNxNLines(N):
        num = math.floor(N/2) * 4
        pass