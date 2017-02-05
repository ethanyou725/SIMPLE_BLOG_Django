# SIMPLE_BLOG_Django

##### 在views.py 里使用class-based-view (Class Example_view(view): pass) 替代了所有的类试图,对应的urls.py,views.Example_View.as_view()
##### mysite_uwsgi.ini uwsgi配置
##### 项目部署 youzhigang.pythonanywhere.com
##### 整体结构还是很简单的

##
## 2017.1 切换到 restful 分支
#### 改版了,抛弃了固有的模式,采用了django rest framework ,视图函数也越写越简单,最新版使用viewset的只剩下30~40行代码
#### 后台django之提供接口,一共两个,一个是返回所有的article列表,一个是根据id返回article的content
#### 前台是react写的,yarn+webpack,现在还在坑里,还有许多可以完善的地方.


## 2017.2
#### 新增vue全家桶版本(vue2 + vue-router + vuex),
> python3 manage.py runserver
> localhost:8000/vue  
> localhost:8000/react 
#### 内容一样，工具不同