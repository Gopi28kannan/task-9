data=['a','b','10','501','22','37','100','999','87','351','word']
for i in data:
          k=lambda x: x.isnumeric()
          if k(i) == True:
                    print(i," its integer")
          else:
                    print(i,"its string")
          
