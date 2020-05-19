#%% Imports
import numpy as np

# np.where() evalutes before condition
np.seterr(divide='ignore',invalid='ignore')

#%% Calculate the Entropy

def entropy(x,nbins=20):
    count, bin_edges  = np.histogram(x,nbins)
    p = count/len(x)
    H = -np.sum(np.where(p>0,p*np.log2(p),0))
    return H

# # Entropy for X:
# Hx = entropy(x)
#%% Calculate the joint entropy for X and Y:

def joint_entropy(x,y,nbins=20):
        count_xy, xedges, yedges = np.histogram2d(x,y,nbins)
        p_xy = count_xy/len(y)

        tmp = np.where(p_xy>0, p_xy*np.log2(p_xy),0)
        Hxy = -np.sum(np.sum(tmp))
        return Hxy

# # Example:
# Hxy = joint_entropy(x.reshape(-1,),y.reshape(-1,))

#%% Calculate the conditional Entropies

def conditional_entropy(x,y,nbins=20):
    count_xy,xedges,yedges = np.histogram2d(x,y,nbins)
    # x-values are rows
    # y-values are columns

    p_xy = count_xy/len(x)

    # Sum across all columns for each row
    p_x = np.sum(p_xy,axis=1)

    # Sum across all rows for each column
    p_y = np.sum(p_xy,axis=0)
    
    # Conditional Entropy for Rows:
    p_x = np.tile(p_x.reshape(-1,1), (1,nbins))
    tmp = np.where(p_xy>0,p_xy*np.log2(p_xy/p_x),0)
    Hyx_conditional = -np.sum(np.sum(tmp))

    # Conditional Entropy for Columns:
    p_y = np.tile(p_y, (nbins,1))
    tmp = np.where(p_xy>0,p_xy*np.log2(p_xy/p_y),0)
    Hxy_conditional = -np.sum(np.sum(tmp))

    return Hyx_conditional, Hxy_conditional

# Example: 
# Hyx_conditional, Hxy_conditional = conditional_entropy(x,y)


#%% Mututal Information
def mutual_information(x,y,nbins=20):
    Hx = entropy(x,nbins)
    Hy = entropy(y,nbins)
    Hxy = joint_entropy(x,y,nbins)
    MI = Hx+Hy-Hxy
    NMI = 2*MI/(Hx + Hy)
    return MI, NMI

# Example: 
# MI,NMI = mutual_information(x,y)

# print(f'I(X,Y) = H(X) + H(Y) - H(X,Y) = {Hx + Hy - Hxy:.4f}')
# print(f'I(X,Y) = H(X) - H(X|Y) = {Hx - Hxy_conditional:.4f}')
# print(f'I(X,Y) = H(Y) - H(Y|X) = {Hy - Hyx_conditional:.4f}')
# print(f"NMI(X,Y) = 2*I(X,Y)/(H(X)+H(Y)) = {2*(Hx + Hy - Hxy)/(Hx + Hy):.4f}")


#%% Old Functions

# def joint_entropy(x,y,nbins=20):
#         count_xy, xedges, yedges = np.histogram2d(x,y,nbins)
#         p_xy = count_xy/len(y)

#         tmp = np.empty((nbins,nbins))

#         for i in range(nbins):
#             for j in range(nbins):
#                 tmp[i,j]=p_xy[i,j]*np.log2(p_xy[i,j])
#         Hxy = -np.nansum(np.nansum(tmp))
#         return Hxy

# def conditional_entropy(x,y,nbins=20):
#     count_xy,xedges,yedges = np.histogram2d(x,y,nbins)
#     # x-values are rows
#     # y-values are columns

#     p_xy = count_xy/len(x)

#     # Sum across all columns for each row
#     p_x = np.sum(p_xy,axis=1)

#     # Sum across all rows for each column
#     p_y = np.sum(p_xy,axis=0)

#     # Conditional Entropy for Rows:
#     tmp = np.empty((nbins,nbins))

#     for i in range(nbins):
#         for j in range(nbins):
#             tmp[i,j] = p_xy[i,j]*np.log2(p_xy[i,j]/p_x[i])
#     Hyx_conditional = -np.nansum(np.nansum(tmp))

#     # Conditional Entropy for Columns:
#     tmp = np.empty((nbins,nbins))
#     for j in range(nbins):
#         for i in range(nbins):
#             tmp[i,j] = p_xy[i,j]*np.log2(p_xy[i,j]/p_y[j])
#     Hxy_conditional = -np.nansum(np.nansum(tmp))

#     return Hyx_conditional, Hxy_conditional


#%% Calculate the conditional frequency

# Division by zero!

# def conditional_frequency(x,y,nbins=20):
#     count_xy,xedges,yedges = np.histogram2d(x,y,nbins)
#     # x-values are rows
#     # y-values are columns

#     # Sum across all columns for each row
#     count_x = np.sum(count_xy,axis=1)
    
#     # Sum across all rows for each column
#     count_y = np.sum(count_xy,axis=0)

#     # Conditional Relative Frequency for Rows:
#     count_x = np.tile(count_x.reshape(-1,1), (1,nbins))
#     p_yx_cond = count_xy/count_x

#     # Conditional Relative Frequency for Columns:
#     count_y = np.tile(count_y, (nbins,1))
#     p_xy_cond = count_xy/count_y

#     return p_yx_cond,p_xy_cond

# # Example:
# p_yx_cond,p_xy_cond = conditional_frequency(x,y)
