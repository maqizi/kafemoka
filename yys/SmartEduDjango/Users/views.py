from django.contrib.auth.models import User
from rest_framework.authtoken.views import APIView,AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from Users.models import Lesson
from Users.models import Share
import time
import os
from langchain_community.document_loaders import TextLoader,PyPDFLoader,UnstructuredWordDocumentLoader,WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter,RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain_chroma import Chroma
from uuid import uuid4
import bs4
from django.core.files.storage import default_storage






# 用户注册
class Register(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            resp = {
                'status':False,
                'data':'用户名已被注册'
            }
        else:
            user = User.objects.create_user(username=username,password=password)
            token, created = Token.objects.get_or_create(user=user)
            resp = {
                'status':True,
                'token': token.key,
                'user_id': user.pk,
                'user_name': user.username,
            }
        return Response(resp)
    
# 用户登录
class Login(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'status':True,
            'token': token.key,
            'user_id': user.pk,
            'user_name':user.username,
        })
    
# 用户删除
class Delect(APIView): 
    def post(self, request, *args, **kwargs):
        userid = request.data.get('userid')
        try:
            user = User.objects.all()
            # user = User.objects.get(id=userid)
            user.delete()
            resp = {
                'status':'用户删除成功！',
            }
        except User.DoesNotExist:
            resp = {
                'status':'用户不存在！',
            }
        return Response(resp)

        
class Insertlesson(APIView):
    def post(self, request, *args, **kwargs):
        UserName = request.data.get('UserName')
        LessonName = request.data.get('LessonName')
        Navigation = request.data.get('Navigation')
        Lessoncontent = request.data.get('Lessoncontent')
        test1 = Lesson(UserName=UserName,
                       LessonName=LessonName,
                       Navigation=Navigation,
                       Lessoncontent=Lessoncontent,
                       )
        test1.save()
        resp = {
                'status':True,
        }
        return Response(resp)
    
class GetLessonDatas(APIView):
    def get(self, request):
        LessonDatas = Lesson.objects.all().values()
        return Response(LessonDatas)
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        ownLessonDatas = Lesson.objects.filter(UserName=username).values('id','UserName','LessonName')
        ShareDatas_id = Share.objects.filter(Sharer=username).values_list('Lessonid')
        shareLessonDatas = Lesson.objects.filter(id__in=ShareDatas_id).values('id','UserName','LessonName')
        querysets = ownLessonDatas | shareLessonDatas
        return Response(querysets)
    

class GetLessonData(APIView):
    def post(self, request, *args, **kwargs):
        lid = request.data.get('id')
        LessonDatas = Lesson.objects.filter(id=lid).values()
        return Response(LessonDatas)
       
    
class DelLessonData(APIView):
    def post(self, request, *args, **kwargs):
        lid = request.data.get('id')
        Lesson.objects.get(id=lid).delete()
        Share.objects.filter(Lessonid=lid).delete()
        return Response(lid)

class ResetLessonData(APIView):
    def post(self, request, *args, **kwargs):
        lid = request.data.get('id')
        # UserName = request.data.get('UserName')
        LessonName = request.data.get('LessonName')
        Navigation = request.data.get('Navigation')
        Lessoncontent = request.data.get('Lessoncontent')
        test1 = Lesson.objects.filter(id=lid)

        test1.update(
                    # UserName=UserName,
                    LessonName=LessonName,
                    Navigation=Navigation,
                    Lessoncontent=Lessoncontent,
                    )
        
        resp = {
                'status':True,
        }
        return Response(resp)
    
class Insertshare(APIView):
    def post(self, request, *args, **kwargs):
        Author = request.data.get('Author')
        Sharer = request.data.get('Sharer')
        Privilege = request.data.get('Privilege')
        Lessonid = request.data.get('Lessonid')
        if Author != Sharer and User.objects.filter(username=Sharer).exists():
            test1 = Share(Author=Author,
                        Sharer=Sharer,
                        Privilege=Privilege,
                        Lessonid=Lessonid,
                        )
            test1.save()
            resp = {
                    'status':True,
            }
        else:
            resp = {
                'status':False,
                'data':'用户名无效'
            }
        return Response(resp)


