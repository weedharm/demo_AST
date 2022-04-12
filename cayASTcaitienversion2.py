#file python giúp chúng ta có thể trích xuất nút cây cú pháp trừu tượng từ tập source code SoftwareDefectPrediction


import pandas as pd
import csv
import javalang
import os
#folder chứa source file
folder_source_code ='camel-camel-1.2.0'
#đọc data
software_metric='camel-1.2.csv'
data = pd.read_csv(software_metric)
nhan = data['bug']
#hàm tìm ra 1 file giữa 1 đống thư mục
def find_files(filename, search_path):
   result = []
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result
### tạo nút AST node
FormalParameter='FormalParameter'
BasicType='BasicType'
PackageDeclaration='PackageDeclaration'
InterfaceDeclaration='InterfaceDeclaration'
CatchClauseParameter='CatchClauseParameter'
ClassDeclaration='ClassDeclaration'
MethodInvocation='MethodInvocation'
SuperMethodInvocation='SuperMethodInvocation'
MemberReference='MemberReference'
SuperMemberReference='SuperMemberReference'
ConstructorDeclaration='ConstructorDeclaration'
ReferenceType='ReferenceType'
MethodDeclaration='MethodDeclaration'
VariableDeclarator='VariableDeclarator'
IfStatement='IfStatement'
WhileStatement ='WhileStatement'
DoStatement='DoStatement'
ForStatement='ForStatement'
AssertStatement='AssertStatement'
BreakStatement='BreakStatement'
ContinueStatement='ContinueStatement'
ReturnStatement='ReturnStatement'
ThrowStatement='ThrowStatement'
SynchronizedStatement='SynchronizedStatement'
TryStatement='TryStatement'
SwitchStatement ='SwitchStatement'
BlockStatement='BlockStatement'
StatementExpression ='StatementExpression'
TryResource='TryResource'
CatchClause='CatchClause'
CatchClauseParameter='CatchClauseParameter'
SwitchStatementCase='SwitchStatementCase'
ForControl ='ForControl'
EnhancedForControl='EnhancedForControl'

###
# aa là số file đã mất mát bb là số file còn ở thực tại
aa=0
bb=0
b=[]#b là đường dẫn tuyệt đối mà chúng ta cần tìm
#chúng ta cần tạo ra 1 file csv mới, file csv này đã loại bỏ đi các file java không còn tồn tại trong source code
file_csv_moi = []
with open(software_metric) as f:
    file_software_metric = csv.reader(f)
    for row in file_software_metric:
        motcaigido=[] #lưu lại cái bản ghi mới
        a=''# mỗi lần for lại a sẽ bằng '' ,khá dễ hiểu
        #bỏ cột name
        if row[0] == 'name':
            continue
        #tách đường dẫn
        i= row[0].split('.')
        #lấy file cuối cùng
        file = i[len(i) - 1]
        #nhét đuôi .java vào
        file = file + '.java'
        #tìm kiếm file trong thư mục
        duong_dan = find_files(file, folder_source_code)
        # print(duong_dan)
        #một số file đã bị xóa đường dẫn sẽ bị = [] sẽ bỏ file đó đi
        if duong_dan == []:
            aa+=1
        else:
            bb+=1
            duong_dan_da_tach = duong_dan[0].split('\\')
            #chuyển đổi dạng tìm được sang dạng file tuyệt đối
            for j in range(len(duong_dan_da_tach)):
                if (j == len(duong_dan_da_tach) - 1):
                    a = a + duong_dan_da_tach[j]
                else:
                    a = a + duong_dan_da_tach[j] + '/'
            b.append(a)
            for abcd in row:
                motcaigido.append(abcd)
            file_csv_moi.append(motcaigido)



file_csv=[]
for n in b:
    # programfile=open(n,encoding='utf-8')
    programfile=open(n)
    tree = javalang.parse.parse(programfile.read())
    allnode = []
    for path, node in tree:

        e = str(node)

        f = e.split("(")[0]
        # print(b)
        if (f == FormalParameter):
            allnode.append(FormalParameter)
        elif (f == BasicType):
            allnode.append(BasicType)
        elif (f == PackageDeclaration):
            allnode.append(PackageDeclaration)
        elif (f == InterfaceDeclaration):
            allnode.append(InterfaceDeclaration)
        elif (f == CatchClauseParameter):
            allnode.append(CatchClauseParameter)
        elif (f == ClassDeclaration):
            allnode.append(ClassDeclaration)
        elif (f == MethodInvocation):
            allnode.append(MethodInvocation)
        elif (f == SuperMethodInvocation):
            allnode.append(SuperMethodInvocation)
        elif (f == MemberReference):
            allnode.append(MemberReference)
        elif (f == SuperMemberReference):
            allnode.append(SuperMemberReference)
        elif (f == ConstructorDeclaration):
            allnode.append(ConstructorDeclaration)
        elif (f == ReferenceType):
            allnode.append(ReferenceType)
        elif (f == MethodDeclaration):
            allnode.append(MethodDeclaration)
        elif (f == VariableDeclarator):
            allnode.append(VariableDeclarator)
        elif (f == IfStatement):
            allnode.append(IfStatement)
        elif (f == WhileStatement):
            allnode.append(WhileStatement)
        elif (f == DoStatement):
            allnode.append(DoStatement)
        elif (f == ForStatement):
            allnode.append(ForStatement)
        elif (f == AssertStatement):
            allnode.append(AssertStatement)
        elif (f == BreakStatement):
            allnode.append(BreakStatement)
        elif (f == ContinueStatement):
            allnode.append(ContinueStatement)
        elif (f == ReturnStatement):
            allnode.append(ReturnStatement)
        elif (f == ThrowStatement):
            allnode.append(ThrowStatement)
        elif (f == SynchronizedStatement):
            allnode.append(SynchronizedStatement)
        elif (f == TryStatement):
            allnode.append(TryStatement)
        elif (f == SwitchStatement):
            allnode.append(SwitchStatement)
        elif (f == BlockStatement):
            allnode.append(BlockStatement)
        elif (f == StatementExpression):
            allnode.append(StatementExpression)
        elif (f == TryResource):
            allnode.append(TryResource)
        elif (f == CatchClause):
            allnode.append(CatchClause)
        elif (f == CatchClauseParameter):
            allnode.append(CatchClauseParameter)
        elif (f == SwitchStatementCase):
            allnode.append(SwitchStatementCase)
        elif (f == ForControl):
            allnode.append(ForControl)
        elif (f == EnhancedForControl):
            allnode.append(EnhancedForControl)
    file_csv.append(allnode)
    programfile.close()

tinh_max=[]
for hiu in file_csv:
    tinh_max.append(len(hiu))
do_rong_file_csv = max(tinh_max)
file_csv_final = []
y=0
for hiu in file_csv:
    h=[]
    so_phan_tu_khong= do_rong_file_csv-len(hiu)
    if so_phan_tu_khong>0:
        for g in hiu:
            h.append(g)
        for k in range(so_phan_tu_khong):
            h.append('0')
    else:
        h=hiu
    h.append(nhan[y])
    y+=1
    file_csv_final.append(h)

with open('jedit3.2AST.csv','w',newline='') as f:
    writer = csv.writer(f)
    for z in file_csv_final:
        writer.writerow(z)
with open('jedit3.2metric.csv','w',newline='')as q:
    nhap = csv.writer(q)
    for x in file_csv_moi:
        nhap.writerow(x)

print('số file java không còn tồn tại',aa)
print('số file java còn tồn tại',bb)