<template>
<el-container style="height: 700px; border: 1px solid #eee">

    <el-header style="text-align: right; font-size: 18px">
		<el-button icon="el-icon-coin"  @click="saveedu()">保存</el-button>
		<el-button icon="el-icon-user" circle ></el-button>
		
    </el-header>
 

  <el-container>
	<el-aside width="200px" style="background-color: rgb(238, 241, 246)" id="Navigation">
		<el-row class="tac">
		  <el-col :span="24">
		    <h5>导航栏</h5>
		    <el-menu class="el-menu-vertical-demo" background-color="#fff6f6" text-color="#000000">
			  <el-menu-item index="1">
			    <i class="el-icon-menu"></i>
			    <span slot="title">教材分析</span>
			  </el-menu-item>
		      <el-menu-item index="2">
		        <i class="el-icon-menu"></i>
		        <span slot="title">学情分析</span>
		      </el-menu-item>
					<el-menu-item index="3">
					  <i class="el-icon-menu"></i>
					  <span slot="title">教学目标</span>
					</el-menu-item>
					<el-menu-item index="4">
					  <i class="el-icon-menu"></i>
					  <span slot="title">教学重点</span>
					</el-menu-item>
					<el-menu-item index="5">
					  <i class="el-icon-menu"></i>
					  <span slot="title">教学过程</span>
					</el-menu-item>
					<el-menu-item index="6">
					  <i class="el-icon-menu"></i>
					  <span slot="title">学习评价</span>
					</el-menu-item>
		      
		    </el-menu>
		  </el-col>
		</el-row>

	</el-aside>
		
    <el-main style="background-color: rgb(255, 255, 255)" id="Lessoncontent">
		
		<el-card class="box-card" id = "LessonName">
			<div contenteditable="true">教案名称</div>
		</el-card>

		<el-card class="box-card" id = "Lessoncontent">
			<!-- <div contenteditable="true">教案内容</div> -->
			<!-- <iframe name="embed_readwrite" 
				src="http://127.0.0.1:9001/p/test1?showControls=true&showChat=true&showLineNumbers=true&useMonospaceFont=false" 
				width="100%" height="900" frameborder="0">
			</iframe> -->
		</el-card>
		
	  
    </el-main>
	

	
  </el-container>

</el-container>
</template>

<style>
  .el-header {
    background-color: #ffffff;
    color: #333;
    line-height: 60px;

  }
  
  .el-aside {
    color: #333;
  }
  
  .box-card {
    width: auto;
	background-color: rgb(255, 247, 247);
  }

  /* .el-button{
	background-color: rgb(255, 247, 247);
  } */
 

</style>

<script>
import {Insertlesson,getetherpad,setetherpad,createtherpad,getLessondatas} from '../api/api.js'
 export default {
     data() {
       return {
		 apiKey: '850315921b51572d1b15eab03e5ff5fae31cc336b5d2098df1bdc609648e9e16',
		 
       };
     },
	 created() {
		this.createpads();
	},
	 methods: {
		saveedu() {
			sessionStorage
			const user_name = sessionStorage.getItem('user_name');
			// const user_name = localStorage.getItem('user_name');
			var LessonName = document.getElementById("LessonName").innerText;
			var Navigation = document.getElementById("Navigation").outerHTML;
			var Lessoncontent = document.getElementById("Lessoncontent").outerHTML;
			

			Insertlesson(user_name, LessonName, Navigation, Lessoncontent).then(response => {

				if(response.data.status == true){
					// 注册成功，显示成功框
					this.$message({
							message: '保存成功',
							type: 'success'
							});
				}
				else
				{
					this.$message.error('保存失败！');
				}
				})
				.catch(error => {
					this.$message.error('保存失败！！');
					});
			
			},
			lessonshare(){
				this.$message({
							message: '分享成功',
							type: 'success'
							});
			},
			getpad(padID){
				getetherpad(this.apiKey,padID).then(response =>{
					console.log(response.data)
				})
				.catch(error => {
					console.error('Error:', error);
				});
			},
			setpad(padID){
				const newText = 'Hello, Etherpad! new edit';
				setetherpad(this.apiKey,padID,newText).then(response =>{
					console.log(response.data)
				})
				.catch(error => {
					console.error('Error:', error);
				});
			},
			createpad(padID){
				createtherpad(this.apiKey,padID).then(response =>{
					console.log(response.data)
				})
				.catch(error => {
					console.error('Error:', error);
				});
			},
			createpads(){
				getLessondatas().then(response =>{
					const id = response.data;
					var etherpad_name = sessionStorage.getItem('user_name') + 20;
					console.log(etherpad_name);

					createtherpad(this.apiKey,etherpad_name).then(response =>{
						setetherpad(this.apiKey,etherpad_name,'')
						var Lessoncontent = document.getElementById("Lessoncontent");
						var src = 'http://127.0.0.1:9001/p/'+ etherpad_name +'?showControls=true&showChat=true&showLineNumbers=true&useMonospaceFont=false'
						console.log(src)
						const iframe = document.createElement('iframe');
						iframe.src = src;
						iframe.width = '100%';
						iframe.height = '800';
						Lessoncontent.appendChild(iframe);
							
					})
					.catch(error => {
						console.error('Error:', error);
					});

				})
				.catch(error => {
					console.error('Error:', error);
				});
			},
			
			
		}
   };
  
</script>