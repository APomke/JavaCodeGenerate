# ��Ŀ����
ʹ��python��д��java SpringBoot��Ŀ����������

������entity��service��controller��Ļ�������

��ʡ�ظ��Ĵ����д

ͨ��config.toml����������

python�汾:3.10

# ����ԭ��
�����ݿ��ȡ��ṹ������ʵ������ͨ��ʵ��������service���controller��Ĵ���

# ����˵��
```angular2html
# config.toml

[generate]
projectLocalPath = "" # java��Ŀ��Ŀ¼·��

isGenerateController = true # �Ƿ�����controller�����������
isGenerateService = true # �Ƿ�����service�����
isGenerateEntity = true # �Ƿ�����entity��ʵ�������

# �����Ҫ�Զ������ɴ����·���������������ã����Զ�����Ӽ���
ControllerGenerateLocalPath = "" # ���controller��������������ɵı���·��
ServiceGenerateLocalPath = "" # ���service��������ɵı���·��
EntityGenerateLocalPath = "" # ���entity��ʵ����������ɵı���·��


[database]
url = "" # ���ݿ�url
port = 3306
username = "" # ���ݿ��û���
password = "" # ���ݿ�����
dbname = "" # ���ݿ�����
```
