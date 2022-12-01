
# 开发文档

### 创建虚拟环境
```
python3 -m venv ./.venvs/mypro
```

### 使用虚拟环境
```
source ~/.venvs/mypro/bin/activate
```

### 创建 django 模块
```
django-admin startproject capmanager
```

### 进入项目目录
```
cd capservice
```

### 创建 cap 模块
```
python manage.py startapp cap
```

### 同步数据库结构，指定 cap 模块
```
# 收集需要同步的变更信息
python manage.py makemigrations cap

# 执行实际的同步逻辑
python manage.py migrate
```

### 创建管理员用户
```
python manage.py createsuperuser
```
# 部署文档

### 收集 requirements
```
pip freeze > requirements.txt
```
### 从 requirements 中安装依赖
```
pip install -r requirements.txt
```
