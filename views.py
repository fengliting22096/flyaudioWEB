
from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse
from test1.models import Blog
from model_test import settings
from test1.models import Pictest
# Create your views here.



def image(request):
        return render(request, 'static/image1.html')

    def index(request):

            # 1、加载模板文件
                # temp = loader.get_template('booktest/index.html')
                    #
                        # #2、定义模板上下文,给模板传送数据
                            # context =(request, {})
                                #
                                    #
                                        #
                                            # #3、模板渲染，产生一个修改后的HTML文件
                                                # resquest_html = temp.render(context)
                                                    # print('1111111111')
                                                        #
                                                            #
                                                                # return HttpResponse(resquest_html)
                                                                    return render(request, 'booktest/index.html', { })



                                                                def template_var(request):

                                                                        my_dict = {'sex': 'boy'}
                                                                            my_list = [1, 2, 3, 4]

                                                                                name = Blog.objects.all()

                                                                                    context = {'my_dict': my_dict, 'my_list': my_list, 'name': name}

                                                                                        return render(request, 'var/template_var.html', context)


                                                                                    def filters(request):
                                                                                            my_dict = {'sex': 'boy'}
                                                                                                my_list = [1, 2, 3, 4]

                                                                                                    name = Blog.objects.all()

                                                                                                        context = {'my_dict': my_dict, 'my_list': my_list, 'name': name}
                                                                                                            return render(request, 'var/filters.html', context)

                                                                                                        # 继承父类模板


                                                                                                        def inherit(request):

                                                                                                                return render(request, 'base/child.html')


                                                                                                            # 反向解析url
                                                                                                            #原理：在主url.py对应的app备注namespace，然后在app的url备注name属性，在views中坐以下的格式即可
                                                                                                            from django.urls import reverse
                                                                                                            def rever(request):
                                                                                                                    return render(request, 'reverse.html')
                                                                                                                def rend(request):

                                                                                                                        url = reverse('test1:index')
                                                                                                                            return redirect(url)


                                                                                                                        def upload(request):
                                                                                                                                return render(request, 'admin/uptupic.html')

                                                                                                                            def upload_pic(request):
                                                                                                                                    #获取上传的图片
                                                                                                                                        pic = request.FILES['pic']


                                                                                                                                            #创建一个文件
                                                                                                                                                save_file = '%s/png/%s'%(settings.MEDIA_ROOT, pic.name)
                                                                                                                                                    with open(save_file, 'wb') as f:

                                                                                                                                                                #获取上传的文件内容并写入新建的文件中
                                                                                                                                                                        for connect in pic.chunks():
                                                                                                                                                                                        f.write(connect)
                                                                                                                                                                                            #上传到数据库
                                                                                                                                                                                                Pictest.objects.create(p_img='png/%s'%pic.name)
                                                                                                                                                                                                    #返回
                                                                                                                                                                                                        return HttpResponse('ok')

#首次更新py文件
                                                                                                                                                                                                  
