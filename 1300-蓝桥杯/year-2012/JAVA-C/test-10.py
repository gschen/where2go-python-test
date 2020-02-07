AB,BC,CD,DE,EA,EB,EC = map(float,input().split())
C1 = (AB+EB+EA)/2
C2 = (BC+EC+EB)/2
C3 = (DE+CD+EC)/2
S1 = (C1*(C1-AB)*(C1-EB)*(C1-EA))**(1/2)
S2 = (C2*(C2-BC)*(C2-EC)*(C2-EB))**(1/2)
S3 = (C3*(C3-DE)*(C3-CD)*(C3-EC))**(1/2)
S = S1+S2+S3
print(S)