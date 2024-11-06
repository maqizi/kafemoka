<template>
<el-container style="height: 700px; border: 1px solid #eee">

    <el-header style="text-align: right; font-size: 18px">
		<el-button icon="el-icon-share"  @click="dialogFormVisible = true">分享</el-button>
		<el-dialog title="教案分享" :visible.sync="dialogFormVisible">
		  <el-form :model="form">
		    <el-form-item label="添加用户ID" :label-width="formLabelWidth">
		      <el-input v-model="form.name" autocomplete="off"></el-input>
		    </el-form-item>
		    <el-form-item label="用户权限:" :label-width="formLabelWidth">
		      <el-select v-model="form.region" placeholder="请选择用户权限">
		        <el-option label="查看" value="shanghai"></el-option>
		        <el-option label="评论" value="beijing"></el-option>
				<el-option label="编辑" value="beijing"></el-option>
		      </el-select>
		    </el-form-item>
		  </el-form>
		  <div slot="footer" class="dialog-footer">
		    <el-button @click="dialogFormVisible = false">取 消</el-button>
		    <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
		  </div>
		</el-dialog>
		
		<el-button icon="el-icon-download"  @click="dialogdownload = true">下载</el-button>
		<el-dialog title="教案下载" :visible.sync="dialogdownload">
			<el-button icon="el-icon-download" >PDF下载</el-button>
			<el-button icon="el-icon-download" >WORD下载</el-button>
			<div slot="footer" class="dialog-footer">
			  <el-button @click="dialogdownload = false">取 消</el-button>
			  <el-button type="primary" @click="dialogdownload = false">确 定</el-button>
			</div>
		</el-dialog>
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
			<div contenteditable="true">教案内容</div>
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
import {Insertlesson} from '../api/api.js'
 export default {
     data() {
       return {
         dialogFormVisible: false,
		 dialogdownload: false,
         form: {
           name: '',
           region: '',
           date1: '',
           date2: '',
           delivery: false,
           type: [],
           resource: '',
           desc: ''
         },
         formLabelWidth: '120px',
		 LessonName: '',
		 Lessoncontent:'',
		
       };
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
			
		}
   };
  
</script>