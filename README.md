# ��Ŀ����
ʹ��python��д��java SpringBoot��Ŀ����������

������entity��service��controller��Ļ�������

��ʡ�ظ��Ĵ����д

���Զ���ÿ����Ĵ�������λ��

ͨ��config.toml����������

python�汾:3.10

# ����ԭ��
�����ݿ��ȡ��ṹ������ʵ������ͨ��ʵ��������service���controller��Ĵ���

# ����˵��
```angular2html
# config.toml

[generate]
projectLocalPath = "" # java��Ŀ��Ŀ¼·��

isGenerateController = true # �Ƿ�����controller����������� Ĭ��Ϊtrue
isGenerateMapper = true # �Ƿ�����mapper����� Ĭ��Ϊtrue
isGenerateService = true # �Ƿ�����service����� Ĭ��Ϊtrue
isGenerateEntity = true # �Ƿ�����entity��ʵ������� Ĭ��Ϊtrue

# ������Զ�����ȷ����Ŀ�ṹ���ɶ�Ӧ��Ĵ��룬�����Ҫ�Զ������ɴ����·���������������ã����Զ�����Ӽ���
ControllerGenerateLocalPath = "" # ���controller��������������ɵı���·��
ServiceGenerateLocalPath = "" # ���service��������ɵı���·��
EntityGenerateLocalPath = "" # ���entity��ʵ����������ɵı���·��

# �ų��б� �����ɹ����в�ϣ�����������ɻ��޸��ض��ļ����б� Ĭ��Ϊ���б� ��,�ŷָ�
ExclusionList = []

[database]
url = "localhost" # ���ݿ�url
port = 3306
username = "" # ���ݿ��û���
password = "" # ���ݿ�����
dbname = "" # ���ݿ�����

# ���ݿ�����תΪjava���͵�ӳ���
[convert]

```

# ��Ҫ����
```angular2html
toml==0.10.2
Jinja2==3.1.4
PyMySQL==1.1.1
```