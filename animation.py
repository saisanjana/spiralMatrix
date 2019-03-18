# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:54:11 2019
representing spiral matrix  of size 4*4
@author: Sanjana
"""
import turtle
turtle.bgcolor("black")
seurat=turtle.Turtle()
width=5
height=7
dot_distance=25
seurat.setpos(-250,250)
def spiral(n,m):
    k=0
    l=0
    f=0
    seurat.color("white")
    '''
    k is the index of starting row
    l is the index of starting coloumn
    '''
    while(k<m and l<n):
        if(f==1):
            seurat.right(90)
        #first print the first row, so
        #row index is constant and col index
        #changes
        for i in range(l,n):
           seurat.forward(dot_distance)
            # print(a[k][i],end=" ")
        
        k=k+1
        f=1
        
        seurat.right(90)
        
        #sholud print last coloumn
        #coloumn should be fixed
        for i in range(k,m):
           seurat.forward(dot_distance)
            # print(a[i][n-1],end=" ")
        
        #sholud print last row,so shift l to seconf last
        #coloumn
        n=n-1
        seurat.right(90)
        
        if(k<m): 
            for i in range(n-1,l-1,-1):                
                seurat.forward(dot_distance)
                # print(a[m-1][i],end=" ")
            
            m=m-1
            seurat.right(90)
        if(l<n):
            #priniting the first col from the remaining col
            for i in range(m-1,k-1,-1):
                seurat.forward(dot_distance)
                #print(a[i][l],end=" ")
            l=l+1
 

    
spiral(20,20)
turtle.done()