class Getshare(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        ShareDatas_id = Share.objects.filter(Sharer=username).values_list('Lessonid')
        result_data = Lesson.objects.filter(id__in=ShareDatas_id).values()
        return Response(result_data)
    
    #start txt文件加载  yes    
class GetTextSplitterDocuments(APIView):
    def get(self, request):
        #用langchain.document_loaders中TextLoader 模块进行加载 error:error loader gbk Unicode 解码错误
        #指定了encoding 为utf-8 即解码成功。
        loader = TextLoader("data/shudaonan.txt",encoding='utf-8')  
        documents = loader.load()
        # 文档分割   from langchain.text_splitter import CharacterTextSplitter      
        # 创建拆分器   
        text_splitter = CharacterTextSplitter(chunk_size=250, chunk_overlap=0)   
        # 拆分文档   
        documents = text_splitter.split_documents(documents)   
        model_name = "E:\\yys\\SmartEduDjango\\moka_ai\\m3e_base"
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': True}
        embedding = HuggingFaceBgeEmbeddings(
                model_name=model_name,
                model_kwargs=model_kwargs,
                encode_kwargs=encode_kwargs,
                query_instruction="为文本生成向量表示用于文本检索"
         )
        uuids = [str(uuid4()) for _ in range(len(documents))]

        # load data to Chroma db
        #db = Chroma.from_documents(documents, embedding,collection_name="lab", persist_directory="./shudaonan1_db")
        db=Chroma(embedding_function=embedding,collection_name="labc1",persist_directory="./shudaonan1_db")
        #db.add_documents(documents=documents, ids=uuids)
        retriever = db.as_retriever()
        # similarity search
        question="蜀道难是谁写的？"
        docs=retriever.invoke(question)
        str1=[]
        for doc in docs:
            for d in doc:
             if d[0]=="page_content":
              str1.append(d[1])
        return Response(str1)
    
    # def post(self, request, *args, **kwargs):
    #     username = request.data.get('username')
    #     ownLessonDatas = Lesson.objects.filter(UserName=username).values('id','UserName','LessonName')
    #     ShareDatas_id = Share.objects.filter(Sharer=username).values_list('Lessonid')
    #     shareLessonDatas = Lesson.objects.filter(id__in=ShareDatas_id).values('id','UserName','LessonName')
    #     querysets = ownLessonDatas | shareLessonDatas
    #     return Response(querysets)
    #end
    #start test -上传各种文件 -目前测试过 txt docx pdf文件上传并且保存到data文件中成功！   
class uploadsFlie(APIView):
    def post(self, request, *args, **kwargs):
        db_name = request.data.get('db_name')
        source_file=request.FILES.get('source')
        #定义存放的名称
        source_file_temp_save_path=str(time.time())+source_file.name
        #保存文件到指定目录 首先获得当前脚本所在的目录，再将该目录转换为绝对路径
        #basedir=os.path.abspath(os.path.dirname(__file__))
        basedir="E:\\yys\\SmartEduDjango\\data\\ChineseSubject"
        filepath=os.path.join(basedir,'ms',source_file_temp_save_path) #ms是存放文件的子目录
        # 确保路径存在
        dir=os.path.dirname(filepath)
        if not os.path.exists(dir):
            os.makedirs(dir)
        with default_storage.open(filepath, 'wb+') as destination:
            for chunk in source_file.chunks():
                destination.write(chunk)
        print(source_file_temp_save_path)
        return Response(source_file_temp_save_path)
    #end
class createdb(APIView):
    def post(self, request, *args, **kwargs):
        db_name = request.data.get('db_name')
        source_file=request.FILES.get('source')
        #定义存放的名称
        source_file_temp_save_path=str(time.time())+source_file.name
        #保存文件到指定目录 首先获得当前脚本所在的目录，再将该目录转换为绝对路径
        #basedir=os.path.abspath(os.path.dirname(__file__))
        basedir="E:\\yys\\SmartEduDjango\\data\\ChineseSubject"
        filepath=os.path.join(basedir,'ms',source_file_temp_save_path) #ms是存放文件的子目录
        # 确保路径存在
        dir=os.path.dirname(filepath)
        if not os.path.exists(dir):
            os.makedirs(dir)
        with default_storage.open(filepath, 'wb+') as destination:
            for chunk in source_file.chunks():
                destination.write(chunk)
        #source_file_temp_save_path 为存放的名称 获取该文件类型，加载文件
        #指定Chroma向量数据库 本地存储地址
        persist_directory='./db/ChineseSubject/ms/'+db_name
        #获取上传的文件的文件拓展名 根据拓展名决定使用哪一个loader
        extension=filepath.split(".")[-1]
        loader=None
        if extension == 'txt':
            loader=TextLoader(filepath,encoding='utf-8')
        if extension == 'pdf':
            loader=PyPDFLoader(filepath)
        if extension == 'docx':
            loader=UnstructuredWordDocumentLoader(filepath) 
        #web success 但就是需要寻找网页的内容class 爬取标签
        # loader = WebBaseLoader(
        # web_paths=("https://www.baike.com/wikiid/1885700839433549406",),
        # bs_kwargs=dict(
        #   parse_only=bs4.SoupStrainer(
        #     class_=("baike-render-wrapper_ea777","baike-render-paragraph")
        # )
        # ),
        # )
        # docs = loader.lazy_load()
        # docs=loader.load()
        #在处理pdf大文档的时候，可以使用lazyload
        pages = []
        for doc in loader.load():
          pages.append(doc)
        
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=0,
        separators=[
        "。",
        "\n\n",
        " ",
        ".",
        ",",
        "",
    ],)
        
        splits=text_splitter.split_documents(pages)
        print(splits)
        model_name = "E:\\yys\\SmartEduDjango\\moka_ai\\m3e_base"
        model_kwargs = {'device': 'cuda'}
        encode_kwargs = {'normalize_embeddings': True}
        embeddings = HuggingFaceBgeEmbeddings(
                model_name=model_name,
                model_kwargs=model_kwargs,
                encode_kwargs=encode_kwargs,
                query_instruction="为文本生成向量表示用于文本检索"
        )
        uuids = [str(uuid4()) for _ in range(len(splits))]
        print(uuids)
        # load data to Chroma db-baiqiuen  altogether ：cms cms100size cmsoneh
        db = Chroma(collection_name="cmsoneh",embedding_function=embeddings,persist_directory=persist_directory)
        #不知道为何每次db 如果加入向量数据库，用全局 似乎容易出错。
        db.add_documents(documents=splits, ids=uuids)

        # similarity search
        question="孟子三章？"
        #docs = db.similarity_search(question, k=5, filter={"source": "E:\\yys\\SmartEduDjango\\data\\ChineseSubject\\ms\\1730098512.8387148shudaonan.pdf"},)
        docs = db.similarity_search(question, k=5)
        print(docs)
        str1=[]
        # for doc in docs:
        #     for d in doc:
        #      if d[0]=="page_content":
        #       str1.append(d[1])
        return Response(docs)
    #end
class retrieve(APIView):
    def post(self, request, *args, **kwargs):
        db_name = request.data.get('db_name')
        query = request.data.get('query')
        # similarity search
        #question=query
        persist_directory='./db/ChineseSubject/ms/'+'cmsoneh'  
        model_name = "E:\\yys\\SmartEduDjango\\moka_ai\\m3e_base"
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': True}
        embeddings = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs,
        query_instruction="为文本生成向量表示用于文本检索"
     )
        db = Chroma(embedding_function=embeddings,persist_directory=persist_directory)   
        docs = db.similarity_search(query, k=5)
        
        str1=[]
        for doc in docs:
            for d in doc:
             if d[0]=="page_content":
              str1.append(d[1])
        return Response(str1)
    #end

