<template>
<el-container style="height: 700px; border: 1px solid #eee">

    <el-header style="text-align: right; font-size: 18px">
		<el-button icon="el-icon-share"  @click="dialogFormVisible = true" style="position: absolute;z-index: 1000;top:7%;right: 4%;">分享</el-button>
		<el-dialog title="教案分享" :visible.sync="dialogFormVisible" width="30%">
		  <el-form :model="form">
		    <el-form-item label="添加用户ID" :label-width="formLabelWidth">
		      <el-input v-model="form.name" autocomplete="off"></el-input>
		    </el-form-item>
		    <el-form-item label="用户权限:" :label-width="formLabelWidth">
		      <el-select v-model="form.limits" placeholder="请选择用户权限">
		        <el-option label="查看" value="view"></el-option>
		        <el-option label="评论" value="comment"></el-option>
				<el-option label="编辑" value="edit"></el-option>
		      </el-select>
		    </el-form-item>
		  </el-form>
		  <div slot="footer" class="dialog-footer">
		    <el-button @click="dialogFormVisible = false">取 消</el-button>
		    <el-button type="primary" @click="dialogFormVisible = false, sharelesson()">确 定</el-button>
		  </div>
		</el-dialog>
		
		<el-button icon="el-icon-coin"  @click="savelesson()">保存</el-button>
		<el-button icon="el-icon-user" circle ></el-button>
		
    </el-header>
 

  <el-container>
	 
	<div width="200px" style="background-color: rgb(238, 241, 246)" id="Navigation">
	</div>
		
    <div style="background-color: rgb(255, 255, 255)" id="Lessoncontent">
    </div>
	

	
  </el-container>

</el-container>
</template>

<style>
  .el-header {
    background-color: #ffffff;
    color: #333;
    line-height: 60px;
  }
  
 
  
  



</style>

<script>
import {getLessondata,resetlesson,insertshare} from '../api/api.js'
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';
 export default {
     data() {
       return {
         dialogFormVisible: false,
		 dialogdownload: false,
         form: {
           name: '',
           limits: '',
         },
         formLabelWidth: '120px',
		 tableData: [],
		 
       };
     },
	created() {
		this.fetchUserData();
	},
	 methods: {
		fetchUserData() {
			const id = this.$route.params.id;
			// console.log(id);
			getLessondata(id).then(response =>{
				console.log(response.data);
				this.tableData = response.data;
				//var Navigation = document.getElementById("Navigation");
				var Lessoncontent = document.getElementById("Lessoncontent");
				//Navigation.outerHTML = this.tableData[0].Navigation;
				Lessoncontent.outerHTML = this.tableData[0].Lessoncontent;
				
			})
			.catch(error => {
			console.error('Error:', error);
			});
		},
		savelesson() {
			const id = this.$route.params.id;
			//var LessonName = document.getElementById("LessonName").innerText;
			//var Navigation = document.getElementById("Navigation").outerHTML;
			var Lessoncontent = document.getElementById("Lessoncontent").outerHTML;
			
			resetlesson(id, LessonName, Navigation, Lessoncontent).then(response => {
				if(response.data.status == true){
					// 注册成功，显示成功框
					this.$message({
							message: '修改成功',
							type: 'success'
							});
				}
				else
				{
					this.$message.error('修改失败！');
				}
				})
				.catch(error => {
					this.$message.error('保存失败！！');
					});
			
		},
		sharelesson(){
			const Author = sessionStorage.getItem('user_name');
			const Sharer = this.form.name;
			const Privilege = this.form.limits;
			const Lessonid = this.$route.params.id;
			insertshare(Author,Sharer,Privilege,Lessonid).then(response => {
				if(response.data.status == true){
					// 注册成功，显示成功框
					this.$message({
							message: '分享成功',
							type: 'success'
							});
				}
				else
				{
					this.$message.error(response.data.data);
				}
				})
				.catch(error => {
					this.$message.error('分享失败！！');
					});

		},
		}
   };
  
</script>