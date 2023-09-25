

from datetime import datetime
a,m,d,h,mi,s=map(int,input("quando foi precisamente esse evento: ").split())

momento= datetime(a,m,d,h,mi,s)

hj= datetime.now()


difenca= hj-momento

print(f"esse envento faz precisamente {difenca}")
