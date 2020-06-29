## 开发工具
vscode
### 在setting.json中更改python安装目录
```
python.pythonPath 
```
## 开发环境配置
安装虚拟环境
```
pip install virtualenv
```
指定当前目录为虚拟环境
```
virtualenv 目录地址
```
安装rest api支持
```
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

// vscode 需要安装
pip install pylint-django
```

## 生成数据库迁移文件
``` python
python manage.py makemigrations
```

## 生成数据库
``` python
python manage.py migrate
```
