from include import *




class ensemble:
    
    def __init__(self):
        
        self.eig_vals = None
    
    def eig_vals_hist(self, **kwargs):
        
        fig, ax = plt.subplots(figsize=(18, 6))
        sns.distplot(self.eig_vals, ax=ax, **kwargs)
        return fig
    
    def eig_gaps_hist(self, **kwargs):
        
        fig, ax = plt.subplots(figsize=(18, 6))
        sns.distplot(self.eig_gaps, ax=ax, **kwargs)
        return fig
    
    def calc_eig_vals(self):
        
        if self.size[0] != self.size[1]:
            print('not a square matrix! eiganvalues are not defined')
        else:
            self.eig_vals = eigvalsh(self.matrix)
            self.eig_gaps = np.diff(self.eig_vals)
            
            
    
class GOE(ensemble):
    
    def __init__(self, n):
        
        if n <= 0:
            raise ValueError('size must be positive')
        self.size     = (n, n)
        self.matrix   = np.random.randn(n * n).reshape(n, n)
        self.matrix   = (self.matrix.T + self.matrix) / 2
        self.calc_eig_vals()
        
    
class GUE(ensemble):
    
    def __init__(self, n):
        
        if n <= 0:
            raise ValueError('size must be positive')
        self.size     = (n, n)
        A             = np.random.randn(n * n).reshape(n, n) + 1j * np.random.randn(n * n).reshape(n, n)
        self.matrix   = (A.T + A) / 2
        self.calc_eig_vals()
    
    

    
    
    
        
        
        